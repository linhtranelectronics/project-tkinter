from tkinter import * #thêm thư viện Tkinter

root = Tk() #tạo giao cửa sổ mới có tên là "root"
root.title('Control Panel')
root.geometry('500x500')

def show_text():
    label = Label(root, font=("Arial", 20), text="Hello, world!")
    label.place(x = 0, y= 0, width=500, height=100)


button = Button(root, text="Nhấn để hiện text", command=show_text)
button.place(x = 200, y= 100, width=100, height=50)

root.mainloop()  #chạy cửa sổ root