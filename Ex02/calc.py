import tkinter as tk
import tkinter.messagebox as tkm
x=0
b=4
r=1
c=0
def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num, f"[{num}]ボタンが押されました")
    #entry.insert(tk.END,f"{num}")

    if num == "=":
        a = entry.get()
        ans = eval(a)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    else:
        entry.insert(tk.END,f"{num}")

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x600")
    root.title("計算機")
    for i,num in enumerate([i for i in range(9,-1,-1)] + ["+"] + ["-"] + ["*"] + ["/"] +["="]):
        button = tk.Button(root, text = f"{num}",bg="lavender" ,width=4, height=1,command=button_click,font=("Times New Roman", 30))
        button.grid(row=r,column=c)
        button.bind("<1>",button_click)
        c+=1
        if (i + 1) % 3 == 0:
            r += 1
            c = 0


    entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman", 40))
    entry.grid(row=0,columnspan=3)
    root.mainloop() 