from tkinter import *
import tkinter.ttk as ttk
import tkinter as tkinter

window =  tkinter.Tk()
window.title("System")
window.minsize(width=1000, height=1000)
window.resizable(width=False, height=False)
chefdata=list()

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
            if i==0:
                table1.configure(bg="red")
            elif i==1:
                table2.configure(bg="red")
            elif i==2:
                table3.configure(bg="red")
            else:
                table4.configure(bg="red")
            order.insert(0,firstbox.get())   
            order.insert(0, secondbox.get())   
            order.insert(0, thirdbox.get())
            order.insert(0, str(i+1)+" : "+finalbox.get())
            order.grid(column=i, row=6)
        
            
        yes = tkinter.Button(waiter_win, text='確定', command=show)
        yes.grid(column=i, row=5)
        
    def go_order():
        data = list()
        data =order.get(0,last=order.size())
        chefdata.extend(data)
    go = tkinter.Button(waiter_win, text='出單', command=go_order)
    go.grid(column=5, row=7)

    table1 = tkinter.Button(waiter_win,text="table1", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(0))
    table1.grid(column=0, row=0)
    table2 = tkinter.Button(waiter_win,text="table2", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(1))
    table2.grid(column=1, row=0)
    table3 = tkinter.Button(waiter_win,text="table3", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(2))
    table3.grid(column=2, row=0)
    table4 = tkinter.Button(waiter_win,text="table4", font=("Arial", 14, "bold"), padx=5, pady=5, bg="white", fg="light green", command=table_clicked(3))
    table4.grid(column=3, row=0)

    

def chef_button_clicked():
    chef_win = tkinter.Toplevel()
    chef_win.title("chef")
    chef_win.minsize(width=500, height=500)
    cheforder = tkinter.Listbox(chef_win)
    for i in range(len(chefdata)):
        cheforder.insert(tkinter.END, chefdata[i])
    cheforder.grid(column=0, row=0)
    
    def out_order_clicked():
        out = cheforder.get(tkinter.END)
        outed.insert(0,out)
        outed.grid(column=1, row=0)
        cheforder.delete(tkinter.END)
        
    out_order = tkinter.Button(chef_win, text='完成', command=out_order_clicked)
    out_order.grid(column=0, row=1)
    outed = tkinter.Listbox(chef_win)

waiter_button = tkinter.Button(text="waiter", font=("Arial", 14, "bold"), padx=30, pady=30, bg="white", fg="black", command=waiter_button_clicked)
waiter_button.place(relx=0.1, rely=0.1)

chef_button = tkinter.Button(text="chef", font=("Arial", 14, "bold"), padx=30, pady=30, bg="white", fg="black", command=chef_button_clicked)
chef_button.place(relx=0.5, rely=0.1)

window.mainloop()


