import tkinter as tk
import Stock
import json
import csv
import os

#----------------------------------------------------------------------------
      
class WIN1_FM1:
    def __init__(self,win,wd,ht,color):
        self.rt1=tk.Frame(win,width=wd,height=ht,bg=color)
        self.rt1.pack(side="top")
        label1=tk.Label(self.rt1,text="選股小程式",font=("新細明體",26))
        label1.place(relx=0.5,rely=0.5,anchor="center")
        self.rt2=tk.Frame(win,width=wd,height=3,bg="white")
        self.rt2.pack(side="top")

#----------------------------------------------------------------------------
        
class WIN1_FM2:
    def __init__(self,win,wd,ht,color):
        self.rt2=tk.Frame(win,width=wd,height=ht,bg=color)
        self.rt2.pack()          

    def back_to_1(self):     
        self.rt2.destroy() 
        frame2_1=WIN1_FM2(win,1280,610,"#1E90FF")
        frame2_1.fm2_1()            

    def back_to_2(self):      
        self.rt2.destroy() 
        frame2_2=WIN1_FM2(win,1280,610,"#1E90FF")
        frame2_2.fm2_2()  

    def back_to_2user(self):
        self.rt2.destroy()
        frame2_2user=WIN1_FM2(win,1280,610,"#1E90FF")
        frame2_2user.fm2_2user()         

#------------------------------------------------------------------------------

    def fm2_1(self):
        def decide_1():
            global listno
            listno=Stock.List_all()
            self.rt2.destroy()
            frame2_2=WIN1_FM2(win,1280,610,"#1E90FF")
            frame2_2.fm2_2()
        def decide_2():
            global listno
            listno=Stock.Read_list_300("150")   
            self.rt2.destroy()
            frame2_2=WIN1_FM2(win,1280,610,"#1E90FF")
            frame2_2.fm2_2()
        def decide_3():
            global listno
            listno=Stock.Read_list_300("300") 
            self.rt2.destroy()
            frame2_2=WIN1_FM2(win,1280,610,"#1E90FF")
            frame2_2.fm2_2()
        def decide_user():
            self.rt2.destroy()
            frame2_2user=WIN1_FM2(win,1280,610,"#1E90FF")
            frame2_2user.fm2_2user()            
        def decide_update_a():
            label5=tk.Label(self.rt2,text="此更新可能會耗時數小時\n需視上次更新時間而定",font=("新細明體",18),bg="#1E90FF")
            label5.place(relx=0.78,rely=0.69,anchor="s")
            button5a=tk.Button(self.rt2,text="確定",font=("新細明體",18),relief="groove",command=decide_update_b)
            button5a.place(relx=0.75,rely=0.75,anchor="center")
            button5b=tk.Button(self.rt2,text="取消",font=("新細明體",18),relief="groove",command=self.back_to_1)
            button5b.place(relx=0.82,rely=0.75,anchor="center")
        def decide_update_b():
            global listno,condi0,prior,exe
            win.destroy()
            #Stock.Get_stock_name()
            listno=Stock.List_all()
            Stock.Get_list_300("300")
            listno.extend( Stock.Read_list_300("300") )
            condi0=False
            prior=["a","b","c","e","f"]
            exe=1
           
        label1=tk.Label(self.rt2,text="請選擇一個股票清單:",font=("新細明體",20),bg="#1E90FF")
        label1.place(relx=0.3,rely=0.15,anchor="e")
        button1=tk.Button(self.rt2,text="作者自選定存股清單",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_1)
        button1.place(relx=0.5,rely=0.15,anchor="center")
        button2=tk.Button(self.rt2,text="市值排名前150之股票清單",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_2)
        button2.place(relx=0.5,rely=0.28,anchor="center")
        button3=tk.Button(self.rt2,text="市值排名前300之股票清單",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_3)
        button3.place(relx=0.5,rely=0.41,anchor="center")
        button4=tk.Button(self.rt2,text="自訂股票清單",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_user)
        button4.place(relx=0.5,rely=0.54,anchor="center")
        label2=tk.Label(self.rt2,text="其他選項:",font=("新細明體",20),bg="#1E90FF")
        label2.place(relx=0.3,rely=0.75,anchor="e")
        button5=tk.Button(self.rt2,text="更新所有內建資料庫數據",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_update_a)
        button5.place(relx=0.5,rely=0.75,anchor="center")

#------------------------------------------------------------------------------

    def fm2_2user(self): 
        def decide_user1():
            self.rt2.destroy()
            frame2_3user=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3user.fm2_3user1()
        def decide_user2():
            self.rt2.destroy()
            frame2_3user=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3user.fm2_3user2()
        def decide_user3():
            self.rt2.destroy()
            frame2_3user=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3user.fm2_3user3()
        def decide_user4():
            self.rt2.destroy()
            frame2_3user=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3user.fm2_3user4()
            
        label1=tk.Label(self.rt2,text="請選擇:",font=("新細明體",20),bg="#1E90FF")
        label1.place(relx=0.3,rely=0.15,anchor="e")
        button1=tk.Button(self.rt2,text="新增或刪除股票清單",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_user1)
        button1.place(relx=0.5,rely=0.15,anchor="center")
        button2=tk.Button(self.rt2,text="使用儲存的股票清單作篩選",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_user2)
        button2.place(relx=0.5,rely=0.28,anchor="center")
        button3=tk.Button(self.rt2,text="直接輸入股票清單作篩選",font=("新細明體",18),width=30,height=2,relief="groove",command=decide_user3)
        button3.place(relx=0.5,rely=0.41,anchor="center")

        button9=tk.Button(self.rt2,text="回前一頁",font=("新細明體",18),width=15,height=1,pady=6,relief="groove",command=self.back_to_1)
        button9.place(relx=0.15,rely=0.9,anchor="center")


    def show_list(self,list_new): 
        file_path1="json/other/stock_number.json"
        with open(file_path1,'r') as fp1:
            Stock_number=json.load(fp1) 
        file_path2="json/other/stock_name.json"
        with open(file_path2,'r') as fp2:
            Stock_name=json.load(fp2)           
        text1=tk.Text(self.rt2,font=("新細明體",18),width=18,height=15)
        text2=tk.Text(self.rt2,font=("新細明體",18),width=18,height=15)
        text3=tk.Text(self.rt2,font=("新細明體",18),width=18,height=15)
        text4=tk.Text(self.rt2,font=("新細明體",18),width=18,height=15)
        text5=tk.Text(self.rt2,font=("新細明體",18),width=18,height=15)
        text6=tk.Text(self.rt2,font=("新細明體",18),width=18,height=15)
        length=len(list_new)            
        for i in [i for i in range(length) if i%6==0]:
            si=list_new[i]
            if si in Stock_name    : text1.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
            elif si in Stock_number: text1.insert(tk.INSERT," "+Stock_number[si]+" "+si+"\n")  
            else                   : text1.insert(tk.INSERT," "+si+"\n")
        for i in [i for i in range(length) if i%6==1]:
            si=list_new[i]
            if si in Stock_name    : text2.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
            elif si in Stock_number: text2.insert(tk.INSERT," "+Stock_number[si]+" "+si+"\n")  
            else                   : text2.insert(tk.INSERT," "+si+"\n")
        for i in [i for i in range(length) if i%6==2]:
            si=list_new[i]
            if si in Stock_name    : text3.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
            elif si in Stock_number: text3.insert(tk.INSERT," "+Stock_number[si]+" "+si+"\n")  
            else                   : text3.insert(tk.INSERT," "+si+"\n")
        for i in [i for i in range(length) if i%6==3]:
            si=list_new[i]
            if si in Stock_name    : text4.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
            elif si in Stock_number: text4.insert(tk.INSERT," "+Stock_number[si]+" "+si+"\n")  
            else                   : text4.insert(tk.INSERT," "+si+"\n")
        for i in [i for i in range(length) if i%6==4]:
            si=list_new[i]
            if si in Stock_name    : text5.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
            elif si in Stock_number: text5.insert(tk.INSERT," "+Stock_number[si]+" "+si+"\n")  
            else                   : text5.insert(tk.INSERT," "+si+"\n")
        for i in [i for i in range(length) if i%6==5]:
            si=list_new[i]
            if si in Stock_name    : text6.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
            elif si in Stock_number: text6.insert(tk.INSERT," "+Stock_number[si]+" "+si+"\n")  
            else                   : text6.insert(tk.INSERT," "+si+"\n")
        text1.place(relx=0.05,rely=0.15,anchor="nw")
        text2.place(relx=0.20,rely=0.15,anchor="nw")
        text3.place(relx=0.35,rely=0.15,anchor="nw")
        text4.place(relx=0.50,rely=0.15,anchor="nw")
        text5.place(relx=0.65,rely=0.15,anchor="nw")
        text6.place(relx=0.80,rely=0.15,anchor="nw") 
        text1.config(state=tk.DISABLED)
        text2.config(state=tk.DISABLED)
        text3.config(state=tk.DISABLED)
        text4.config(state=tk.DISABLED)
        text5.config(state=tk.DISABLED)
        text6.config(state=tk.DISABLED)


    def fm2_3user1(self):
        def add_list():
            global Saving,i_list
            i_list=len(Saving)
            Saving.append([])            
            show_list2() 
            suc.set("")
        def del_list():
            global Saving,i_list
            del Saving[i_list]
            i_list-=1
            show_list2()
            suc.set("")            
        def show_list1():
            global i_list
            if i_list > 0 :
                i_list-=1
            list_num.set("股票清單"+str(i_list+1))
            self.show_list(Saving[i_list]) 
            suc.set("")               
        def show_list2():
            global i_list
            if i_list < len(Saving)-1 : 
                i_list+=1
            list_num.set("股票清單"+str(i_list+1))
            self.show_list(Saving[i_list])
            suc.set("")
        def add_user1():
            global Saving 
            s1=e1_var_user1.get()
            e1_var_user1.set("")
            if s1 in Stock_number:
                s2=Stock_number[s1]
                Saving[i_list].append(s2)
            else:
                Saving[i_list].append(s1)            
            self.show_list(Saving[i_list])
            suc.set("")
            button2=tk.Button(self.rt2,text="儲存清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=save_list) 
            button2.place(relx=0.90,rely=0.9,anchor="e")
        def del_user1():
            global Saving
            s1=e1_var_user1.get()
            e1_var_user1.set("")
            if s1 in Saving[i_list]:
                Saving[i_list].remove(s1) 
                suc.set("")
            elif s1 in Stock_number:
                s2=Stock_number[s1]
                if s2 in Saving[i_list]:
                    Saving[i_list].remove(s2)
                    suc.set("")
                else:      
                    suc.set("刪除輸入錯誤")
                    print("刪除失敗")
            else:
                suc.set("刪除輸入錯誤") 
                print("刪除失敗")
            self.show_list(Saving[i_list])            
            button2=tk.Button(self.rt2,text="儲存清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=save_list) 
            button2.place(relx=0.90,rely=0.9,anchor="e")
        def save_list():
            file_path3="csv/User_lists.csv"
            fp3=open(file_path3,'w',newline='')
            writer=csv.writer(fp3)
            for list0 in Saving:
                writer.writerow(list0)
            fp3.close()
            suc.set("儲存清單成功")
            button3=tk.Button(self.rt2,text="完成",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2user) 
            button3.place(relx=0.91,rely=0.9,anchor="w") 

        global i_list,Saving
        i_list=0 
        Saving=[] 
        file_path3="csv/User_lists.csv"
        fp3 = open(file_path3,'r')
        reader=csv.reader(fp3)        
        for row in reader:
            Saving.append(row)
        fp3.close()
        file_path1="json/other/stock_number.json"
        with open(file_path1,'r') as fp1:
            Stock_number=json.load(fp1)
        
        self.show_list(Saving[i_list])
        button_up=tk.Button(self.rt2,text="上一份清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=show_list1) 
        button_up.place(relx=0.85,rely=0.1,anchor="e")        
        button_down=tk.Button(self.rt2,text="下一份清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=show_list2) 
        button_down.place(relx=0.85,rely=0.1,anchor="w")

        button_add=tk.Button(self.rt2,text="新增清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=add_list) 
        button_add.place(relx=0.14,rely=0.1,anchor="e")        
        button_del=tk.Button(self.rt2,text="刪除清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=del_list) 
        button_del.place(relx=0.14,rely=0.1,anchor="w")

        list_num=tk.StringVar()
        label0=tk.Label(self.rt2,textvariable=list_num,font=("新細明體",24))
        label0.place(relx=0.5,rely=0.1,anchor="center")
        list_num.set("股票清單"+str(i_list+1))

        label1=tk.Label(self.rt2,text="請輸入股票代號或名稱: ",font=("新細明體",18),width=20,bg="#20B2AA")
        label1.place(relx=0.5,rely=0.9,anchor="e")
        e1_var_user1=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_user1,font=("新細明體",18))
        entry1.place(relx=0.5,rely=0.9,anchor="w")
        button1=tk.Button(self.rt2,text="新增",font=("新細明體",18),padx=0,pady=0,relief="groove",command=add_user1) 
        button1.place(relx=0.71,rely=0.9,anchor="center")        
        button2=tk.Button(self.rt2,text="刪除",font=("新細明體",18),padx=0,pady=0,relief="groove",command=del_user1) 
        button2.place(relx=0.77,rely=0.9,anchor="center")
        button9=tk.Button(self.rt2,text="回前一頁",font=("新細明體",18),width=15,height=1,pady=6,relief="groove",command=self.back_to_2user)
        button9.place(relx=0.15,rely=0.9,anchor="center")
        suc=tk.StringVar()
        label9=tk.Label(self.rt2,textvariable=suc,font=("新細明體",18),fg="blue",bg="#20B2AA")
        label9.place(relx=0.85,rely=0.82,anchor="center")
        suc.set("")

       
    def fm2_3user2(self):           
        def show_list1():
            global i_list
            if i_list > 0 :
                i_list-=1
            list_num.set("股票清單"+str(i_list+1))
            self.show_list(Saving[i_list])               
        def show_list2():
            global i_list
            if i_list < len(Saving)-1 : 
                i_list+=1
            list_num.set("股票清單"+str(i_list+1))
            self.show_list(Saving[i_list])
        def decide_goto2():
            global listno
            listno=Saving[i_list]
            self.back_to_2()
            
        global i_list,Saving
        i_list=0 
        Saving=[] 
        file_path3="csv/User_lists.csv"
        fp3 = open(file_path3,'r')
        reader=csv.reader(fp3)        
        for row in reader:
            Saving.append(row)
        fp3.close()
#        file_path1="json/other/stock_number.json"
#        with open(file_path1,'r') as fp1:
#            Stock_number=json.load(fp1)
            
        self.show_list(Saving[i_list])
        button_up=tk.Button(self.rt2,text="上一份清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=show_list1) 
        button_up.place(relx=0.85,rely=0.1,anchor="e")        
        button_down=tk.Button(self.rt2,text="下一份清單",font=("新細明體",18),padx=0,pady=0,relief="groove",command=show_list2) 
        button_down.place(relx=0.85,rely=0.1,anchor="w")

        list_num=tk.StringVar()
        label0=tk.Label(self.rt2,textvariable=list_num,font=("新細明體",24))
        label0.place(relx=0.5,rely=0.1,anchor="center")
        list_num.set("股票清單"+str(i_list+1))

        button3=tk.Button(self.rt2,text="選定此股票清單\n開始選取篩選條件",font=("新細明體",20),width=20,height=2,pady=3,relief="groove",command=decide_goto2) 
        button3.place(relx=0.5,rely=0.9,anchor="center")
        button9=tk.Button(self.rt2,text="回前一頁",font=("新細明體",18),width=15,height=1,pady=6,relief="groove",command=self.back_to_2user)
        button9.place(relx=0.15,rely=0.9,anchor="center")

        
    def fm2_3user3(self):
        def add_user3():
            global list_new,listno

            s1=e1_var_user3.get()
            e1_var_user3.set("")
            if s1 in Stock_number:
                s2=Stock_number[s1]
                list_new.append(s2)
            else:
                list_new.append(s1)            
            self.show_list(list_new)
            listno=list_new
            button3=tk.Button(self.rt2,text="開始選取篩選條件",font=("新細明體",18),padx=0,pady=8,relief="groove",command=self.back_to_2) 
            button3.place(relx=0.81,rely=0.9,anchor="w")         
        def del_user3():
            global list_new,listno 
            s1=e1_var_user3.get()
            e1_var_user3.set("")
            if s1 in list_new:
                list_new.remove(s1) 
            elif s1 in Stock_number:
                s2=Stock_number[s1]
                if s2 in list_new:
                    list_new.remove(s2)           
            self.show_list(list_new)
            listno=list_new
            
        global list_new
        list_new=[]
        file_path1="json/other/stock_number.json"
        with open(file_path1,'r') as fp1:
            Stock_number=json.load(fp1)        
        label1=tk.Label(self.rt2,text="請輸入股票代號或名稱: ",font=("新細明體",18),width=20,bg="#20B2AA")
        label1.place(relx=0.5,rely=0.9,anchor="e")
        e1_var_user3=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_user3,font=("新細明體",18))
        entry1.place(relx=0.5,rely=0.9,anchor="w")
        button1=tk.Button(self.rt2,text="新增",font=("新細明體",18),padx=0,pady=0,relief="groove",command=add_user3) 
        button1.place(relx=0.71,rely=0.9,anchor="center") 
        button2=tk.Button(self.rt2,text="刪除",font=("新細明體",18),padx=0,pady=0,relief="groove",command=del_user3) 
        button2.place(relx=0.77,rely=0.9,anchor="center")       
        button9=tk.Button(self.rt2,text="回前一頁",font=("新細明體",18),width=15,height=1,pady=6,relief="groove",command=self.back_to_2user)
        button9.place(relx=0.15,rely=0.9,anchor="center")

#---------------------------------------------------------------------------------------------------------------
               
    def fm2_2(self):
        def decide_a():
            self.rt2.destroy()
            frame2_3=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3.fm2_3a()
        def decide_b():
            self.rt2.destroy()
            frame2_3=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3.fm2_3b()
        def decide_c():
            self.rt2.destroy()
            frame2_3=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3.fm2_3c() 
        def decide_d():
            self.rt2.destroy()
            frame2_3=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3.fm2_3d()   
        def decide_e():
            self.rt2.destroy()
            frame2_3=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3.fm2_3e()   
        def decide_f():
            self.rt2.destroy()
            frame2_3=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_3.fm2_3f() 
        def decide_gofirst():
            global prior,exe
            prior=pri0
            exe=1
            win.destroy()
        def decide_priority():
            self.rt2.destroy()
            frame2_4=WIN1_FM2(win,1280,610,"#20B2AA")
            frame2_4.fm2_4()
        def delete_a():
            global condi1
            condi1="__"
            self.back_to_2()
        def delete_b():
            global condi2_1,condi2_2
            condi2_1=condi2_2="__"
            self.back_to_2()
        def delete_c():
            global condi3
            condi3=["__"]
            self.back_to_2()
        def delete_d():
            global condi4_1,condi4_2
            condi4_1=condi4_2="__"
            self.back_to_2()
        def delete_e():
            global condi5_1,condi5_2
            condi5_1=condi5_2="__"
            self.back_to_2()
        def delete_f():
            global condi6
            condi6="__"
            self.back_to_2()
            
        b1_var_2,b2_var_2,b3_var_2=tk.StringVar(),tk.StringVar(),tk.StringVar()
        b4_var_2,b5_var_2,b6_var_2=tk.StringVar(),tk.StringVar(),tk.StringVar()        
        label0=tk.Label(self.rt2,text="請選擇篩選條件:",font=("新細明體",22),bg="#1E90FF",width=20,height=1)
        label0.place(relx=0.5,rely=0.09,anchor="center")
        button1=tk.Button(self.rt2,textvariable=b1_var_2,font=("新細明體",18),width=50,height=1,padx=20,relief="groove",anchor="w",command=decide_a)
        button1.place(relx=0.5,rely=0.18,anchor="center")
        button2=tk.Button(self.rt2,textvariable=b2_var_2,font=("新細明體",18),width=50,height=1,padx=20,relief="groove",anchor="w",command=decide_b)
        button2.place(relx=0.5,rely=0.27,anchor="center")
        button3=tk.Button(self.rt2,textvariable=b3_var_2,font=("新細明體",18),width=50,height=1,padx=20,relief="groove",anchor="w",command=decide_c)
        button3.place(relx=0.5,rely=0.36,anchor="center")
        button4=tk.Button(self.rt2,textvariable=b4_var_2,font=("新細明體",18),width=50,height=1,padx=20,relief="groove",anchor="w",command=decide_d)
        button4.place(relx=0.5,rely=0.45,anchor="center")
        button5=tk.Button(self.rt2,textvariable=b5_var_2,font=("新細明體",18),width=50,height=1,padx=20,relief="groove",anchor="w",command=decide_e)
        button5.place(relx=0.5,rely=0.54,anchor="center")
        button6=tk.Button(self.rt2,textvariable=b6_var_2,font=("新細明體",18),width=50,height=1,padx=20,relief="groove",anchor="w",command=decide_f)
        button6.place(relx=0.5,rely=0.63,anchor="center") 
        b1_var_2.set("(a) 今年累計EPS 大於等於 過去"+condi1+"年平均同期累計EPS ") 
        b2_var_2.set("(b) 近"+condi2_1+"年EPS的變異係數小於"+condi2_2 ) 
        b3_var_2.set("(c) 最新收盤價 小於 "+(",".join(condi3))+" 年均線 ") 
        b4_var_2.set("(d) 近"+condi4_1+"年股價的變異係數小於"+condi4_2 ) 
        b5_var_2.set("(e) 過去"+condi5_1+"年ROE 平均大於"+condi5_2+"% ")
        b6_var_2.set("(f) 過去"+condi6+"年自由現金流 平均大於0 ") 
        
        pri0=[]
        if condi1 !="__":   #因為command的因素 可能無法用迴圈表達
            label1=tk.Label(self.rt2,text="(已選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label1.place(relx=0.82,rely=0.18,anchor="center")
            button1d=tk.Button(self.rt2,text="刪除",font=("新細明體",18),relief="groove",command=delete_a)
            button1d.place(relx=0.9,rely=0.18,anchor="center")
            pri0.append("a")
        else:
            label1=tk.Label(self.rt2,text="(未選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label1.place(relx=0.82,rely=0.18,anchor="center") 

        if condi2_1 !="__" and condi2_2 !="__":
            label2=tk.Label(self.rt2,text="(已選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label2.place(relx=0.82,rely=0.27,anchor="center")
            button2d=tk.Button(self.rt2,text="刪除",font=("新細明體",18),relief="groove",command=delete_b)
            button2d.place(relx=0.9,rely=0.27,anchor="center")
            pri0.append("b")
        else:
            label2=tk.Label(self.rt2,text="(未選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label2.place(relx=0.82,rely=0.27,anchor="center") 

        if condi3[0] !="__":
            label3=tk.Label(self.rt2,text="(已選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label3.place(relx=0.82,rely=0.36,anchor="center")
            button3d=tk.Button(self.rt2,text="刪除",font=("新細明體",18),relief="groove",command=delete_c)
            button3d.place(relx=0.9,rely=0.36,anchor="center")
            pri0.append("c")
        else:
            label3=tk.Label(self.rt2,text="(未選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label3.place(relx=0.82,rely=0.36,anchor="center") 

        if condi4_1 !="__" and condi4_2 !="___":
            label4=tk.Label(self.rt2,text="(已選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label4.place(relx=0.82,rely=0.45,anchor="center")
            button4d=tk.Button(self.rt2,text="刪除",font=("新細明體",18),relief="groove",command=delete_d)
            button4d.place(relx=0.9,rely=0.45,anchor="center")
            pri0.append("d")
        else:
            label4=tk.Label(self.rt2,text="(未選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label4.place(relx=0.82,rely=0.45,anchor="center")            

        if condi5_1 !="__" and condi5_2 !="__":
            label5=tk.Label(self.rt2,text="(已選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label5.place(relx=0.82,rely=0.54,anchor="center")
            button5d=tk.Button(self.rt2,text="刪除",font=("新細明體",18),relief="groove",command=delete_e)
            button5d.place(relx=0.9,rely=0.54,anchor="center")
            pri0.append("e")
        else:
            label5=tk.Label(self.rt2,text="(未選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label5.place(relx=0.82,rely=0.54,anchor="center")            

        if condi6 !="__":
            label6=tk.Label(self.rt2,text="(已選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label6.place(relx=0.82,rely=0.63,anchor="center")
            button6d=tk.Button(self.rt2,text="刪除",font=("新細明體",18),relief="groove",command=delete_f)
            button6d.place(relx=0.9,rely=0.63,anchor="center")
            pri0.append("f")
        else:
            label6=tk.Label(self.rt2,text="(未選擇)",font=("新細明體",18),bg="#1E90FF",width=8,height=2)
            label6.place(relx=0.82,rely=0.63,anchor="center")

        if len(pri0) != 0 :
            button0=tk.Button(self.rt2,text="直接開始篩選計算",font=("新細明體",20),width=20,height=2,relief="groove",command=decide_gofirst)
            button0.place(relx=0.5,rely=0.9,anchor="center")
            if len(pri0) > 1 :
                button0a=tk.Button(self.rt2,text="自訂篩選順序",font=("新細明體",18),width=15,height=1,pady=4,relief="groove",command=decide_priority)
                button0a.place(relx=0.85,rely=0.9,anchor="center")
            
        button9=tk.Button(self.rt2,text="回前一頁",font=("新細明體",18),width=15,height=1,pady=6,relief="groove",command=self.back_to_1)
        button9.place(relx=0.15,rely=0.9,anchor="center")
       
#---------------------------------------------------------------------------------------------------------------
        
    def fm2_3a(self):
        def confirm_a():
            if e1_var_3a.get() in [str(i) for i in range(1,11)]:
                global condi1
                condi1=e1_var_3a.get()
                label3=tk.Label(self.rt2,text="輸入成功!",font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
                label3.place(relx=0.6,rely=0.75,anchor="center")
                button1.destroy()
                button2.destroy()
                l0_var_3a.set("(a)今年目前累計的EPS 大於等於 \n過去"+condi1+"年平均同期累計的EPS ")
                self.back_to_2()                           
            else:
                label3=tk.Label(self.rt2,text="輸入錯誤!",font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
                label3.place(relx=0.6,rely=0.75,anchor="center")
        l0_var_3a= tk.StringVar()       
        label0=tk.Label(self.rt2,textvariable=l0_var_3a,font=("新細明體",22),width=30,height=4)
        label0.place(relx=0.5,rely=0.3,anchor="center")
        l0_var_3a.set("(a)今年目前累計的EPS 大於等於 \n過去"+condi1+"年平均同期累計的EPS ")

        label1=tk.Label(self.rt2,text="請輸入[1~10]年: ",font=("新細明體",22),width=16,bg="#20B2AA")
        label1.place(relx=0.39,rely=0.5,anchor="center")
        e1_var_3a=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_3a,font=("新細明體",22))
        entry1.place(relx=0.58,rely=0.5,anchor="center")

        button1=tk.Button(self.rt2,text="確定",font=("新細明體",18),padx=0,pady=0,relief="groove",command=confirm_a) 
        button1.place(relx=0.55,rely=0.65,anchor="center")        
        button2=tk.Button(self.rt2,text="取消",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2) 
        button2.place(relx=0.65,rely=0.65,anchor="center") 


    def fm2_3b(self):
        def confirm_b():
            def label3f(show):                
                label3=tk.Label(self.rt2,text=show ,font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
                label3.place(relx=0.6,rely=0.9,anchor="center")
            e1=e1_var_3b.get()
            e2=e2_var_3b.get()
            if e1 in [str(i) for i in range(1,11)]:
                try:
                    f_e2=float(e2)
                    if f_e2 <= 2 and f_e2 > 0 :
                        label3f("輸入成功")
                        global condi2_1,condi2_2
                        condi2_1=e1
                        condi2_2=e2
                        button1.destroy()
                        button2.destroy()
                        l0_var_3b.set("(b) 近"+condi2_1+"年EPS的變異係數小於"+condi2_2)
                        self.back_to_2()                                             
                    else:
                        label3f("變異係數超過範圍")
                except ValueError:
                    label3f("變異係數輸入錯誤")
            else:
                label3f("年數輸入錯誤")
        
        l0_var_3b= tk.StringVar()       
        label0=tk.Label(self.rt2,textvariable=l0_var_3b,font=("新細明體",22),width=30,height=4)
        label0.place(relx=0.5,rely=0.3,anchor="center")
        l0_var_3b.set("(b) 近"+condi2_1+"年EPS的變異係數小於"+condi2_2)

        label1=tk.Label(self.rt2,text="請輸入[1~10]年: ",font=("新細明體",22),width=13,bg="#20B2AA",anchor="e")
        label1.place(relx=0.39,rely=0.5,anchor="center")
        label2=tk.Label(self.rt2,text=" 變異係數[0~2]: ",font=("新細明體",22),width=13,bg="#20B2AA",anchor="e")
        label2.place(relx=0.39,rely=0.65,anchor="center")

        hint1=tk.Label(self.rt2,text="提示:",font=("新細明體",15),bg="#20B2AA",anchor="e")
        hint1.place(relx=0.7,rely=0.45,anchor="w")
        hint2=tk.Label(self.rt2,text="若想篩選穩定獲利的公司",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint2.place(relx=0.7,rely=0.5,anchor="w")
        hint3=tk.Label(self.rt2,text="可先嘗試設定近[5]年 變異係數小於[0.16]",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint3.place(relx=0.7,rely=0.55,anchor="w")
        hint4=tk.Label(self.rt2,text="但仍需視實際情況再調整變異係數",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint4.place(relx=0.7,rely=0.6,anchor="w")
        hint5=tk.Label(self.rt2,text="變異係數較大者" ,font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint5.place(relx=0.7,rely=0.65,anchor="w")
        hint6=tk.Label(self.rt2,text="可能屬於成長型或者獲利較不穩定的公司" ,font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint6.place(relx=0.7,rely=0.7,anchor="w")

        e1_var_3b=tk.StringVar()
        e2_var_3b=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_3b,font=("新細明體",22))
        entry1.place(relx=0.58,rely=0.5,anchor="center")
        entry2=tk.Entry(self.rt2,textvariable=e2_var_3b,font=("新細明體",22))
        entry2.place(relx=0.58,rely=0.65,anchor="center")

        button1=tk.Button(self.rt2,text="確定",font=("新細明體",18),padx=0,pady=0,relief="groove",command=confirm_b) 
        button1.place(relx=0.55,rely=0.8,anchor="center")        
        button2=tk.Button(self.rt2,text="取消",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2) 
        button2.place(relx=0.65,rely=0.8,anchor="center") 


    def fm2_3c(self):
        def label3f(show):
            label3=tk.Label(self.rt2,text=show,font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
            label3.place(relx=0.6,rely=0.75,anchor="center")        
        def confirm_c():
            global condi3
            if e1_var_3c.get() in [str(i) for i in range(1,6)]:
                if not e1_var_3c.get() in condi3:
                    if condi3[0] == "__" :
                        condi3[0]=e1_var_3c.get()
                    else:
                        condi3.append(e1_var_3c.get())
                    e1_var_3c.set("")
                    l0_var_3c.set("(c) 最新收盤價 小於 "+(",".join(condi3))+" 年均線 ")
                    label3f("輸入成功!")
                    button3=tk.Button(self.rt2,text="完成",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2) 
                    button3.place(relx=0.75,rely=0.65,anchor="center")
                else: label3f("輸入重複!")
            else: label3f("輸入錯誤!")  

        l0_var_3c= tk.StringVar()       
        label0=tk.Label(self.rt2,textvariable=l0_var_3c,font=("新細明體",22),width=30,height=4)
        label0.place(relx=0.5,rely=0.3,anchor="center")
        l0_var_3c.set("(c) 最新收盤價 小於 "+(",".join(condi3))+" 年均線 ")
    
        label1=tk.Label(self.rt2,text="請輸入[1~5]年: ",font=("新細明體",22),width=16,bg="#20B2AA")
        label1.place(relx=0.39,rely=0.5,anchor="center")
        e1_var_3c=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_3c,font=("新細明體",22))
        entry1.place(relx=0.58,rely=0.5,anchor="center")

        button1=tk.Button(self.rt2,text="加入",font=("新細明體",18),padx=0,pady=0,relief="groove",command=confirm_c) 
        button1.place(relx=0.55,rely=0.65,anchor="center")        
        button2=tk.Button(self.rt2,text="取消",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2) 
        button2.place(relx=0.65,rely=0.65,anchor="center") 

                
    def fm2_3d(self):
        def confirm_d():
            def label3f(show):                
                label3=tk.Label(self.rt2,text=show ,font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
                label3.place(relx=0.6,rely=0.9,anchor="center")
            e1=e1_var_3d.get()
            e2=e2_var_3d.get()
            if e1 in [str(i) for i in range(1,6)]:
                try:
                    f_e2=float(e2)
                    if f_e2 <= 2 and f_e2 > 0 :
                        label3f("輸入成功")
                        global condi4_1,condi4_2
                        condi4_1=e1
                        condi4_2=e2
                        button1.destroy()
                        button2.destroy()
                        l0_var_3d.set("(d) 近"+condi4_1+"年股價的變異係數小於"+condi4_2 )
                        self.back_to_2()                                                                    
                    else:
                        label3f("變異係數超過範圍")
                except ValueError:
                    label3f("變異係數輸入錯誤")
            else:
                label3f("年數輸入錯誤")
        
        l0_var_3d= tk.StringVar()       
        label0=tk.Label(self.rt2,textvariable=l0_var_3d,font=("新細明體",22),width=30,height=4)
        label0.place(relx=0.5,rely=0.3,anchor="center")
        l0_var_3d.set("(d) 近"+condi4_1+"年股價的變異係數小於"+condi4_2 )

        label1=tk.Label(self.rt2,text="請輸入[1~5]年: ",font=("新細明體",22),width=13,bg="#20B2AA",anchor="e")
        label1.place(relx=0.39,rely=0.5,anchor="center")
        label2=tk.Label(self.rt2,text=" 變異係數[0~2]: ",font=("新細明體",22),width=13,bg="#20B2AA",anchor="e")
        label2.place(relx=0.39,rely=0.65,anchor="center")

        hint1=tk.Label(self.rt2,text="提示:",font=("新細明體",15),bg="#20B2AA",anchor="e")
        hint1.place(relx=0.7,rely=0.45,anchor="w")
        hint2=tk.Label(self.rt2,text="若想篩選股價穩定的公司",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint2.place(relx=0.7,rely=0.5,anchor="w")
        hint3=tk.Label(self.rt2,text="可先嘗試設定近[5]年 變異係數小於[0.15]",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint3.place(relx=0.7,rely=0.55,anchor="w")
        hint4=tk.Label(self.rt2,text="但仍需視實際情況再調整變異係數",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint4.place(relx=0.7,rely=0.6,anchor="w")
        hint5=tk.Label(self.rt2,text="變異係數較大者",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint5.place(relx=0.7,rely=0.65,anchor="w")
        hint6=tk.Label(self.rt2,text="可能屬於成長型或者股價起伏較大的公司",font=("新細明體",15),bg="#20B2AA",anchor="w")
        hint6.place(relx=0.7,rely=0.7,anchor="w")

        e1_var_3d=tk.StringVar()
        e2_var_3d=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_3d,font=("新細明體",22))
        entry1.place(relx=0.58,rely=0.5,anchor="center")
        entry2=tk.Entry(self.rt2,textvariable=e2_var_3d,font=("新細明體",22))
        entry2.place(relx=0.58,rely=0.65,anchor="center")

        button1=tk.Button(self.rt2,text="確定",font=("新細明體",18),padx=0,pady=0,relief="groove",command=confirm_d) 
        button1.place(relx=0.55,rely=0.8,anchor="center")        
        button2=tk.Button(self.rt2,text="取消",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2) 
        button2.place(relx=0.65,rely=0.8,anchor="center") 

        
    def fm2_3e(self):
        def confirm_e():
            def label3f(show):                
                label3=tk.Label(self.rt2,text=show ,font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
                label3.place(relx=0.6,rely=0.9,anchor="center")
            e1=e1_var_3e.get()
            e2=e2_var_3e.get()
            if e1 in [str(i) for i in range(1,11)]:
                try:
                    f_e2=float(e2)
                    if f_e2 <= 50 and f_e2 > 0 :
                        label3f("輸入成功")
                        global condi5_1,condi5_2
                        condi5_1=e1
                        condi5_2=e2
                        button1.destroy()
                        button2.destroy()
                        l0_var_3e.set("(e) 過去"+condi5_1+"年ROE 平均大於"+condi5_2+"% ")
                        self.back_to_2()                                                                     
                    else:
                        label3f("ROE超過範圍")
                except ValueError:
                    label3f("ROE輸入錯誤")
            else:
                label3f("年數輸入錯誤")
        
        l0_var_3e= tk.StringVar()       
        label0=tk.Label(self.rt2,textvariable=l0_var_3e,font=("新細明體",22),width=30,height=4)
        label0.place(relx=0.5,rely=0.3,anchor="center")
        l0_var_3e.set("(e) 過去"+condi5_1+"年ROE 平均大於"+condi5_2+"% ")

        label1=tk.Label(self.rt2,text="請輸入[1~10]年: ",font=("新細明體",22),width=13,bg="#20B2AA",anchor="e")
        label1.place(relx=0.39,rely=0.5,anchor="center")
        label2=tk.Label(self.rt2,text=" ROE[0~50]%: ",font=("新細明體",22),width=13,bg="#20B2AA",anchor="e")
        label2.place(relx=0.39,rely=0.65,anchor="center")

        hint1=tk.Label(self.rt2,text="提示:",font=("新細明體",18),bg="#20B2AA",anchor="e")
        hint1.place(relx=0.75,rely=0.5,anchor="e")
        hint2=tk.Label(self.rt2,text="均標可設定 [5]年[10]%",font=("新細明體",18),bg="#20B2AA",anchor="w")
        hint2.place(relx=0.75,rely=0.55,anchor="w")
        hint3=tk.Label(self.rt2,text="高標可設定 [5]年[15]%",font=("新細明體",18),bg="#20B2AA",anchor="w")
        hint3.place(relx=0.75,rely=0.61,anchor="w")

        e1_var_3e=tk.StringVar()
        e2_var_3e=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_3e,font=("新細明體",22))
        entry1.place(relx=0.58,rely=0.5,anchor="center")
        entry2=tk.Entry(self.rt2,textvariable=e2_var_3e,font=("新細明體",22))
        entry2.place(relx=0.58,rely=0.65,anchor="center")

        button1=tk.Button(self.rt2,text="確定",font=("新細明體",18),padx=0,pady=0,relief="groove",command=confirm_e) 
        button1.place(relx=0.55,rely=0.8,anchor="center")        
        button2=tk.Button(self.rt2,text="取消",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2) 
        button2.place(relx=0.65,rely=0.8,anchor="center") 

        
    def fm2_3f(self):
        def confirm_f():
            if e1_var_3f.get() in [str(i) for i in range(1,11)]:
                global condi6
                condi6=e1_var_3f.get()
                label3=tk.Label(self.rt2,text="輸入成功!",font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
                label3.place(relx=0.6,rely=0.75,anchor="center")
                button1.destroy()
                button2.destroy()
                l0_var_3f.set("(f) 過去"+condi6+"年自由現金流 平均大於0 ")
                self.back_to_2()                  
            else:
                label3=tk.Label(self.rt2,text="輸入錯誤!",font=("新細明體",16),width=16,fg="red",bg="#20B2AA")
                label3.place(relx=0.6,rely=0.75,anchor="center")
        l0_var_3f= tk.StringVar()       
        label0=tk.Label(self.rt2,textvariable=l0_var_3f,font=("新細明體",22),width=30,height=4)
        label0.place(relx=0.5,rely=0.3,anchor="center")
        l0_var_3f.set("(f) 過去"+condi6+"年自由現金流 平均大於0 ")

        label1=tk.Label(self.rt2,text="請輸入[1~10]年: ",font=("新細明體",22),width=16,bg="#20B2AA")
        label1.place(relx=0.39,rely=0.5,anchor="center")
        e1_var_3f=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_3f,font=("新細明體",22))
        entry1.place(relx=0.58,rely=0.5,anchor="center")

        button1=tk.Button(self.rt2,text="確定",font=("新細明體",18),padx=0,pady=0,relief="groove",command=confirm_f) 
        button1.place(relx=0.55,rely=0.65,anchor="center")        
        button2=tk.Button(self.rt2,text="取消",font=("新細明體",18),padx=0,pady=0,relief="groove",command=self.back_to_2) 
        button2.place(relx=0.65,rely=0.65,anchor="center") 

#---------------------------------------------------------------------------------------------------------------------------

    def fm2_4(self):
        def re_pri(pri):
            global label1_24,label2_24,label3_24,label4_24,label5_24,label6_24
            global prior
            prior=pri
            for i in range(len(pri)):
                if pri[i]=="a":
                    label1_24=tk.Label(self.rt2,text=("(a) 今年累計EPS 大於等於 過去"+condi1+"年平均同期累計EPS "),font=("新細明體",18))
                    label1_24.place(relx=0.5,rely=(0.15 + 0.08*i),anchor="center")               
                elif pri[i]=="b":
                    label2_24=tk.Label(self.rt2,text=("(b) 近"+condi2_1+"年EPS的變異係數小於"+condi2_2),font=("新細明體",18))
                    label2_24.place(relx=0.5,rely=(0.15 + 0.08*i),anchor="center")           
                elif pri[i]=="c":
                    label3_24=tk.Label(self.rt2,text=("(c) 最新收盤價 小於 "+(",".join(condi3))+" 年均線 "),font=("新細明體",18))
                    label3_24.place(relx=0.5,rely=(0.15 + 0.08*i),anchor="center")               
                elif pri[i]=="d":
                    label4_24=tk.Label(self.rt2,text=("(d) 近"+condi4_1+"年股價的變異係數小於"+condi4_2 ),font=("新細明體",18))
                    label4_24.place(relx=0.5,rely=(0.15 + 0.08*i),anchor="center")                               
                elif pri[i]=="e":
                    label5_24=tk.Label(self.rt2,text=("(e) 過去"+condi5_1+"年ROE 平均大於"+condi5_2+"% "),font=("新細明體",18))
                    label5_24.place(relx=0.5,rely=(0.15 + 0.08*i),anchor="center")                              
                elif pri[i]=="f":
                    label6_24=tk.Label(self.rt2,text=("(f) 過去"+condi6+"年自由現金流 平均大於0 "),font=("新細明體",18))
                    label6_24.place(relx=0.5,rely=(0.15 + 0.08*i),anchor="center")
        def delete_label(pri):
            for i in range(len(pri)):
                if pri[i]=="a":
                    label1_24.destroy()
                elif pri[i]=="b":
                    label2_24.destroy()   
                elif pri[i]=="c":
                    label3_24.destroy()               
                elif pri[i]=="d":
                    label4_24.destroy()                              
                elif pri[i]=="e":
                    label5_24.destroy()                              
                elif pri[i]=="f":
                    label6_24.destroy()                    
        def check_pri2():
            global cango
            str1=e1_var_4.get()
            str2=str1.replace(" ", "")
            pri2=str2.split(",")
#            print(pri2)
#            print(pri1)
            times=0
            for letter in pri2:
                if letter in pri1:
                    if pri2.count(letter)==1:
                        times+=1
                    else:
                        label8=tk.Label(self.rt2,text="輸入條件重複",font=("新細明體",18),bg="#20B2AA")
                        label8.place(relx=0.8,rely=0.68,anchor="w")
                        break
                else:
                    label8=tk.Label(self.rt2,text="輸入條件失敗",font=("新細明體",18),bg="#20B2AA")
                    label8.place(relx=0.8,rely=0.68,anchor="w")
                    break                
            if times==len(pri1):
                if len(pri2)==len(pri1):
                    label8=tk.Label(self.rt2,text="輸入條件成功",font=("新細明體",18),bg="#20B2AA")
                    label8.place(relx=0.8,rely=0.68,anchor="w")
                    delete_label(pri1)
                    re_pri(pri2)
                    cango=True
                else: cango=False
            else: cango=False                    
        def decide_gofinal():
            global exe
            if cango==True:
                exe=1
                win.destroy()
        
        condi_test=[condi1,condi2_1,condi3[0],condi4_1,condi5_1,condi6]
        print(condi_test)
        words=["a","b","c","d","e","f"]
        pri1=[]
        for i in range(6):
            if condi_test[i] != "__" :
                pri1.append(words[i])      
        label0=tk.Label(self.rt2,text="目前篩選順序:",font=("新細明體",22),bg="#20B2AA",width=16)
        label0.place(relx=0.5,rely=0.06,anchor="center")  
        hint1=tk.Label(self.rt2,text="提示:",font=("新細明體",18),bg="#20B2AA",anchor="w")
        hint2=tk.Label(self.rt2,text="此排序只影響篩選過程",font=("新細明體",18),bg="#20B2AA",anchor="w")
        hint3=tk.Label(self.rt2,text="不影響最終篩選結果",font=("新細明體",18),bg="#20B2AA",anchor="w")
        hint1.place(relx=0.77,rely=0.47,anchor="e")  
        hint2.place(relx=0.77,rely=0.53,anchor="w")
        hint3.place(relx=0.77,rely=0.59,anchor="w")        
        re_pri(pri1)

        label7=tk.Label(self.rt2,text="自行輸入篩選順序: \n (例如: e,b,a,c)",font=("新細明體",18),bg="#20B2AA")
        label7.place(relx=0.5,rely=0.7,anchor="e")
        e1_var_4=tk.StringVar()
        entry1=tk.Entry(self.rt2,textvariable=e1_var_4,font=("新細明體",18))
        entry1.place(relx=0.5,rely=0.68,anchor="w")
        button1=tk.Button(self.rt2,text="確定",font=("新細明體",18),padx=0,pady=0,relief="groove",command=check_pri2) 
        button1.place(relx=0.75,rely=0.68,anchor="center")
        button9=tk.Button(self.rt2,text="回前一頁",font=("新細明體",18),width=15,height=1,pady=6,relief="groove",command=self.back_to_2)
        button9.place(relx=0.15,rely=0.9,anchor="center")
        global cango
        cango=True
        button0=tk.Button(self.rt2,text="開始篩選計算",font=("新細明體",20),width=20,height=2,relief="groove",command=decide_gofinal)
        button0.place(relx=0.5,rely=0.9,anchor="center")        


    def fm2_e(self,cond0,list_output):
        def Restart():
            global exe
            exe=1
            win.destroy()
        global exe
        exe=0
        if cond0:        
            file_path="json/other/stock_name.json"
            if os.path.exists(file_path):
                with open(file_path,'r') as fp1:
                    Stock_name=json.load(fp1)            
            
            label0=tk.Label(self.rt2,text="最終符合條件的股票清單:",font=("新細明體",22))
            label0.place(relx=0.5,rely=0.07,anchor="center")           
            text1=tk.Text(self.rt2,font=("新細明體",18),width=18,height=18)
            text2=tk.Text(self.rt2,font=("新細明體",18),width=18,height=18)
            text3=tk.Text(self.rt2,font=("新細明體",18),width=18,height=18)
            text4=tk.Text(self.rt2,font=("新細明體",18),width=18,height=18)
            text5=tk.Text(self.rt2,font=("新細明體",18),width=18,height=18)
            text6=tk.Text(self.rt2,font=("新細明體",18),width=18,height=18)
            length=len(list_output)            
            for i in [i for i in range(length) if i%6==0]:
                si=str(list_output[i])
                if si in Stock_name: text1.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
                else               : text1.insert(tk.INSERT," "+si+"\n")
            for i in [i for i in range(length) if i%6==1]:
                si=str(list_output[i])
                if si in Stock_name: text2.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
                else               : text2.insert(tk.INSERT," "+si+"\n")
            for i in [i for i in range(length) if i%6==2]:
                si=str(list_output[i])
                if si in Stock_name: text3.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
                else               : text3.insert(tk.INSERT," "+si+"\n")
            for i in [i for i in range(length) if i%6==3]:
                si=str(list_output[i])
                if si in Stock_name: text4.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
                else               : text4.insert(tk.INSERT," "+si+"\n")
            for i in [i for i in range(length) if i%6==4]:
                si=str(list_output[i])
                if si in Stock_name: text5.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
                else               : text5.insert(tk.INSERT," "+si+"\n")
            for i in [i for i in range(length) if i%6==5]:
                si=str(list_output[i])
                if si in Stock_name: text6.insert(tk.INSERT," "+si+" "+Stock_name[si]+"\n")
                else               : text6.insert(tk.INSERT," "+si+"\n")
            text1.place(relx=0.05,rely=0.13,anchor="nw")
            text2.place(relx=0.20,rely=0.13,anchor="nw")
            text3.place(relx=0.35,rely=0.13,anchor="nw")
            text4.place(relx=0.50,rely=0.13,anchor="nw")
            text5.place(relx=0.65,rely=0.13,anchor="nw")
            text6.place(relx=0.80,rely=0.13,anchor="nw")
            text1.config(state=tk.DISABLED)
            text2.config(state=tk.DISABLED)
            text3.config(state=tk.DISABLED)
            text4.config(state=tk.DISABLED)
            text5.config(state=tk.DISABLED)
            text6.config(state=tk.DISABLED)
            fp=open("Result.txt","a",encoding="utf8")
            fp.write("\n\n最終符合條件的股票清單:\n\n")
            for out in list_output:
                s0=str(out)
                if s0 in Stock_name: fp.write("("+s0+") "+Stock_name[s0]+"\n")
                else               : fp.write("("+s0+") \n")
        else:
            label0=tk.Label(self.rt2,text="  已更新所有內建資料庫數據!  ",font=("新細明體",22),height=2)
            label0.place(relx=0.5,rely=0.5,anchor="center")           
            fp=open("Result.txt","a",encoding="utf8")
            fp.write("\n\n已更新所有內建資料庫數據! \n\n")
        
        button0=tk.Button(self.rt2,text="重新回到主目錄",font=("新細明體",20),bg="#DDDDDD",width=20,height=1,relief="groove",command=Restart)
        button0.place(relx=0.5,rely=0.93,anchor="center")
#----------------------------------------------------------------------------
        
class WIN1_FM3:
    def __init__(self,win,wd,ht,color):
        self.rt3=tk.Frame(win,width=wd,height=ht,bg=color)
        self.rt3.pack(side="bottom")
        label_3=tk.Label(self.rt3,text="v2.0",font=("新細明體",20))
        label_3.place(relx=0.5,rely=0.5,anchor="center")
        self.rt3a=tk.Frame(win,width=wd,height=3,bg="white")
        self.rt3a.pack(side="bottom")
              
#----------------------------------------------------------------------------

def Declare_global():
    global condi0,condi1,condi2_1,condi2_2,condi3,condi4_1,condi4_2,condi5_1,condi5_2,condi6,win,listno,prior,exe
    condi1=condi2_1=condi2_2=condi4_1=condi4_2=condi5_1=condi5_2=condi6="__"
    condi0=True
    condi3=["__"]
    listno=["2412"]
    prior=[]
    exe=0
    win=tk.Tk()
    win.title("Main")
    win.geometry("1280x720")


def Condi_refresh():    
    Condition=[condi0]
    if condi1   !="__": Condition.append(int(condi1))
    else               : Condition.append(1)
    if condi2_1 !="__": Condition.append([int(condi2_1),float(condi2_2)])
    else               : Condition.append([1,1.0])    
    if condi3[0]!="__":
        int_condi3=[int(i) for i in condi3]
        Condition.append(int_condi3)
    else               : Condition.append([1])
    if condi4_1 !="__": Condition.append([int(condi4_1),float(condi4_2)])
    else               : Condition.append([1,1.0])
    if condi5_1 !="__": Condition.append([int(condi5_1),float(condi5_2)])
    else               : Condition.append([1,1.0])
    if condi6   !="__": Condition.append(int(condi6))
    else               : Condition.append(1)    
    return Condition


def Write_result1(List_NO,Condition,priority,exe):
    if exe==1:
        fp = open("Result.txt","w",encoding="utf8")
        fp.write("******************************選股程式******************************\n")
        if Condition[0]==True:
            fp.write("\n最初選股清單:\n")    
            fp.write(str(List_NO)+"\n")
            print(priority)
            Con=Condition
            times=1
            for I in priority:       
                if I=="a" :
                    fp.write("\n選股條件順位"+str(times)+" : ")
                    fp.write("今年目前累計的EPS 大於等於 過去"+str(Con[1])+"年平均同期累計的EPS")
                elif I=="b" :
                    fp.write("\n選股條件順位"+str(times)+" : ")
                    fp.write("近"+str(Con[2][0])+"年EPS的變異係數小於"+str(Con[2][1]) )
                elif I=="c" :
                    fp.write("\n選股條件順位"+str(times)+" : ")
                    for yr in Con[3]: 
                        fp.write("最新收盤價小於"+str(yr)+"年均線  ")
                elif I=="d" :
                    fp.write("\n選股條件順位"+str(times)+" : ")
                    fp.write("近"+str(Con[4][0])+"年股價的變異係數小於"+str(Con[4][1]))
                elif I=="e" :
                    fp.write("\n選股條件順位"+str(times)+" : ")
                    fp.write("過去"+str(Con[5][0])+"年ROE 平均大於"+str(Con[5][1])+"%")
                elif I=="f" :
                    fp.write("\n選股條件順位"+str(times)+" : ")
                    fp.write("過去"+str(Con[6])+"年自由現金流 平均大於0 ")
                times+=1    
        fp.close() 

#------------------------------------------------------------------------------

def Main_gui():
   
    Declare_global()
    frame1=WIN1_FM1(win,1280,52,"#444444") #1E90FF  #20B2AA
    frame2_1=WIN1_FM2(win,1280,610,"#1E90FF")                
    frame3=WIN1_FM3(win,1280,52,"#444444")
    frame2_1.fm2_1()
    win.mainloop()
    
    List_NO=listno
    Condition=Condi_refresh()
    priority=prior    
    Write_result1(List_NO,Condition,priority,exe)
    
    return List_NO,Condition,priority,exe

#------------------------------------------------------------------------------

def End_gui(cond0,list_output):
    global win
    win=tk.Tk()
    win.title("Main")
    win.geometry("1280x720")
    frame1=WIN1_FM1(win,1280,52,"#444444")
    frame2_e=WIN1_FM2(win,1280,610,"#1E90FF") 
    frame3=WIN1_FM3(win,1280,52,"#444444")                      
    frame2_e.fm2_e(cond0,list_output)                                   
    win.mainloop()
    
    return exe
    
#------------------------------------------------------------------------------

if __name__=="__main__":

    List_NO,Condition,priority,exe=Main_gui()
    cond0=True
    list_output=[1233,1507,1604,2382,2834,2880,2881,2882,2884,2885,2886,2890,2891,2892,2912,5312,5434,5880,6136,6184,6202,8083,8406,9924,1233,1507,1604,2382,2834,2880,2881,2882,2884,2885,2886,2890,2891,2892,2912,5312,5434,5880,6136,6184,6202,8083,8406,9924]
#    exe=End_gui(cond0,list_output)

    





