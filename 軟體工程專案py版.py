import tkinter.ttk as ttk
import tkinter as tkinter
import datetime

window =  tkinter.Tk()
window.title("System")
window.minsize(width=1000, height=1000)
window.resizable(width=False, height=False)
chefdata=list()
pricedata = list()
orderdata = list()
prepare_time = list()
stop_time = list()
color = list([False,False,False,False])
t1_price = list()
t2_price = list()
t3_price = list()
t4_price = list()

def waiter_button_clicked():
    waiter_win = tkinter.Toplevel()
    waiter_win.title("waiter")
    waiter_win.minsize(width=500, height=500)
    order = tkinter.Listbox(waiter_win)

    def table_clicked(i):
        firstbox = ttk.Combobox(waiter_win, values=['酥炸花枝','香煎干貝','煙燻鮭魚'])
        firstbox.grid(column=i, row=1)
        
        secondbox = ttk.Combobox(waiter_win, values=['蛋花湯','紫菜湯','洋蔥湯'])
        secondbox.grid(column=i, row=2)
           
        thirdbox = ttk.Combobox(waiter_win, values=['雞排','豬排','牛排'])
        thirdbox.grid(column=i, row=3)
        
        finalbox = ttk.Combobox(waiter_win, values=['蛋糕','布丁','冰淇淋'])
        finalbox.grid(column=i, row=4)
        
        def show():
            meal = thirdbox.get()
            if meal == "雞排":
                price = 400
            elif meal == "豬排":
                price = 500
            else:
                price = 600
            
            pricedata.append(price)
            if i==0:
                table1.configure(bg="red")
                color[0] = True
                t1_price.append(price)
            elif i==1:
                table2.configure(bg="red")
                color[1] = True
                t2_price.append(price)
            elif i==2:
                table3.configure(bg="red")
                color[2] = True
                t3_price.append(price)
            elif i==3:
                table4.configure(bg="red")
                color[3] = True
                t4_price.append(price)
                
            orderdata.append(firstbox.get())
            orderdata.append(secondbox.get())
            orderdata.append(thirdbox.get())
            orderdata.append(finalbox.get())
            
            order.insert(0,firstbox.get())   
            order.insert(0, secondbox.get())   
            order.insert(0, thirdbox.get())
            order.insert(0, str(i+1)+" : "+finalbox.get())
            order.grid(column=i, row=6)
        def checkout_clicked():                          
            global eat_time
            eat_time = datetime.datetime.now()
            price_sum = 0
            if t1_price!=[]:
                for j in range(0,len(t1_price)):
                    price_sum = price_sum + t1_price[j]
                t1_price.clear()
            elif t2_price!=[]:
                 for j in range(0,len(t2_price)):
                     price_sum = price_sum + t2_price[j]
                 t2_price.clear()
            elif t3_price!=[]:
                 for j in range(0,len(t3_price)):
                     price_sum = price_sum + t3_price[j]
                 t3_price.clear()
            elif t4_price!=[]:
                for j in range(0,len(t4_price)):
                    price_sum = price_sum + t4_price[j]
                t4_price.clear()
            pricelabel = tkinter.Label(waiter_win,text=price_sum,font=('Arial',14,'bold'))
            pricelabel.grid(column=5, row=9)
            
        
        yes = tkinter.Button(waiter_win, text='確定', command=show)
        yes.grid(column=i, row=5)
        checkout = tkinter.Button(waiter_win, text='結帳', command=checkout_clicked)
        checkout.grid(column=5, row=8)
    def go_order():
        global start_time
        start_time = datetime.datetime.now()
        data = list()
        data =order.get(0,last=order.size())
        chefdata.extend(data)
        order.delete(0,tkinter.END)

    go = tkinter.Button(waiter_win, text='出單', command=go_order)
    go.grid(column=5, row=7)
    
    global table1,table2,table3,table4
    table1 = tkinter.Button(waiter_win,text="table1", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(0))
    table1.grid(column=0, row=0)
    table2 = tkinter.Button(waiter_win,text="table2", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(1))
    table2.grid(column=1, row=0)
    table3 = tkinter.Button(waiter_win,text="table3", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(2))
    table3.grid_forget()
    table4 = tkinter.Button(waiter_win,text="table4", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(3))
    table4.grid_forget()
   
def chef_button_clicked():
    chef_win = tkinter.Toplevel()
    chef_win.title("chef")
    chef_win.minsize(width=500, height=500)
    cheforder = tkinter.Listbox(chef_win)
    
    for i in range(len(chefdata)):
        cheforder.insert(tkinter.END, chefdata[i])
    cheforder.grid(column=0, row=0)
    
    def out_order_clicked():
        global end_time,time
        end_time =  datetime.datetime.now()
        
        out = cheforder.get(tkinter.END)
        outed.insert(0,out)
        outed.grid(column=1, row=0)
        cheforder.delete(tkinter.END)
        temp = end_time - start_time
        time = temp.seconds
        prepare_time.append(time)
       
    out_order = tkinter.Button(chef_win, text='完成', command=out_order_clicked)
    out_order.grid(column=0, row=1)
    outed = tkinter.Listbox(chef_win)
    
def manager_button_clicked():
   manager_win = tkinter.Toplevel()
   manager_win.title("manager")
   manager_win.minsize(width=500, height=500)
   def massage_button_clicked():
       global income
       income = list()
       income.append(pricedata.count(400))
       income.append(pricedata.count(500))
       income.append(pricedata.count(600))
       print("雞排收入:" + str(400*income[0]))
       print("豬排收入:"  + str(500*income[1]))
       print("牛排收入:" + str(600*income[2]))
       pre1 = (400*income[0]/(400*income[0]+500*income[1]+600*income[2]))*100
       pre2 = (500*income[1]/(400*income[0]+500*income[1]+600*income[2]))*100
       pre3 = (600*income[2]/(400*income[0]+500*income[1]+600*income[2]))*100
       print("雞排收入百分比:" + str(pre1) + "%")
       print("豬排收入百分比:" + str(pre2) + "%")
       print("牛排收入百分比:" + str(pre3) + "%")
       sum_price = 400*income[0]+500*income[1]+600*income[2]
       print("總收入:" + str(sum_price))
    
       hot = list()   
       def compare_dish(one,two,three):   
           compare = list()
           dish = list()
           compare.append(orderdata.count(one))
           compare.append(orderdata.count(two))
           compare.append(orderdata.count(three))
           hotdish = max(compare)
           
           dish.append(compare.index(hotdish)+1)
           for i in range(0,len(dish)):
               if dish[i] == 1:
                   hot.append(one)
               elif dish[i] == 2:
                   hot.append(two)
               else:
                   hot.append(three)
           compare.clear()
       
       compare_dish('酥炸花枝','香煎干貝','煙燻鮭魚')
       compare_dish('蛋花湯','紫菜湯','洋蔥湯')
       compare_dish('雞排','豬排','牛排')
       compare_dish('蛋糕','布丁','冰淇淋')
       print("熱門菜品:",hot)
       
       temp = 0
       for i in range (0,len(prepare_time)):
           temp = temp + prepare_time[i]
       temp = temp/len(prepare_time)
       print("平均準備時間:" + str(temp))
       temp = 0
       for i in range(0,len(stop_time)):
           temp = temp +  stop_time[i]
       temp = temp/len(stop_time)
       print("顧客平均停留時間:" + str(temp))
       print("---------------")
   
   def file_button_clicked():
       staff_name = ['王一','陳二','張三','李四','黃五']
       staff_position = ['服務生','廚師','經理','前台','雜工']
       staff_work = ['負責1.2.3.4桌點單','負責做菜','負責清潔','負責帶位','管理餐廳']
       for i in range(0,len(staff_name)):
           print(staff_name[i],staff_position[i],staff_work[i])
       print("---------------")

       def add_button_clicked():
           staff_name.append(func.get('1.0','1.end'))
           staff_position.append(func.get('2.0','2.end'))
           staff_work.append(func.get('3.0','3.end'))
           for i in range(0,len(staff_name)):
               print(staff_name[i],staff_position[i],staff_work[i])
               
       def revise_button_clicked():
           def revise(i):
               staff_position[i] = func.get('2.0','2.end')
               staff_work[i] = func.get('3.0','3.end')
               
           for j in range(0,len(staff_name)):
               if func.get('1.0','1.end') == staff_name[j]:
                   revise(j)
           for i in range(0,len(staff_name)):
               print(staff_name[i],staff_position[i],staff_work[i])
       def delete_button_clicked():
           staff_position.pop(staff_name.index(func.get('1.0','1.end')))
           staff_work.pop(staff_name.index(func.get('1.0','1.end')))
           staff_name.pop(staff_name.index(func.get('1.0','1.end')))
           for i in range(0,len(staff_name)):
               print(staff_name[i],staff_position[i],staff_work[i])
           
       func = tkinter.Text(manager_win,width = 20,height= 3)
       func.place(relx=0.1, rely=0.4)
       add = tkinter.Button(manager_win,text="新增", font=("Arial", 10), bg="white", fg="black", command=add_button_clicked)
       add.place(relx=0.1, rely=0.5)
       add = tkinter.Button(manager_win,text="修改", font=("Arial", 10), bg="white", fg="black", command=revise_button_clicked)
       add.place(relx=0.2, rely=0.5)
       delete = tkinter.Button(manager_win,text="刪除", font=("Arial", 10), bg="white", fg="black", command=delete_button_clicked)
       delete.place(relx=0.3, rely=0.5)
   def change_button_clicked():
       global count
       count = 0
       def add_table_clicked():   
           global count
           count+=1
           if count == 1:
               table3.grid(column=2,row=0)
           else:
               table4.grid(column=3,row=0)
       def hide_table_clicked():
           global count
           count-=1
           if count == 1:
               table4.grid_forget()
           else:
               table3.grid_forget()
            
       add_table = tkinter.Button(manager_win,text="增加桌子", font=("Arial", 14, "bold"), bg="white", fg="black", command=add_table_clicked)
       add_table.place(relx=0.7, rely=0.3)
       hide_table = tkinter.Button(manager_win,text="刪除桌子", font=("Arial", 14, "bold"), bg="white", fg="black", command=hide_table_clicked)
       hide_table.place(relx=0.7, rely=0.5)
       
   def reserve_button_clicked():
       reserve = ['花枝','干貝','鮭魚','蛋','紫菜','洋蔥','雞排','豬排','牛排','蜂蜜蛋糕','統一布丁','杜老爺冰淇淋']
       menu = ['酥炸花枝','香煎干貝','煙燻鮭魚','蛋花湯','紫菜湯','洋蔥湯','雞排','豬排','牛排','蛋糕','布丁','冰淇淋']
       quantity=list()
       for i in range(0,len(reserve)):
           quantity.append(orderdata.count(menu[i]))
       for i in range(0,len(reserve)):
           print(reserve[i],quantity[i])
       print("---------")

   file_button = tkinter.Button(manager_win,text="staff \n file", font=("Arial", 14, "bold"), bg="white", fg="black", command=file_button_clicked)
   file_button.place(relx=0.1, rely=0.1)
   massage_button = tkinter.Button(manager_win,text="restaurant \n information", font=("Arial", 14, "bold"), bg="white", fg="black", command=massage_button_clicked)
   massage_button.place(relx=0.3, rely=0.1)
   change_button = tkinter.Button(manager_win,text="change \n table", font=("Arial", 14, "bold"), bg="white", fg="black", command=change_button_clicked)
   change_button.place(relx=0.6, rely=0.1)
   reserve_button = tkinter.Button(manager_win,text="reserve", font=("Arial", 14, "bold"), bg="white", fg="black", command=reserve_button_clicked)
   reserve_button.place(relx=0.8, rely=0.1)
   
def reception_button_clicked(): 
    reception_win = tkinter.Toplevel()
    reception_win.title("reception")
    reception_win.minsize(width=500, height=500)
    
    global r_table1,r_table2,r_table3,r_table4
    r_table1 = tkinter.Button(reception_win,text="table1", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    r_table1.grid(column=0, row=0)
    r_table2 = tkinter.Button(reception_win,text="table2", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    r_table2.grid(column=1, row=0)
    r_table3 = tkinter.Button(reception_win,text="table3", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    r_table3.grid(column=2, row=0)
    r_table4 = tkinter.Button(reception_win,text="table4", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    r_table4.grid(column=3, row=0)
    
    if color[0]== True :  
        r_table1.configure(bg="red")
    if color[1]== True:
        r_table2.configure(bg="red")
    if color[2]== True:
        r_table3.configure(bg="red")
    if color[3]== True:
        r_table4.configure(bg="red")
    
def busboy_button_clicked():  
    busboy_win = tkinter.Toplevel()
    busboy_win.title("busboy")
    busboy_win.minsize(width=500, height=500)
   
    b_table1 = tkinter.Button(busboy_win,text="table1", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    b_table1.grid(column=0, row=0)
    b_table2 = tkinter.Button(busboy_win,text="table2", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    b_table2.grid(column=1, row=0)
    b_table3 = tkinter.Button(busboy_win,text="table3", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    b_table3.grid(column=2, row=0)
    b_table4 = tkinter.Button(busboy_win,text="table4", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green")
    b_table4.grid(column=3, row=0)
    
    def clear_clicked():
        if color[0] ==True:
            table1.configure(bg = "white")
            r_table1.configure(bg = "white")
            b_table1.configure(bg = "white")
        if color[1] ==True:
            table2.configure(bg = "white")
            r_table2.configure(bg = "white")
            b_table2.configure(bg = "white")
        if color[2] ==True:
            table3.configure(bg = "white")
            r_table3.configure(bg = "white")
            b_table3.configure(bg = "white")
        if color[3] ==True:
            table4.configure(bg = "white")
            r_table4.configure(bg = "white")
            b_table4.configure(bg = "white")
            
    clear = tkinter.Button(busboy_win,text="clear", font=("Arial", 10, "bold"), padx=5, pady=5, bg="white", fg="black",command=clear_clicked)
    clear.grid(column=4, row=0)
    temp = eat_time - start_time
    global eat
    eat = temp.seconds
    stop_time.append(eat)
     
    if color[0]== True :     
        b_table1.configure(bg="red")
        if eat == 20 or eat>20 :
            b_table1.configure(bg="green")
            r_table1.configure(bg="green")
            table1.configure(bg = "green")
    if color[1]== True:
        b_table2.configure(bg="red")
        if eat == 20 or eat>20:
            b_table2.configure(bg="green")
            r_table2.configure(bg="green")
            table2.configure(bg = "green")
    if color[2]== True:
        b_table3.configure(bg="red")
        if eat == 20 or eat>20:
            b_table3.configure(bg="green")
            b_table3.configure(bg="green")
            table3.configure(bg = "green")
    if color[3]== True:
        b_table4.configure(bg="red")
        if eat == 20 or eat>20:
            b_table4.configure(bg="green")
            r_table4.configure(bg="green")
            table4.configure(bg= "green")
               
waiter_button = tkinter.Button(text="waiter", font=("Arial", 14, "bold"), padx=30, pady=30, bg="white", fg="black", command=waiter_button_clicked)
waiter_button.place(relx=0.1, rely=0.1)

chef_button = tkinter.Button(text="chef", font=("Arial", 14, "bold"), padx=30, pady=30, bg="white", fg="black", command=chef_button_clicked)
chef_button.place(relx=0.4, rely=0.1)

manager_button = tkinter.Button(text="manager", font=("Arial", 14, "bold"), padx=30, pady=30, bg="white", fg="black", command=manager_button_clicked)
manager_button.place(relx=0.7, rely=0.1)

reception_button = tkinter.Button(text="reception", font=("Arial", 14, "bold"), padx=30, pady=30, bg="white", fg="black", command=reception_button_clicked)
reception_button.place(relx=0.25, rely=0.3)

busboy_button =  tkinter.Button(text="busboy", font=("Arial", 14, "bold"), padx=30, pady=30, bg="white", fg="black", command=busboy_button_clicked)
busboy_button.place(relx=0.55, rely=0.3)

window.mainloop()
