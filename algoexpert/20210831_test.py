# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:00:13 2021

@author: 88697
"""

from database import * 
#概念: 透過多次隨機取樣方式 獲得交易最大值出現的結果
import random
def maxProfitWithKTransactions(prices, k):
    #先判斷prices 列表中長度 是否符合 2個以上 不符合則直接print(0)
    if len(prices) > 1:
        #用一個列表 儲存prices 元素index
        list_num=[]
        for i in range(len(prices)):
            list_num.append(i)
        list_sum=[]
        #k值代表交易次數 假設有5次 但是不一定要交易5次才會有最大值
        #所以k如果是5 就模擬1~5次交易的情況
        for time in range(1,k+1):
            count = 0
            while count < 5000 :
                list_all=[]
                #透過迴圈獲取與k值相對數量的 不重複隨機index 
                #list_index用來儲存 不重複隨機index
                list_index=[]
                while True:
                    r = random.randint(0, len(list_num)-1)
                    if r in list_index:
                        continue
                    list_index.append(r)
                    stop = time*2-1
                    if stop > len(prices):
                        stop = len(prices) //2
                        if stop % 2 == 0:
                            stop+=1
                    if len(list_index) > stop  :
                        break
                #將list_index 裡面的index值 依照順序排列
                #來模擬交易的日子 是有序的
                list_index.sort()
                #依照隨機的index 去取prices列表裡的數值 出來做計算
                #因為是隨機取樣 所以設定5000次隨機取樣 
                #以確保最大值一定會出現
                for i in range(0,len(list_index),2):
                    num = prices[list_index[i+1]] - prices[list_index[i]]
                    list_all.append(num)
                list_sum.append(sum(list_all))
                count+=1
            if max(list_sum)<0:
                break
        #最後根據 list_sum 的最大值 搭配題目條件 去做返回 
        if max(list_sum)>0:
            return max(list_sum)
        else:
            return 0
    else:
        return 0
