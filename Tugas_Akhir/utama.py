from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.messagebox import showerror
import tkinter as tk
from harga import App

class Awal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.config(bg="red")
        self.resizable(width = 0, height = 0)
        self.title("Burjo Mantap Uhuy")

        self.img = PhotoImage(file = "D:/FILE ALIEF/PRAKTIKUM DKP/burjo.png")
        self.image = Label (self, image = self.img)
        self.image.place(y = -200)
        
        self.button = Button(self, text = 'Pesan Sekarang', font = ('Times', 15, 'bold'),
                                 padx=1,
                                 pady=1,
                                 activebackground='#4a6abc',
                                 activeforeground='white',)
        self.button['command'] = self.destroy
        self.button.place(x = 440, y = 640)
       
    def destroy(self):
        super().destroy() 
         
if __name__ == "__main__":
    awal = Awal()
    awal.mainloop()

top = Tk()
top.geometry("1000x800")
top.resizable(width = 0, height = 0)
top.config(bg="light blue")
top.title("Burjo Mantap Uhuy")

judul = Label (top, text = "Burjo Mantap Uhuy ", 
font=('Berlin Sans FB Demi', 50), foreground="black")
judul.place(x = 190, y = 0)

pembuka1 = Label (top, text = "Terima kasih Telah mampir Ke Burjo mantap Uhuy", 
font=('Berlin Sans FB', 20), background="light blue", foreground="black")
pembuka1.place(x = 210, y = 85)

pembuka = Label (top, text = "Silahkan Pesan Makanan dan Minuman yang Tersedia", 
font=('Berlin Sans FB', 20), background="light blue", foreground="black")
pembuka.place(x = 190, y = 120)

food = ["1. Mie Goreng/Rebus : Rp 5.000", 
        "2. Nasi Lengko : Rp 5.000", 
        "3. Nasi Goreng : Rp.10.000"]
food.append("4. Bubur Kacang Ijo : Rp 3.000")

drink = ["1. Kopi Hitam : Rp 5.000", 
         "2. Teh Anget/Es : Rp 5.000", 
         "3. Jus Buah : Rp.10.000", 
         "4. Es Campur : Rp.10.000"]

text = Text(top, font=('Century', 15, 'bold'), 
            width = 800, 
            background="#4a6abc", 
            foreground="white")
text.insert(INSERT, 'Menu Makanan Unggulan')
text.place(y = 170)

text1 = Text(top, font=('Kristen ITC', 13), 
             width = 800, 
             background="light blue", 
             foreground="black")
for i in food:
    text1.insert(INSERT, i + '\n')
text1.place(y = 200)

text2 = Text(top, font=('Century', 15, 'bold'), 
             width = 800, 
             background="#4a6abc", 
             foreground="white")
text2.insert(INSERT, 'Menu Minuman Unggulan')
text2.place(y = 300)

text3 = Text(top, font= ('Kristen ITC', 13), 
             width = 800, 
             background="light blue", 
             foreground="black")
for i in drink:
    text3.insert(INSERT, i + '\n')
    text3.place(y = 330)


pesan_apa = Label (top, text = "Pilih makanan yang ingin dipesan :                ", 
                   font=('Algerian', 15), 
                   background="#4a6abc", 
                   foreground="white")
pesan_apa.place(y = 440)

strmakanan = StringVar(value='...')
combobox1 = ttk.Combobox(top, 
                        width = 20,
                        font = ('Algerian', 15), 
                        textvariable = strmakanan, 
                        state ="readonly")
combobox1.place(x=480, y=440)
combobox1["values"] = ("Mie Goreng/Rebus", 
                        "Nasi Lengko", 
                        "Nasi Goreng",
                        "Magelangan",
                        "Nasi Orak arik telur",
                        "Nasi Omelet",
                        "Nasi Ayam Bali",
                        "Nasi Ayam Geprek",
                        "Bubur Kacang Ijo",
                        "Pancong")

pesan_berapa = Label (top, text = "Berapa makanan yang ingin anda pesan : ",
                      font=('Algerian', 15), 
                      background="#4a6abc", 
                      foreground="white")
pesan_berapa.place(y = 470)

jumlah = Entry (top, 
                font=('century', 10),
                width = 36, 
                bd = 5)
jumlah.place(x = 480, y = 470)

pesan_minum = Label (top, text = "Pilih minuman yang ingin dipesan :                  ", 
                     font=('Algerian', 15), 
                     background="#4a6abc", 
                     foreground="white")
pesan_minum.place(y = 500)

strminuman = StringVar(value='...')
combobox2 = ttk.Combobox(top, 
                        width = 20,
                        font = ('Algerian', 15), 
                        textvariable = strminuman, 
                        state ="readonly")

combobox2.place(x=480, y=500)
combobox2["values"] = ("Kopi Hitam", 
                 "Teh Anget/Es", 
                 "Jus Buah", 
                 "Es Campur",
                 "Good Day",
                 "Beng-beng",
                 "Milo",
                 "Ovomaltine",
                 "Energen",
                 "Nutrisari",
                 "Chocolatos")

pesan_berapa_minum = Label (top, text = "Berapa minuman yang ingin anda pesan :    ",
                            font=('Algerian', 15), 
                            background="#4a6abc", 
                            foreground="white")
pesan_berapa_minum.place(y = 530)

jumlah_minum = Entry (top,
                      font=('century', 10), 
                      width = 36, 
                      bd = 5)
jumlah_minum.place(x = 480, y = 530)



def display():
    pesan_makan = jumlah.get()
    pesan_minum = jumlah_minum.get()
    try:
       pesan_makan = int(pesan_makan)
       pesan_minum = int(pesan_minum)
    except ValueError:
        showerror('Warning!!!', 'Masukkan angka 1-10 pada jumlah yang ingin dipesan!!')
    else:  
        if pesan_minum < 1 :
            info = messagebox.showinfo ('Warning!!!', 'Masukkan angka 1-10 pada jumlah yang ingin dipesan!!')
            info.pack()
        elif pesan_minum > 10 :
            info = messagebox.showinfo ('Warning!!!', 'Masukkan angka 1-10 pada jumlah yang ingin dipesan!!')
            info.pack()
        else :
            if pesan_makan < 1 :
                info = messagebox.showinfo ('Warning!!!', 'Masukkan angka 1-10 pada jumlah yang ingin dipesan!!')
                info.pack()
            elif pesan_makan > 10 :
                info = messagebox.showinfo ('Warning!!!', 'Masukkan angka 1-10 pada jumlah yang ingin dipesan!!')
                info.pack()
            else :
                info = messagebox.showinfo ("Terima kasih sudah mampir ke Burjo Mantap Uhuy", "Silahkan duduk dan makanan akan segera disajikan...")
            info.pack()
            

button = Button(top, text = "Pesan Sekarang", 
font=('Times', 20, 'bold'),
    padx=1,
    pady=1,
    bg='#4a7abc',
    fg='white',
    activebackground='green',
    activeforeground='white', 
    command = display)
button.place(x = 250, y = 600)

button = Button(top, text = "Lihat Daftar Menu",
    font=('Times', 20, 'bold'),
    padx=1,
    pady=1,
    bg='#4a7abc',
    fg='white',
    activebackground='green',
    activeforeground='white',
    command = App,
    )
button.place(x = 470, y = 600)



top.mainloop()