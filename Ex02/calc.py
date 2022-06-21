import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x600")
r,t=1,0

def button_click(event):
    button=event.widget
    txt = button["text"]
    #tkm.showinfo("",f"{txt}が押されました。")
    entry.insert(tk.END,txt)

for num in range(9,-1,-1):
    button = tk.Button(root,
                       
                       text=f"{num}",
                       command=button_click,
                       font=("Times New Roman",30),
                       width=4,
                       height=2, 
                       )

    button.bind("<1>",button_click)
    button.grid(row=r,column=t)
    t += 1
    if (num-1)%3 == 0:
        r+=1
        t=0

entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,columnspan=3)

root.mainloop()