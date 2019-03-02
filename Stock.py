
import os
import requests
import time
import csv
import json
from bs4 import BeautifulSoup


def List_all():

    List_NO=[]
    List_0=[1216,1232,1513,1521,1730,1773,1788,2330,2373,2385,2412,2414,2480,2823,2891,2892,3010,3042,3045,3501,4205,4527,4535,4904,5880,6023,6224,6508,6803,8341,8422,8435,8926,9908,9911,9942] # 4103, 6024,8341
    List_1=[1215,1229,1264,1307,1712,2420,2450,2451,2459,2493,2616,2729,2820,2908,3130,3702,4104,4974,5871,6112,6189,6201,6216,6263,6277,6281,6285,8923,8931,9917,9925,9941,9943]    
    List_2=[1231,1451,1558,1726,2105,2114,2355,2433,2608,2903,4506,4532,4706,5706,6128,6192,6206,6214,9930,9933]
    List_3=[1233,1507,1604,2382,2834,2880,2881,2882,2884,2885,2886,2890,2891,2892,2912,5312,5434,5880,6136,6184,6202,8083,8406,9924]
    List_NO.extend(List_0)
    List_NO.extend(List_1)
    List_NO.extend(List_2)
    List_NO.extend(List_3)    
    List_4=[1580,1593,2376,2455,2889,3563,4305,4736,5007,5487,5706,6146,8210,8446,9905,9937]    #待確認穩定型
    List_5=[2104,2476,3088,3213,3416,3479,3705,5493,6154,6290,6464,8042,8255,8916]    #待確認選股區
    List_6=[1234,1702,2377,2383,2397,2441,2727,3617,3665,5287,5388,8016,8050]              #待確認成長型 ,3299
    List_7=[1535,1537,1560,1707,1723,2015,2104,2114,2347,3022,3023,3388,4104,4175,4722,6184,8109,8114,9904,9910,9951]  #雜誌 #8359    
    List_NO.extend(List_4)
    List_NO.extend(List_5)
    List_NO.extend(List_6)
    List_NO.extend(List_7)      
    print("\n取得作者自選定存股清單中...")
#    print(List_NO)            
    return List_NO


def Now():
    sec0=time.time()
    tlocal=time.localtime(sec0)
    # tlocal[0],tlocal[1],tlocal[2],tlocal[3],tlocal[4],tlocal[5] 代表 年 月 日 時 分 秒 
    return tlocal
    

def Decide_season():
    month=Now()[1]
    day=Now()[2]
    days=(month-1)*30+day
    yr=0
    if days>315: season="Q3"
    elif days>225 and days<=315: season="Q2"
    elif days>105 and days<=225: season="Q1"
    elif days<85: 
        season="Q3"
        yr=-1
    else:
        season="Q4"
        yr=-1
    return season,yr


def Make_dir(string):
    if not os.path.exists(string+"/"):
        os.mkdir(string)
        print(string+"資料夾已建立")
    else:
        print(string+"資料夾已存在")
 

def Get_list_300(number):
    print("\n取得市值排名前"+number+"之股票清單中...")
    List_num=[]
    url="https://goodinfo.tw/StockInfo/StockList.asp?MARKET_CAT=%E7%86%B1%E9%96%80%E6%8E%92%E8%A1%8C&INDUSTRY_CAT=%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%E6%9C%80%E9%AB%98%40%40%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%40%40%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%E6%9C%80%E9%AB%98&SHEET=%E5%85%AC%E5%8F%B8%E5%9F%BA%E6%9C%AC%E8%B3%87%E6%96%99&RPT_TIME=&SHEET2=%E7%8D%B2%E5%88%A9%E8%83%BD%E5%8A%9B"
    soup=Get_soup(url,310,0.3)                
    tag_tr=soup.find(id="hrow0") 
    tag_list=[tag_tr]
    tag_list0=tag_tr.find_next_siblings()
    tag_list.extend(tag_list0)    
    print("市值排名   股票號碼")    
    for tag in tag_list:
        td_list=tag.find_all("td")
        s1=td_list[0].string
        s2=td_list[1].nobr.a.string
        print(s1,"       ",s2)
        List_num.append([s1,s2])
        if s1==number:
            break        
    file_path="csv/stock300.csv"
    fp = open(file_path,'w',newline='')
    writer=csv.writer(fp)
    for small_list in List_num:
        writer.writerow(small_list)
    fp.close()    


def Read_list_300(number):
    print("\n取得市值排名前"+number+"之股票清單中...")
    file_path="csv/stock300.csv"
    if os.path.exists(file_path):
        fp = open(file_path,'r')
        reader=csv.reader(fp)        
        List_NO=[]
        num=0
        for row in reader:
            List_NO.append(row[1])
            num+=1
            if num==int(number):
                break
        fp.close()
    print(List_NO)    
    return List_NO    


def Get_stock_name():
    print("取得上市上櫃股票號碼跟名稱")
    list1=[i for i in range(11,38)] 
    list2=[i for i in range(41,69)]
    list2.remove(63)
    list3=["00","01",74,75,80,81,82,83,84,89,91,98,99]
    total=[]
    total.extend(list1)
    total.extend(list2)
    total.extend(list3)
    Stock_name={}
    Stock_number={}
    for no in total:
        url_0="https://goodinfo.tw/StockInfo/StockList.asp?MARKET_CAT=%E5%85%A8%E9%83%A8&STOCK_CODE={0}&SHEET=%E4%BA%A4%E6%98%93%E7%8B%80%E6%B3%81&SHEET2=%E6%97%A5&RPT_TIME=%E6%9C%80%E6%96%B0%E8%B3%87%E6%96%99"
        url=url_0.format(str(no))
        soup=Get_soup(url,180,3)
        tag_test=soup.find(text="查無資料!!") 
        if tag_test==None:
            tag_tr_0=soup.find(id="row0")
            if tag_tr_0!=None:
                tag_tr_123=tag_tr_0.find_next_siblings()
                tag_tr_list=[]
                tag_tr_list.append(tag_tr_0)
                tag_tr_list.extend(tag_tr_123)
                for tr in tag_tr_list: 
                    td_list=tr.find_all("td")
                    str0=td_list[0].nobr.a.string
                    str1=td_list[1].nobr.a.string
                    print(str0,str1)
                    Stock_name[str0]=str1
                    Stock_number[str1]=str0
            else: print("id=row0搜尋不到")
        else: print("此號碼開頭查無資料!")
    file_path1="json/other/stock_name.json"
    file_path2="json/other/stock_number.json"
    fp1= open(file_path1,'w')  
    json.dump(Stock_name,fp1) 
    fp1.close()
    fp2= open(file_path2,'w')  
    json.dump(Stock_number,fp2) 
    fp2.close()       
#    fp1= open(file_path1,'r')
#    Stock_name0=json.load(fp1)
#    print(Stock_name0)
#    fp2= open(file_path2,'r')
#    Stock_number0=json.load(fp2)
#    print(Stock_number0)

    
def Get_soup(url,time1,time2):
    headers={"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    aa=1
    while(aa==1):
        try:
            html=requests.get(url,headers=headers)
            aa=0
        except requests.exceptions.ConnectionError as ex3:
            print("網路連線錯誤: " + str(ex3) )
            print("等待"+str(time1)+"秒再次嘗試連線")
            time.sleep(time1)
        
    if html.status_code==requests.codes.ok:        
        html.encoding="utf8"
        print("HTML取得成功")
        soup=BeautifulSoup(html.text, "lxml")
#        print("SOUP取得成功")  
    else:
        print("HTML取得失敗")
#        print("SOUP取得失敗") 
        soup=[]
    time.sleep(time2)
    return soup
   

def Soup_to_note(string1,string2,soup):
    filename="{0}_{1}.txt".format(string1,string2)
    prettysoup=soup.prettify()
    fp=open(filename,"w",encoding="utf8")
    fp.write(prettysoup)
    print("將SOUP寫入檔案",filename)
    fp.close()
    
#-----------------------------------------------------------

if __name__=="__main__":

#    List_NO=Read_list_300("300")
#    Get_stock_name()
    seasont=Decide_season()
    print(seasont)
    print("stockstock")
        
        
        
        
        

