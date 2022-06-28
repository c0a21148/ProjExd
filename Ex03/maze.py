import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}キーがおされました")

def key_up(event):
    global key
    key = ""
    
def main_proc():
    global cx,cy
    global mx,my
    #delta = {
    #    "":[0,0],
    #    "Up":[0,-20],
    #    "Down":[0,+20],
    #    "Left":[-20,0],
    #    "Right":[+20,0]
    #}
    
    if key == "Up" and maze_bg[my-1][mx] == 0: my -=1
    if key == "Down" and maze_bg[my+1][mx] == 0: my +=1
    if key == "Left" and maze_bg[my][mx-1] == 0: mx -=1
    if key == "Right" and maze_bg[my][mx+1] == 0: mx +=1

    cx,cy = mx*100+50,my*100+50
    canvas.coords("tori",cx,cy)
    root.after(50,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,maze_bg)
    tori = tk.PhotoImage(file="fig/9.png")
    mx,my=1,1
    cx,cy = mx*100+50,my*100+50
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    main_proc()
    root.mainloop()