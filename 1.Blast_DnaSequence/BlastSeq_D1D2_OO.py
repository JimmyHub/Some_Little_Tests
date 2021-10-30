#打開文件 讀取內容
import re,csv,time
import glob,pathlib
from selenium import webdriver
from pathlib import Path
""" 在NCBI 網站上 blast """
class Blasting(object):
    def __init__(self,driver,dir_name,filename,seq):
        #diver對象
        self.driver = driver
        #菌名
        self.filename = filename
        #序列
        self.seq = seq
        self.dir_name = dir_name
        #儲存資料的list
        self.list_results = [('Name', 'Identity', 'Gaps'), ]
    # 找到元素並輸入內容
    def key_in(self,target):
        box = self.driver.find_element_by_class_name(target)
        box.send_keys(self.seq)
    #找到元素並點擊
    def click_in(self,tag,target):
        if tag == 'id':
            while True:
                try:
                    #除非這個按鈕有存在 不然就會一直檢測
                    button = self.driver.find_element_by_id(target)
                    break
                except:
                    print('Connecting...')
                    time.sleep(3)
        else:
            button = self.driver.find_element_by_class_name(target)
        button.click()
    #去除菌名結果中 空白的元素
    def del_space(self,name_list):
        for n in range(len(name_list) - 1, -1, -1):
            if name_list[n].text == '':
                name_list.remove(name_list[n])
    #把每筆資料做整合處理
    def collect_data(self,name_list,idt_list,gap_list):
        for i in range(len(name_list)):
            name = name_list[i].text.split(',')
            if name :
                tuple_re = (name[0], idt_list[i].text, gap_list[i].text)
                self.list_results.append(tuple_re)
    #把資料輸出成CSV檔
    def output_data(self):
        with open('{}/{}.csv'.format(self.dir_name,self.filename), 'w+') as f:
            writer = csv.writer(f)
            writer.writerows(self.list_results)
        print('{}完成'.format(self.filename))
    def run(self):
        self.key_in('reset')
        self.click_in('class','blastbutton')
        self.click_in('id','btnAlign')
        for i in range(2):
            js = "var action=document.documentElement.scrollTop=8000"
            #重複 執行頁面JS指令 讓載入的元素更多
            self.driver.execute_script(js)
            time.sleep(5)
        #透過各種不同方式找到頁面中記錄 菌名 比例 跟 差異的數據
        name_list = self.driver.find_elements_by_class_name('dlfRow')
        idt_list = self.driver.find_elements_by_xpath("//table[@class='alnParams']//tbody//tr[2]//td[3]")
        gap_list = self.driver.find_elements_by_xpath("//table[@class='alnParams']//tbody//tr[2]//td[4]")
        self.del_space(name_list)
        self.collect_data(name_list,idt_list,gap_list)
        self.output_data()

""" 獲取資料夾中的序列檔案 將序列放到 在NCBI 網站上 blast """
class BlastD1D2(object):
    def __init__(self,url):
        #儲存 ( 菌名 跟 序列 ) 列表
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get(url)
        self.dir_name = './{}_seq'.format(time.strftime('%m%d_%M%S'))
        self.list_seq = []
    def search_seq(self):
        #D1/D2 頭尾特徵設定
        pattern = 'GCGAG.*CCC'
        #創建 re對象 放入 匹配特徵
        seq = re.compile(pattern)
        return seq
    #搜尋資料夾內部 有哪些文件是 txt檔
    def find_texts(self):
        #獲取當前資料夾 絕對路徑
        path_ = pathlib.Path.cwd()
        path_str = str(path_)
        #搜尋資料夾內部 有哪些文件是 txt檔
        pathlist =glob.iglob(r'{}/*.txt'.format(path_str))
        return path_str,pathlist
    #拼湊完整的seq
    def get_fullseq(self,filename):
        with open(filename, 'r+') as f:
            str_fullseq = ''
            for line in f.read():
                if line != '\n':
                    str_fullseq += line
        return str_fullseq
    #輸出菌名跟其序列
    def output_seq(self):
        with open('{}.csv'.format(self.dir_name),'w+') as f:
            writer = csv.writer(f)
            writer.writerows(self.list_seq)
        self.driver.close()
        print('結束')
    def run(self):
        Path(self.dir_name).mkdir(parents=True,exist_ok=True)
        path_all = self.find_texts()
        path_str = path_all[0]
        pathlist = path_all[1]
        for path in pathlist:
            filename = path.split('\\')[-1]
            if '\\' not in filename:
                path_file = pathlib.Path(path_str+'/'+filename)
                if path_file.exists():
                    str_fullseq = self.get_fullseq(filename)
                    finall = self.search_seq().findall(str_fullseq)
                    if finall == []:
                        finall = ['0']
                    seq_name = filename.split('.')[0]
                    self.list_seq.append((seq_name,finall[0]))
                    if finall[0] != '0':
                        Acting = Blasting(self.driver,self.dir_name,seq_name,finall[0])
                        Acting.run()
                        self.driver.get(url)
        self.output_seq()

if __name__ == '__main__':
    url = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'
    Blast = BlastD1D2(url)
    Blast.run()