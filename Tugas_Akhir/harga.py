from tkinter import *
from tkinter.messagebox import *
from tkinter.messagebox import showerror
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.resizable(width = 0, height = 0)
        self.config(bg="light green")
        self.title("Burjo Mantap Uhuy")

        self.judul = Label (self, text = "Burjo Mantap Uhuy ", 
                            font=('Berlin Sans FB Demi', 50), 
                            foreground="black")
        self.judul.place(x = 190, y = 0)
        
        self.judul = Label (self, text = "Daftar Menu Burjo Mantap Uhuy ", 
                            font=('Berlin Sans FB', 25), 
                            background = 'light green', 
                            foreground="black")
        self.judul.place(x = 250, y = 85)
        
        self.text4 = Text(self, font=('script MT bold', 30, ), 
                          width = 23, 
                          background="light green", 
                          foreground="black")
        self.text4.insert(INSERT, 'Menu Makanan')
        self.text4.place(y = 140)
        
        self.text5 = Text(self, font=('script MT bold', 30, ), 
                          width = 25, 
                          background="light green", 
                          foreground="black")
        self.text5.insert(INSERT, 'Menu Minuman')
        self.text5.place(x= 480, y = 140)

        food = ["1. Mie Goreng/Rebus : Rp 5.000", 
                "2. Nasi Lengko : Rp 5.000", 
                "3. Nasi Goreng : Rp 10.000",
                "4. Magelangan : Rp 10.000",
                "5. Nasi Orak arik telur : Rp 6.000",
                "6. Nasi Omelet : Rp 6.000",
                "7. Nasi Ayam Bali : Rp 10.000",
                "8. Nasi Ayam Geprek : Rp 10.000",
                "9. Burjo : Rp 5.000",
                "10. Pancong : Rp 7.000"]
        
        drink = ["1. Kopi Hitam : Rp 5.000", 
                 "2. Teh Anget/Es : Rp 5.000", 
                 "3. Jus Buah : Rp 10.000", 
                 "4. Es Campur : Rp 10.000",
                 "5. Good Day : Rp 5.000",
                 "6. Beng-beng : Rp 3.000",
                 "7. Milo : Rp 5.000",
                 "8. Ovomaltine : Rp 5.000",
                 "9. Energen : Rp 4.000",
                 "10. Nutrisari : Rp 2.000",
                 "11. Chocolatos : Rp 4.000",]
        
        self.text1 = Text(self, font=('century', 20),
                          pady=10,
                          background="light green", 
                          foreground="black")
        for i in food:
            self.text1.insert(INSERT, i + '\n')
            self.text1.place(y = 195)

        self.text3 = Text(self, font=('century', 20),
                          pady = 10, 
                          background="light green", 
                          foreground="black")
        for i in drink:
            self.text3.insert(INSERT, i + '\n')
            self.text3.place(x = 480, y = 195)

        self.button = Button(self, text = 'Kembali ke Pemesanan', 
                             font=('Times', 20, 'bold'),
                             bg='#4a7abc', 
                             fg='white', 
                             activebackground='green', 
                             activeforeground='white',)
        self.button['command'] = self.destroy
        self.button.place(x = 330, y = 600)
       
    def destroy(self):
        super().destroy() 
         
if __name__ == "__main__":
    app = App()
    app.mainloop()