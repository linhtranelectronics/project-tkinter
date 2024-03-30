from tkinter import * #thêm thư viện Tkinter

root = Tk() #tạo giao cửa sổ mới có tên là "root"

root.title('Control Panel')

root.geometry('500x500')

def clickButton1():
    print('bạn vừa nhấn nút 1')
button1 = Button(root, text= 'nút nhấn 1', command=clickButton1, bg= 'red')
button1.place(x = 0, y = 0, width= 100, height= 100)

def clickButton2():
    print('bạn vừa nhấn nút 2')
button2 = Button(root, text= 'nút nhấn 2', command=clickButton2, bg= 'green')
button2.place(x = 200, y = 0, width= 100, height= 100)

def clickButton3():
    print('bạn vừa nhấn nút 3')
button3 = Button(root, text= 'nút nhấn 3', command=clickButton3, bg= 'blue')
button3.place(x = 100, y = 120, width= 100, height= 100)

root.mainloop()  #chạy cửa sổ root