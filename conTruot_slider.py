from tkinter import * #thêm thư viện Tkinter

root = Tk() #tạo giao cửa sổ mới có tên là "root"
root.title('Control Panel')
root.geometry('500x500')

def on_slider_move(value):
    print("Giá trị mới:", value)
# Tạo thanh trượt
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=on_slider_move)
slider.place(x= 0, y = 0, width= 500, height= 50)


root.mainloop()