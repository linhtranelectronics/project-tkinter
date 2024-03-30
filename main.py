import tkinter as tk
import webbrowser
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import subprocess
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import os
import pygame
# Khởi tạo giao diện người dùng
root = tk.Tk()
root.title('Control Panel')
root.geometry('1000x1000')  # Điều chỉnh kích thước cửa sổ

# Lấy interface âm lượng
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_control = cast(interface, POINTER(IAudioEndpointVolume))
def update_volume(value):
    volume_level = float(value) / 100
    volume_control.SetMasterVolumeLevelScalar(volume_level, None)
# Tạo slider điều chỉnh âm lượng
volume_slider = tk.Scale(root, from_=0, to=100, orient='horizontal', label='Âm lượng', command=update_volume)
#volume_slider.pack(fill='x', padx=15, pady=10)
volume_slider.grid(row=0, column=0, columnspan= 30, rowspan= 1)
# Đặt giá trị slider phản ánh âm lượng hiện tại
current_volume = volume_control.GetMasterVolumeLevelScalar()
volume_slider.set(current_volume * 100)


def update_brightness(value):
    sbc.set_brightness(int(value))
# Tạo slider điều chỉnh độ sáng
brightness_slider = tk.Scale(root, from_=0, to=100, orient='horizontal', label='Độ sáng', command=update_brightness)
#brightness_slider.pack(fill='x', padx=15, pady=10)
brightness_slider.grid(row= 1, column= 0, columnspan= 3)

# Đặt giá trị slider phản ánh độ sáng hiện tại
current_brightness = sbc.get_brightness()
brightness_slider.set(current_brightness)


def open_google():
    webbrowser.open('http://www.google.com')

def open_youtube():
    webbrowser.open('https://www.youtube.com')
# Tạo nút mở Chrome
btn_open_google = tk.Button(root, text='Mở Google', command=open_google)
btn_open_google.grid(row= 6, column= 0 )

btn_open_google = tk.Button(root, text='Mở Youtube', command=open_youtube)
btn_open_google.grid(row= 7, column= 0)


def shutdown():
    subprocess.call("shutdown /s /t 0", shell=True)
# Tạo nút tắt máy
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown, bg="red")
#shutdown_button.pack(pady=20)
shutdown_button.grid(row= 2, column= 0)


# Tạo nhãn thời gian
time_label = tk.Label(root, text="Current Time: ")
#time_label.pack(pady=20)
time_label.grid(row= 3, column= 0)
def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text="Current Time: " + current_time)
    time_label.after(1000, update_time)  # Cập nhật thời gian sau mỗi giây


# Cập nhật thời gian
update_time()
def play_mp3(file_path):
    # Khởi tạo Pygame
    pygame.init()

    # Khởi tạo mixer
    pygame.mixer.init()

    try:
        # Load file âm thanh
        pygame.mixer.music.load(file_path)

        # Phát âm thanh
        pygame.mixer.music.play()

        # Chờ cho đến khi âm thanh kết thúc
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error:
        print("Không thể phát file âm thanh.")

    # Đóng Pygame
    pygame.mixer.quit()
    pygame.quit()

def text_to_speech():
    # Lấy văn bản từ text_entry
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        # Tạo một đối tượng gTTS với văn bản và ngôn ngữ
        tts = gTTS(text=text, lang='vi')

        # Lưu giọng nói thành một file tạm thời
        tts.save("output.mp3")

        # Phát âm thanh từ file
        #playsound("output.mp3")

        play_mp3("output.mp3")
        # Xóa file tạm thời sau khi đã phát
        os.remove("output.mp3")

# Tạo text_entry để nhập văn bản
text_entry = tk.Text(root, height=10, width=50)
#text_entry.pack(pady=10)
text_entry.grid(row= 4, column= 0)
# Tạo nút "Chuyển thành giọng nói"
convert_button = tk.Button(root, text="Chuyển thành giọng nói", command=text_to_speech)
convert_button.grid(row=5, column= 0)












root.mainloop()