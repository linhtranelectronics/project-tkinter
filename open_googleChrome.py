from tkinter import * #thêm thư viện Tkinter
import webbrowser

root = Tk() #tạo giao cửa sổ mới có tên là "root"
root.title('Control Panel')
root.geometry('500x500')

def open_youtube():
    webbrowser.open('https://www.youtube.com')
open_youtube_button = Button(root, text= 'open youtube', command=open_youtube, bg= 'red')
open_youtube_button.place(x = 0, y = 0, width= 100, height= 100)

def open_facebook():
    webbrowser.open('https://www.facebook.com')
open_facebook_button = Button(root, text= 'open FB', command=open_facebook, bg= 'blue')
open_facebook_button.place(x = 120, y = 0, width= 100, height= 100)

root.mainloop()  #chạy cửa sổ root