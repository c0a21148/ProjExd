import tkinter as tk

def key_down(event):
    global key
    key = event.keysym
    print(f"{key}キーがおされました")
    

root = tk.Tk()
root.title("迷えるこうかとん")
canvas = tk.Canvas(root,width=1500,height=900,bg="black")
canvas.pack()
tori = tk.PhotoImage(file="fig/9.png")
cx,cy=300,400
canvas.create_image(cx,cy,image=tori,tag="tori")
key = ""
root.bind("<KeyPress>",key_down)
root.mainloop()