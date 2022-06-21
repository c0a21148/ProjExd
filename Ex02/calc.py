import tkinter as tk
import tkinter.messagebox as tkm
p=4　　
c=0 # %,**,!を任意の位置に置くための変数
d=0 # %,**,!を任意の位置に置くための変数
r=4 # 1~9,四則演算を任意の位置に置くための変数　
c=0 # 1~9,四則演算を任意の位置に置くための変数
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

    elif num =="%":
        a = entry.get()
        y = eval(a)/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,y)
    for i,num in enumerate([i for i in range(9,0,-1)] + ["+"] + ["-"] + ["*"] + ["/"] +["="]):#９から０と四則演算、＝を順番に置く
    elif num =="**":
        a = entry.get()
        y = eval(a)/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,y)

    elif num =="!":
        a = entry.get()
        for i in range(a):
            y *= eval(a)
        entry.delete(0,tk.END)
        entry.insert(tk.END,y)

    else:
        entry.insert(tk.END,f"{num}")

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x600")
    root.title("計算機")
    for i,num in enumerate([i for i in range(9,0,-1)] + ["+"] + ["-"] + ["*"] + ["/"] +["="]):
        button = tk.Button(root, text = f"{num}",bg="lavender" ,width=3, height=1,command=button_click,font=("Times New Roman", 30))
        button.grid(row=r,column=c)
        button.bind("<1>",button_click)
        c+=1
        if (i + 1) % 3 == 0:
            r += 1
            c = 0

    for i,num in enumerate([i for i in ["%","**","!"]]): #deleteと()、割り算、％、√の表示
        button = tk.Button(root, text = f"{num}", width = 3, height = 1, font=("Times New Roman", 30))
        button.grid(row = b, column = d)
        d += 1
        button.bind("<1>", button_click)
        if (i+1)%4 == 0:
            b += 1
            d = 0

    for i,num in enumerate([i for i in ["+","-","*","/"]]):
        if i == 4:
            button = tk.Button(root, text = f"{num}", width = 3, height = 1,bg="blue", font=("Times New Roman", 30))
        else:
            button = tk.Button(root, text = f"{num}", width = 3, height = 1, font=("Times New Roman", 30))
        button.grid(row = p, column = 3)
        p += 1
        button.bind("<1>", button_click)


    entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman", 40))
    entry.grid(row=0,columnspan=5)
    root.mainloop() 