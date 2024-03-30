from tkinter import * #thêm thư viện Tkinter
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

root = Tk() #tạo giao cửa sổ mới có tên là "root"
root.title('Control Panel')
root.geometry('500x500')

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_control = cast(interface, POINTER(IAudioEndpointVolume))

def update_volume(value):
    volume_level = float(value) / 100
    volume_control.SetMasterVolumeLevelScalar(volume_level, None)

# Tạo thanh trượt
volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label='Âm lượng', command=update_volume)
volume_slider.place(x= 0, y = 0, width= 500, height= 100)
# Lấy giá trị volum hiện tại để đồng bộ với slider
current_volume = volume_control.GetMasterVolumeLevelScalar()
volume_slider.set(current_volume * 100)

root.mainloop()