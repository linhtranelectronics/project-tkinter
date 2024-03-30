from tkinter import * #thêm thư viện Tkinter

root = Tk() #tạo giao cửa sổ mới có tên là "root"
root.title('Control Panel')
root.geometry('500x500')

root.title("Ô nhập văn bản")
box = Entry(root)
box.place(x=0, y=0, width=500, height=50)

def get_text():
    text = box.get()
    print("Nội dung đã nhập:", text)
button = Button(root, text="Nhận nội dung", command=get_text)
button.place(x=200, y=100, width=100, height=50)

root.mainloop()  #chạy cửa sổ root