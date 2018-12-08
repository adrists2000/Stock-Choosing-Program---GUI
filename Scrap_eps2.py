
import os
import json 
import Stock 


def Stockname():
    global Stock_name
    file_path0="json/other/stock_name.json"
    fp0= open(file_path0,'r')
    Stock_name=json.load(fp0)
    fp0.close()   


def Check_json_eps2(input_no):
  
    option=1
    dict_no={}
    str_no=str(input_no)    
    str1=str(input_no)[0]+"xxx"
    if Stock.Now()[1] >= 5:
        end_y=Stock.Now()[0]-1     #視情況 此處設定每年5月作切換
    else: 
        end_y=Stock.Now()[0]-2                           #end_y=所需資料的最新一年
    season=Stock.Decide_season()
    if season=="Q4":
        str_sea=str(Stock.Now()[0]-1)[2:4]+season
    else:
        str_sea=str(Stock.Now()[0])[2:4]+season          #str_sea=所需資料的最新一季       
    
    file_path="json/eps2/"+ str1 + "_eps2.json"    #      
    if os.path.exists(file_path):
        fp1 = open(file_path,'r') 
        dict_large=json.load(fp1)                
        if str_no in dict_large:
            if str(end_y) in dict_large[str_no]:   #設定最新一年!! 視情況!!  
                dict_no=dict_large[str_no]
#                print("\n由原本JSON檔案讀取[" +str_no+ "]EPS資料成功(最新!)")
                option=0
            elif str_sea in dict_large[str_no]:
                print("\n["+str_no+"]的EPS資料可能尚未滿一年!")
                option=0
            else: 
                print("\n原本JSON檔案中[" +str_no+ "]的EPS資料不是最新的")  #option=1 執行網路爬蟲
        else: print("\n"+str_no+"的EPS資料尚未在json檔案裡")              #option=1 執行網路爬蟲
    else: print("\n"+file_path+"檔案不存在")                        #option=1 執行網路爬蟲    
#    print(dict_no)
    return option,dict_no,end_y  


def Generate_URL_eps2(input_no):
    url_0="https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID={0}&YEAR_PERIOD=9999&RPT_CAT=M_YEAR" 
    url=url_0.format(str(input_no))
    print("由台灣股市資訊網擷取資料...")
#    print("\n股票代號=",input_no)
#    print("URL=",url)
    return url


def Delete_data_eps2(no_list):
    for input_no in no_list:
        dict_large={}
        str1=str(input_no)[0]+"xxx"
        str_no=str(input_no)
        file_path="json/eps2/"+ str1 + "_eps2.json"
        if os.path.exists(file_path):
            fp=open(file_path,'r') 
            dict_large=json.load(fp)
            fp.close()
            if str_no in dict_large:
                del dict_large[str_no]
                fp=open(file_path,'w')
                json.dump(dict_large,fp)
                fp.close()
                print("\n已刪除JSON檔案中"+str_no+"的EPS資料")
            else:
                print("\nJSON檔案中沒有"+str_no+"的EPS資料")
                
                
def Scrap_data_eps2(input_no,soup):
    
    dict_large={}
    dict_small={}
    str1=str(input_no)[0]+"xxx"
    str_no=str(input_no)
    file_path="json/eps2/"+ str1 + "_eps2.json"
    if os.path.exists(file_path):
        with open(file_path,'r') as fp1: 
            dict_large=json.load(fp1)
                            
    tag_test=soup.find(text="查無資料")          
    tag_div=soup.find(id="divFinDetail")
    if (tag_test != None) :
        print("台灣股市資訊網:查無此股票資料")        
    elif (tag_div != None):            
        print("\n--歷年每年獲利(EPS)--")
        for i in range(12):                     #設定抓取12年資料 視情況!!
            string="row"+str(i)
            tag_tr=tag_div.find(id=string)
            if (tag_tr != None):
                tag_nobr_list=tag_tr.select("td nobr")
                str1=tag_nobr_list[0].string
                tag3=tag_nobr_list[-3]
                tag_a=tag3.find("a")
                if (tag_a != None):
                    str2=tag_a.string
                    if ( str2 != (None and "-") ):
                        dict_small[str1]=str2
                        print(" ",str1,"    ",str2)
                    else:
                        print(" ",str1,"     (無EPS資料)")
                else:
                    print(" ",str1,"     (無EPS資料)")     
            else:
                print("超出歷史年份資料範圍!")
        dict_large[str_no]=dict_small 
        with open(file_path,'w') as fp1: 
            json.dump(dict_large,fp1)        
        print("--------------------")
        print("寫入JSON檔成功")
    else:
        print("台灣股市資訊網:目前連線錯誤") 
         
    return dict_small    


def Calculate_eps2(input_no,dict_no,end_y,cond2):        
    
    select=0
    if dict_no!={}:
        fp = open("Result.txt","a",encoding="utf8") 
        str_no=str(input_no)        
        if str_no in Stock_name:
            print("\n股票: ["+str_no+"] ["+Stock_name[str_no]+"]")
            fp.write("\n股票: ["+str_no+"] ["+Stock_name[str_no]+"]\n")
        else:
            print("\n股票號碼= "+str_no)
            fp.write("\n股票號碼= "+str_no)
        
        print("年份      EPS")
        fp.write("年份      EPS")        
        miss=0
        sum_all=0
        sum2_all=0
        for i in range(cond2[0]):
            str1=str(end_y-i)                    
            if str1 in dict_no:
                str2=dict_no[str1]
                print(str1,"    ",str2)
                fp.write("\n"+str1+"     "+str2)
                if str2 != ("-" and "--"):
                    sum_all += float(str2)
                    sum2_all += pow(float(str2),2)
                else: miss+=1
            else: miss+=1
        count=cond2[0]-miss            #可計算的年份
        if count==0:
            print("無法計算過去幾年EPS的變異係數")
            fp.write("\n無法計算過去幾年EPS的變異係數\n")
        else:
            avg=sum_all/float(count)  
            print("\n過去"+str(count)+"年平均EPS為",avg)
            fp.write("\n過去"+str(count)+"年平均EPS為"+str(avg))
#            print("sum2_all=",sum2_all)
#            print("sum2_all/float(count)",sum2_all/float(count) )
#            print("avg*avg",(avg*avg) )
            var0=( sum2_all/float(count) ) - (avg*avg)    #變異數公式
            dev0= pow(var0,0.5)                           #開根號變 標準差 
            coef0= dev0/avg                               #變異係數公式
            print("變異數=",var0," 標準差=",dev0)
            print("變異係數=",coef0)
            fp.write("\n變異數="+str(var0)+"  標準差="+str(dev0))
            fp.write("\n變異係數="+str(coef0))
            if coef0 < cond2[1]:
                print("變異係數 < "+str(cond2[1]) )
                fp.write("  < "+str(cond2[1]))
                select=1
            else:
                print("變異係數 > "+str(cond2[1]) )
                fp.write("  > "+str(cond2[1]))

        print("\n********************************************************")
        fp.write("\n\n********************************************************\n")
        fp.close()        
    return select
        
#--------------------------------------------------------------------------------

def Main_eps2(LIST_NO,COND2):
    
    print("\n\n*******************[Main_EPS2 Program]*******************\n")
    with open("Result.txt","a",encoding="utf8") as fp:
        fp.write("\n\n*******************[Main_EPS2 Program]*******************\n\n") 
        
    LIST_SELECT=[] 
    Stockname()       
    for INPUT_NO in LIST_NO:
        OPTION,DICT_NO,END_Y=Check_json_eps2(INPUT_NO)
        if OPTION==1:
            URL=Generate_URL_eps2(INPUT_NO)
            SOUP=Stock.Get_soup(URL,310,3.5)
            DICT_NO=Scrap_data_eps2(INPUT_NO,SOUP) 
        SELECT=Calculate_eps2(INPUT_NO,DICT_NO,END_Y,COND2)                   
        if (SELECT==1): LIST_SELECT.append(INPUT_NO)
        
    print("\n階段選股清單:")
    print(LIST_SELECT)
    with open("Result.txt","a",encoding="utf8") as fp:
        fp.write("\n階段選股清單:\n"+str(LIST_SELECT)+"\n")
        
    return LIST_SELECT

#------------------------------------------------------------------------

if __name__=="__main__":

#    no_list=[1563]
#    Delete_data_roe(no_list)
    
#    LIST_NO=Stock.List_all()   
#    LIST_NO=Stock.Read_list_300("300")     
    LIST_NO=[3711] 
    COND2=[9,1]
    LIST_SELECT=Main_eps2(LIST_NO,COND2)










