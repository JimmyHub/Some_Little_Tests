#打開文件 讀取內容
import re,csv,time
import glob,pathlib
from selenium import webdriver
from pathlib import Path
dir_name='./{}_seq'.format(time.strftime('%m%d_%M%S'))
Path(dir_name).mkdir(parents=True,exist_ok=True)
# NCBI_Blast網址
url = 'https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome'
def blastSeq(driver,filename,seq):
    #找到輸入Seq的輸入框
    box = driver.find_element_by_class_name('reset')
    #輸入序列
    box.send_keys(seq)
    #找到blast按鈕
    button = driver.find_element_by_class_name('blastbutton')
    #點擊按鈕
    button.click()
    #等待Blast
    while True:
        try:
            #除非這個按鈕有存在 不然就會一直檢測
            button_re = driver.find_element_by_id('btnAlign')
            break
        except:
            print('blasting...')
            time.sleep(3)
    print('Blast ok!')
    #切換結果顯示
    button_re.click()
    #JS的 頁面滑動指令
    js = "var action=document.documentElement.scrollTop=8000"
    #重複 執行頁面JS指令 讓載入的元素更多
    driver.execute_script(js)
    time.sleep(5)
    driver.execute_script(js)
    time.sleep(5)
    #透過各種不同方式找到頁面中記錄 菌名 比例 跟差異的數據
    results_name = driver.find_elements_by_class_name('dlfRow')
    results_idt = driver.find_elements_by_xpath("//table[@class='alnParams']//tbody//tr[2]//td[3]")
    results_gap = driver.find_elements_by_xpath("//table[@class='alnParams']//tbody//tr[2]//td[4]")
    list_results = [('Name', 'Identity', 'Gaps'), ]
    #去除菌名結果中 空白的元素
    for n in range(len(results_name) - 1, -1, -1):
        if results_name[n].text == '':
            results_name.remove(results_name[n])
    #遍歷結果 先組合成tuple 然後存到list中
    for i in range(len(results_name)):
        name = results_name[i].text.split(',')[0]
        tuple_re = (name, results_idt[i].text, results_gap[i].text)
        list_results.append(tuple_re)
    #將list輸出成CSV檔案
    with open('{}/{}.csv'.format(dir_name,filename), 'w+') as f:
        writer = csv.writer(f)
        writer.writerows(list_results)
    print('{}完成'.format(filename))
    driver.get(url)
start = time.time()
#D1/D2 頭尾特徵設定
pattern = 'GCGAG.*CCC'
#創建 re對象 放入 匹配特徵
seq = re.compile(pattern)
#獲取當前資料夾 絕對路徑
path_ = pathlib.Path.cwd()
path_str = str(path_)
#搜尋資料夾內部 有哪些文件是 txt檔
pathlist =glob.iglob(r'{}/*.txt'.format(path_str))
#儲存 ( 菌名 跟 序列 ) 列表
list_seq =[]
# 創建driver對象
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
for path in pathlist:
    filename = path.split('\\')[-1]
    if '\\' not in filename:
        path_file = pathlib.Path(path_str+'/'+filename)
        if path_file.exists():
            with open(filename, 'r+') as f:
                str_f = ''
                for line in f.read():
                    if line != '\n':
                        str_f += line
                finall = seq.findall(str_f)
                if finall == []:
                    finall= ['0']
                seq_name = filename.split('.')[0]
                list_seq.append((seq_name,finall[0]))
                # 創建deiver對象 ('chromedriver.exe位置')
                # 一個對象是一個網頁
                if finall[0] != '0':
                    blastSeq(driver,seq_name,finall[0])
#dir_name =path_str.split('\\')[-1]
with open('{}.csv'.format(dir_name),'w+') as f:
    writer = csv.writer(f)
    writer.writerows(list_seq)
driver.close()
print('結束')
print(time.time()-start)
time.sleep(5)
