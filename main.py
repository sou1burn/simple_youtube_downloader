from tkinter import *
import pytube
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("500x250")
root.resizable(True, True)

root.title("Загрузчик")
root.config(bg="#D3D3D3")

def download():
    try:
        yt_link = link1.get()
        youtube_link = pytube.YouTube(yt_link)
        video = youtube_link.streams.get_highest_resolution()
        video.download()
        result = "Загружено"
        messagebox.showinfo("Готово", result)
    except:
        result = "Ссылка сломана"
        messagebox.showerror("Ошибка", result)

def reset():
    link1.set("")

def exit():
    root.destroy()

def selection(event):
    selection = combobox.get()
    print(selection)
    label["text"] = f"Вы выбрали {selection}"

icon = PhotoImage(file="icon.png")
root.iconphoto(True, icon)
lb = Label(root, text="Загрузка видео с Youtube", font=('Arial', 15, 'bold'), bg='#D3D3D3')
lb.pack(pady=15)

lb1=Label(root, text="Ссылка на видео :", font=('Arial',15,'bold'), bg='#D3D3D3')
lb1.place(x=10, y=80)

link1=StringVar()
En1=Entry(root, textvariable=link1, font=('Arial',15,'bold'))
En1.place(x=200, y=80)

btn1=Button(root, text="Скачать", font=('Arial',10,'bold'), bd=4, command=download)
btn1.place(x=380, y=130)

btn2=Button(root, text="Очистить", font=('Arial',10,'bold'), bd=4, command=reset)
btn2.place(x=280, y=130)

btn3=Button(root, text=" Выход ", font=('Arial',10,'bold'), bd=4, command=exit)
btn3.place(x=10, y=190)

resolutions = ["144p", '240p', '360p', '480p', "720p", "1080p", "2k", "4k"]
labels_res = Label(root, text="Выберите разрешение: ", font=('Arial', 15, 'bold'), bg='#D3D3D3')
labels_res.pack(pady=15)
labels_res.place(x=10,y = 130)
res_var = StringVar(value=resolutions[4])
label = ttk.Label(textvariable=res_var)

combobox = ttk.Combobox(textvariable=res_var, values=resolutions,  font=('Arial',10,'bold'), state="readonly")
combobox.pack(anchor=NW, fill=X, padx = 6, pady=6)
combobox.bind("<<ComboboxSelected>>", selection)
combobox.place(x=10, y = 160)
selection = combobox.get()
#res_var.set(new_value)
#combobox.set(new_value)

root.mainloop()
