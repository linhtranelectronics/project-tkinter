from tkinter import * #thêm thư viện Tkinter

root = Tk() #tạo giao cửa sổ mới có tên là "root"
root.title('Control Panel')
root.geometry('500x500')

box = Entry(root,font=("Arial", 20))
box.place(x=0, y=0, width=500, height=50)

def show_text():
    text = box.get()
    binhPhuong = int(text) ** 2
    label = Label(root, font=("Arial", 20), text=binhPhuong)
    label.place(x = 0, y=150, width=500, height=100)

button = Button(root, text="Tính bình phương", command=show_text)
button.place(x = 200, y= 100, width=100, height=50)

root.mainloop()  #chạy cửa sổ root