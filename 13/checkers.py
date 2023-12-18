import tkinter as tk


def get_tipe(tag):
    if tag in "checker2":
        return -1
    return 1


def mouse_position(event):
    global x
    global y
    global current_item
    x = event.x
    y = event.y
    if current_item is not None:
        if plain[x // 50][y // 50] == 0 and abs(x//50-current_item[0])==1 and abs(y//50 -current_item[1])==1:
            item = canvas.find_closest(current_item[0] * 50 + 25, current_item[1] * 50 + 25)
            plain[x // 50][y // 50] = get_tipe(canvas.itemcget(item, "tags"))
            plain[current_item[0]][current_item[1]] = 0
            canvas.moveto(item, (x // 50) * 50, (y // 50) * 50)
            current_item = (x // 50, y // 50)



win = tk.Tk()


def clic_oval(event):
    global current_item
    if current_item is None:
        current_item = (x // 50, y // 50)
    elif plain[x//50][y//50]!=plain[current_item[0]][current_item[1]]:
        new_i = 2*(x//50)-current_item[0]
        new_j = 2*(y//50)-current_item[1]
        if -1 <new_j<8 and -1<new_i<8 and plain[new_i][new_j]==0:
            item = canvas.find_closest(current_item[0] * 50 + 25, current_item[1] * 50 + 25)
            plain[x // 50][y // 50] = get_tipe(canvas.itemcget(item, "tags"))
            plain[current_item[0]][current_item[1]] = 0
            plain[x//50][y//50]=0
            canvas.delete(canvas.find_closest(x,y))
            canvas.moveto(item, (new_i) * 50, (new_j) * 50)
            current_item = None
    else:
        current_item = None


canvas = tk.Canvas(win, bg='#fff', width=400, height=400)
plain = [[0] * 8 for _ in range(8)]
for i in range(0, 400, 400 // 8):
    canvas.create_line(i, 0, i, 400, fill='black')
    canvas.create_line(0, i, 400, i, fill='black')
for i in range(0, 8, 1):
    for j in range(0, 3, 1):
        if (i + j) % 2 == 0:
            canvas.create_oval((i * 50, j * 50), ((i + 1) * 50, (j + 1) * 50), fill="#0f0", activewidth=1.5,
                               activeoutline="red", tags="checker1")
            plain[i][j] = 1
    for j in range(5,8):
        if (i + j) % 2 == 0:
            plain[i][j] = -1
            canvas.create_oval((i * 50, j * 50), ((i + 1) * 50, (j + 1) * 50), fill="#f00", activewidth=1.5,
                               activeoutline="green", tags="checker2")
x, y = 0, 0

win.bind("<Motion>", mouse_position)

canvas.tag_bind("checker1", "<ButtonPress-1>", clic_oval)
canvas.tag_bind("checker2", "<ButtonPress-1>", clic_oval)
current_item = None

canvas.pack()
win.mainloop()
