import tkinter
import random
import time
from datetime import datetime
from gif import ImageLabel
class Program:
    def __init__(self):
        self.start_time = datetime.now()
        self.finis = None
        self.modry = 0
        self.cerveny = 0
        self.k = None
        self.l = None
        self.narade = 0
        self.hod = 0
        self.root = tkinter.Tk()
        self.root.title("Človeče nehnevaj sa")
        self.menu = tkinter.Menu(self.root)
        self.ponuka = tkinter.Menu(self.menu)
        self.ponuka.add_command(label='Nová hra',command=self.restart)
        self.ponuka.add_separator()
        self.ponuka.add_command(label='Skóre',command=self.skore)
        self.ponuka.add_separator()
        self.ponuka.add_command(label="Opustiť hru",command=self.opusti)
        self.menu.add_cascade(label='Ponuka', menu=self.ponuka)
        self.root.config(menu=self.menu)
        self.root.geometry("1280x720")
        self.Console = tkinter.Text(self.root,height = 12, width = 25,font='Courier 20 normal',state="normal")
        self.Console.pack()
        # unicodove oznacenia pre kocky od 1 do 6
        self.kocka = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.label = tkinter.Label(self.root, text='', font=('Helvetica', 260))
        canvas = tkinter.Canvas()
        canvas.pack()
        plocha = []
        pomoc = []
        n = 11
        k = 0
        for i in range(0, n + 1):
            pomoc = []
            for x in range(0, n + 1):
                pomoc.append(" ")
            plocha.append(pomoc)

        for cl in range(0, n):
            if k == -1:
                k = 9
            if k == 10:
                k = 0
            plocha[cl + 1][0] = str(k)
            k = k + 1
        k = 0
        cl = 0
        for cl in range(0, n):
            if k == -1:
                k = 9
            if k == 10:
                k = 0
            plocha[0][cl + 1] = str(k)
            k = k + 1

        for i in range(0, n):
            if i < (n + 1) // 2 - 1:
                plocha[i + 1][(n) // 2] = "*"
            elif i == (n) // 2:
                plocha[i + 1][(n) // 2] = "D"
            elif i > (n) // 2:
                plocha[i + 1][(n) // 2] = "*"

        for i in range(0, n):
            if i == 0:
                plocha[i + 1][(n + 1) // 2] = "*"
            elif i < (n + 1) // 2 - 1:
                plocha[i + 1][(n + 1) // 2] = "D"
            elif i == (n) // 2:
                plocha[i + 1][(n + 1) // 2] = "X"
            elif i == (n - 1):
                plocha[i + 1][(n + 1) // 2] = "*"
            elif i > (n) // 2:
                plocha[i + 1][(n + 1) // 2] = "D"
        i = 0
        for i in range(0, n):
            if i < (n + 1) // 2 - 1:
                plocha[i + 1][(n + 3) // 2] = "*"
            elif i == (n) // 2:
                plocha[i + 1][(n + 3) // 2] = "D"
            elif i > (n) // 2:
                plocha[i + 1][(n + 3) // 2] = "*"

        for i in range(0, n):
            if i < (n + 1) // 2 - 1:
                plocha[(n) // 2][i + 1] = "*"
            elif i == (n) // 2:
                plocha[(n) // 2][i + 1] = "D"
            elif i > (n) // 2:
                plocha[(n) // 2][i + 1] = "*"
        for i in range(0, n):
            if i < (n + 1) // 2 - 1:
                plocha[(n + 3) // 2][i + 1] = "*"
            elif i == (n) // 2:
                plocha[(n + 3) // 2][i + 1] = "D"
            elif i > (n) // 2:
                plocha[(n + 3) // 2][i + 1] = "*"

        for i in range(0, n):
            if i == 0:
                plocha[(n + 1) // 2][i + 1] = "*"
            elif i < (n + 1) // 2 - 1:
                plocha[(n + 1) // 2][i + 1] = "-"
            elif i == (n) // 2:
                plocha[(n + 1) // 2][i + 1] = "X"
            elif i == (n - 1):
                plocha[(n + 1) // 2][i + 1] = "*"
            elif i > (n) // 2:
                plocha[(n + 1) // 2][i + 1] = "-"
        self.plocha = plocha
        #plocha[1][7] = "M"  # Myšlienka - hod kockou napr 5 = 5* prikaz jeden prikaz 1 posun, exaktne definovať posun na pozície

        self.vykresli()

        self.Console.config(state="disabled")
        self.w = tkinter.Label(self.root, text = "Aktuálne hádže: Modrý")
        self.w.place(x=590, y=365)
        self.w.config(fg="Blue")
        self.padlo = tkinter.Label(self.root, text="")
        self.padlo.place(x=220, y=125)
        self.button2 = tkinter.Button(self.root, text ="Hod kockou", command = self.hodkockou,height = "5",width = "10",bg="white",foreground = 'red')
        self.button2.place(x=220, y=25)
        self.button3 = tkinter.Button(self.root, text ="Opustiť hru", command = self.opusti,height = "1",width = "8",bg="red",foreground = 'black')
        self.button3.place(x=1215, y=695)
        self.root.mainloop()

    def vykresli(self):
        for c in range(len(self.plocha)):
            self.zapis(' '.join(self.plocha[c]))

    def opusti(self):
        raise SystemExit(0)

    def hodik(self):
        # unicodove oznacenia pre kocky od 1 do 6
        kocka = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(75, 170), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(250, 380), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(250, 380), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(250, 380), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(350, 480), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(350, 580), self.label.configure(text=f'{random.choice(kocka)}'))
        self.label.place(x=120, y=100)
        self.root.update()
        self.root.after(random.randrange(150, 680), self.label.configure(text=f'{kocka[self.hod-1]}'))
        self.label.place(x=120, y=100)
        self.root.update()
        time.sleep(0.2)

    def skore(self):
        with open("skore.txt", "r", encoding="UTF-8") as f:
            content = f.readlines()
        content = [x.strip() for x in content]

        height = len(content)
        width = 1
        el = 0
        xtapa = tkinter.Tk()
        for i in reversed(range(height)):  # Riadky
            for j in range(width):  # Stlpce
                b = tkinter.Label(xtapa, text=f"{str(content[i])}")
                b.config(state="normal")
                b.grid(row=el, column=j)
                b.config(state="disabled")
            el += 1

    def vyhra(self,rozhodnutie):
        if rozhodnutie =="M":
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=0)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=0)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=0)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=0)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=0)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=0)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=0)
            # 1.riadok
            c = 200
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=c)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=c)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=c)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=c)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=c)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=c)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=c)

            # 2. riadok
            huf = 400
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=huf)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=huf)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=huf)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=huf)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=huf)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=huf)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=huf)

            # Posledny-riadok
            cal = 600
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=cal)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=cal)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=cal)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=cal)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=cal)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=cal)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=cal)

            haka = tkinter.Label(self.root, text="Modrý tím vyhral!", )
            haka.config(width=15, height=1, font=("Helvetica", 32), background="#ffffff", borderwidth=0,
                        foreground="blue")
            haka.place(x=400, y=300)

            elem = tkinter.Button(self.root, text="Začať novú partiu", width=30, height=5, command=self.restart)
            elem.place(x=480, y=400)

            time_elapsed = datetime.now() - self.start_time

            haka = tkinter.Label(self.root, text=f"Trvanie hry: {time_elapsed}", )
            haka.config(width=20, height=1, background="#ffffff", borderwidth=0)
            haka.place(x=525, y=600)
            subor = open("skore.txt", "a", encoding="UTF-8")
            subor.write(f"M {time_elapsed}" + "\n")
            subor.close()
            elem = tkinter.Button(self.root, text="Pozri skóre", width=10, height=2, command=self.skore)
            elem.place(x=550, y=500)
        elif rozhodnutie =="Č":
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=0)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=0)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=0)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=0)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=0)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=0)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=0)
            # 1.riadok
            c = 200
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=c)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=c)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=c)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=c)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=c)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=c)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=c)

            # 2. riadok
            huf = 400
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=huf)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=huf)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=huf)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=huf)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=huf)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=huf)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=huf)

            # Posledny-riadok
            cal = 600
            padlo = ImageLabel(self.root)
            padlo.load("confeti.gif")
            padlo.configure(background="#ffffff", borderwidth=0)
            padlo.place(x=0, y=cal)

            padlo1 = ImageLabel(self.root)
            padlo1.load("confeti.gif")
            padlo1.configure(background="#ffffff", borderwidth=0)
            padlo1.place(x=150, y=cal)

            padlo2 = ImageLabel(self.root)
            padlo2.load("confeti.gif")
            padlo2.configure(background="#ffffff", borderwidth=0)
            padlo2.place(x=250, y=cal)

            padlo3 = ImageLabel(self.root)
            padlo3.load("confeti.gif")
            padlo3.configure(background="#ffffff", borderwidth=0)
            padlo3.place(x=350, y=cal)

            padlo4 = ImageLabel(self.root)
            padlo4.load("confeti.gif")
            padlo4.configure(background="#ffffff", borderwidth=0)
            padlo4.place(x=450, y=cal)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=750, y=cal)

            padlo5 = ImageLabel(self.root)
            padlo5.load("confeti.gif")
            padlo5.configure(background="#ffffff", borderwidth=0)
            padlo5.place(x=1000, y=cal)

            haka = tkinter.Label(self.root, text="Červený tím vyhral!", )
            haka.config(width=15, height=1, font=("Helvetica", 32), background="#ffffff", borderwidth=0,
                        foreground="red")
            haka.place(x=400, y=300)

            elem = tkinter.Button(self.root, text="Začať novú partiu", width=30, height=5, command=self.restart)
            elem.place(x=480, y=400)

            time_elapsed = datetime.now() - self.start_time

            haka = tkinter.Label(self.root, text=f"Trvanie hry: {time_elapsed}", )
            haka.config(width=20, height=1, background="#ffffff", borderwidth=0)
            haka.place(x=525, y=600)
            subor = open("skore.txt", "a", encoding="UTF-8")
            subor.write(f"Č {time_elapsed}" + "\n")
            subor.close()
            elem = tkinter.Button(self.root, text="Pozri skóre", width=10, height=2, command=self.skore)
            elem.place(x=550, y=500)

        else:
            print("CHYBA !")

    def restart(self):
        self.root.destroy()
        while True:
            Program()

    def najdi(self,slovo):
        for i in self.plocha:
            for x in i:
                if x == slovo:
                    return True
        return False


    def zapis(self,*ano, end = "\n", sep = " "):
        self.text = ""
        for polozka in ano:
            self.text += "{}".format(polozka)
            self.text += sep
        self.text += end
        self.Console.insert(tkinter.INSERT, self.text)
    def hodkockou(self):
        hod = random.randrange(1,7)
        self.hod = hod
        self.button2 = tkinter.Button(self.root, text="Hod kockou", command=self.hodkockou, height="5", width="10",bg="white", foreground='red')
        self.button2.place(x=220, y=25)
        self.button2.config(state="disabled")
        self.w.config(text="")
        self.padla = tkinter.Label(self.root, text=f"")
        self.padla.place(x=220, y=125)
        self.padla.config(text="                           ")
        self.root.update()
        self.hodik()
        time.sleep(0.3)
        self.root.update()
        self.rob()
        if self.narade == 0:
            self.narade = 1
        elif self.narade == 1:
            self.narade = 0
        if self.finis == None:
            self.padlo = tkinter.Label(self.root, text=f"Padlo {self.hod}")
            self.padlo.place(x=220, y=125)
            self.padlo.config(text=f"Padlo {self.hod}")
            self.button2.config(state="normal")
        else:
            pass

        self.root.update()
    def rob(self):

        #self.narade 0 = "M";self.narade 1="Č"
        if self.narade == 0 and self.najdi("M")== False:
            if self.hod == 6:
                self.plocha[1][7] = "M"
                self.Console.config(state="normal")
                self.Console.delete('1.0', tkinter.END)
                self.vykresli()
                self.Console.config(state="disabled")
                self.root.update()
                self.w.config(text="Aktuálne hádže: Červený")
                self.w.config(fg="Red")
                self.modry = 0
                return
            else:
                self.modry = self.modry + 1
                hod1 = random.randrange(1, 7)
                hod2 = random.randrange(1, 7)
                hod3 = random.randrange(1, 7)
                self.padla = tkinter.Label(self.root, text=f"")
                self.padla.place(x=220, y=125)
                self.padla.config(text=f"Padlo: {hod1},{hod2},{hod3}")
                self.hod = hod1
                zoznamik = [hod1,hod2,hod3]
                zoznamik.sort()
                hodos = zoznamik[-1]
                self.root.after(random.randrange(50, 380), self.label.configure(text=f'{self.kocka[hodos - 1]}'))
                self.label.place(x=120, y=100)
                self.root.update()
                time.sleep(0.2)
                if (hod1==6) or (hod2==6) or (hod3==6):
                    self.hod = 6
                    self.rob()
                else:
                    self.w.config(text="Aktuálne hádže: Červený")
                    self.w.config(fg="Red")
                self.root.update()
                return


        elif self.narade == 1 and self.najdi("Č") == False:
            if self.hod == 6:
                self.plocha[11][5] = "Č"
                self.Console.config(state="normal")
                self.Console.delete('1.0', tkinter.END)
                self.vykresli()
                self.Console.config(state="disabled")
                self.root.update()
                self.w.config(text="Aktuálne hádže: Modrý")
                self.w.config(fg="Blue")
                return
            else:
                hod1 = random.randrange(1, 7)
                hod2 = random.randrange(1, 7)
                hod3 = random.randrange(1, 7)
                self.padla = tkinter.Label(self.root, text=f"")
                self.padla.place(x=220, y=125)
                self.padla.config(text=f"Padlo: {hod1},{hod2},{hod3}")
                self.hod = hod1
                zoznamik = [hod1,hod2,hod3]
                zoznamik.sort()
                hodos = zoznamik[-1]
                self.root.after(random.randrange(50, 380), self.label.configure(text=f'{self.kocka[hodos - 1]}'))
                self.label.place(x=120, y=100)
                self.root.update()
                time.sleep(0.2)
                if (hod1==6) or (hod2==6) or (hod3==6):
                    self.hod = 6
                    self.rob()
                else:
                    self.w.config(text="Aktuálne hádže: Modrý")
                    self.w.config(fg="Blue")
                self.root.update()
                return
        # else:
        #     if self.narade ==0:
        #         self.w.config(text="Aktuálne hádže: Červený")
        #         self.w.config(fg="Red")
        #     else:
        #         self.w.config(text="Aktuálne hádže: Modrý")
        #         self.w.config(fg="Blue")
        if self.narade == 0:
            self.padla = tkinter.Label(self.root, text=f"")
            self.padla.place(x=220, y=125)
            self.padla.config(text="                           ")
            self.padlo = tkinter.Label(self.root, text=f"Padlo {self.hod}")
            self.padlo.place(x=220, y=125)
            self.padlo.config(text=f"Padlo {self.hod}")
            self.root.update()
            if self.plocha[1][6] == "M" and self.hod == 6:
                if self.plocha[2][6] == "V":
                    if self.plocha[3][6] == "Ý":
                        if self.plocha[4][6] == "H":
                            if self.plocha[5][6] == "R":
                                self.plocha[1][6] = "*"
                                self.plocha[6][6] = "A"
                                self.Console.config(state="normal")
                                self.Console.delete('1.0', tkinter.END)
                                self.vykresli()
                                self.Console.config(state="disabled")
                                self.root.update()
                                time.sleep(0.3)
                                self.vyhra("M")

                            else:
                                self.plocha[1][6] = "*"
                                self.plocha[5][6] = "R"
                                self.Console.config(state="normal")
                                self.Console.delete('1.0', tkinter.END)
                                self.vykresli()
                                self.Console.config(state="disabled")
                                self.root.update()
                                return
                        else:
                            self.plocha[1][6] = "*"
                            self.plocha[4][6] = "H"
                            self.Console.config(state="normal")
                            self.Console.delete('1.0', tkinter.END)
                            self.vykresli()
                            self.Console.config(state="disabled")
                            self.root.update()
                            return

                    else:
                        self.plocha[1][6] = "*"
                        self.plocha[3][6] = "Ý"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        return

                else:
                    self.plocha[2][6] = "V"
                    self.plocha[1][6] = "*"
                    self.Console.config(state="normal")
                    self.Console.delete('1.0', tkinter.END)
                    self.vykresli()
                    self.Console.config(state="disabled")
                    self.root.update()
                    return



            for i in range(self.hod):
                time.sleep(0.3)
                if self.plocha[1][7] == "M":
                    self.plocha[1][7] = "*"
                    if i < (self.hod-1) and self.plocha[2][7]=="Č":
                        self.plocha[2][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[2][7] = "Č"
                        self.k = 1

                    else:
                        self.plocha[2][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None

                elif self.plocha[2][7] == "M" or self.k==1:
                    if self.k==1:
                        pass
                    else:
                        self.plocha[2][7] = "*"
                    if i < (self.hod-1) and self.plocha[3][7]=="Č":
                        self.plocha[2][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[3][7] = "Č"
                        self.k = 2

                    else:
                        self.plocha[3][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[3][7] == "M" or self.k==2:
                    if self.k == 2:
                        pass
                    else:
                        self.plocha[3][7] = "*"
                    if i < (self.hod-1) and self.plocha[4][7]=="Č":
                        self.plocha[4][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[4][7] = "Č"
                        self.k = 3

                    else:
                        self.plocha[4][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[4][7] == "M" or self.k== 3:
                    if self.k == 3:
                        pass
                    else:
                        self.plocha[4][7] = "*"
                    if i < (self.hod-1) and self.plocha[5][7]=="Č":
                        self.plocha[5][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][7] = "Č"
                        self.k = 4

                    else:
                        self.plocha[5][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][7] == "M" or self.k==4:
                    if self.k == 4:
                        pass
                    else:
                        self.plocha[5][7] = "*"
                    if i < (self.hod-1) and self.plocha[5][8]=="Č":
                        self.plocha[5][8] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][8] = "Č"
                        self.k = 5

                    else:
                        self.plocha[5][8] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                    self.root.update()
                elif self.plocha[5][8] == "M" or self.k==5:
                    if self.k == 5:
                        pass
                    else:
                        self.plocha[5][8] = "*"
                    if i < (self.hod-1) and self.plocha[5][9]=="Č":
                        self.plocha[5][9] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][9] = "Č"
                        self.k = 6

                    else:
                        self.plocha[5][9] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][9] == "M" or self.k==6:
                    if self.k == 6:
                        pass
                    else:
                        self.plocha[5][9] = "*"
                    if i < (self.hod-1) and self.plocha[5][10]=="Č":
                        self.plocha[5][10] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][10] = "Č"
                        self.k = 7

                    else:
                        self.plocha[5][10] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][10] == "M" or self.k==7:
                    if self.k == 7:
                        pass
                    else:
                        self.plocha[5][10] = "*"
                    if i < (self.hod-1) and self.plocha[5][11]=="Č":
                        self.plocha[5][11] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][11] = "Č"
                        self.k = 8

                    else:
                        self.plocha[5][11] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][11] == "M" or self.k==8:
                    if self.k == 8:
                        pass
                    else:
                        self.plocha[5][11] = "*"
                    if i < (self.hod-1) and self.plocha[6][11]=="Č":
                        self.plocha[6][11] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[6][11] = "Č"
                        self.k = 9

                    else:
                        self.plocha[6][11] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[6][11] == "M" or self.k==9:
                    if self.k == 9:
                        pass
                    else:
                        self.plocha[6][11] = "*"
                    if i < (self.hod-1) and self.plocha[7][11]=="Č":
                        self.plocha[7][11] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][11] = "Č"

                        self.k = 10

                    else:
                        self.plocha[7][11] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][11] == "M" or self.k==10:
                    if self.k == 10:
                        pass
                    else:
                        self.plocha[7][11] = "*"
                    if i < (self.hod-1) and self.plocha[7][10]=="Č":
                        self.plocha[7][10] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][10] = "Č"
                        self.k = 11

                    else:
                        self.plocha[7][10] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][10] == "M" or self.k==11:
                    if self.k == 11:
                        pass
                    else:
                        self.plocha[7][10] = "*"
                    if i < (self.hod-1) and self.plocha[7][9]=="Č":
                        self.plocha[7][9] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][9] = "Č"
                        self.k = 12

                    else:
                        self.plocha[7][9] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][9] == "M" or self.k==12:
                    if self.k == 12:
                        pass
                    else:
                        self.plocha[7][9] = "*"
                    if i < (self.hod-1) and self.plocha[7][8]=="Č":
                        self.plocha[7][8] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][8] = "Č"
                        self.k = 13

                    else:
                        self.plocha[7][8] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][8] == "M" or self.k==13:
                    if self.k == 13:
                        pass
                    else:
                        self.plocha[7][8] = "*"
                    if i < (self.hod-1) and self.plocha[7][7]=="Č":
                        self.plocha[7][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][7] = "Č"
                        self.k = 14

                    else:
                        self.plocha[7][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                    self.root.update()
                elif self.plocha[7][7] == "M" or self.k==14:
                    if self.k == 14:
                        pass
                    else:
                        self.plocha[7][7] = "*"
                    if i < (self.hod-1) and self.plocha[8][7]=="Č":
                        self.plocha[8][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[8][7] = "Č"
                        self.k = 15

                    else:
                        self.plocha[8][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[8][7] == "M" or self.k==15:
                    if self.k == 15:
                        pass
                    else:
                        self.plocha[8][7] = "*"
                    if i < (self.hod-1) and self.plocha[9][7]=="Č":
                        self.plocha[9][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[9][7] = "Č"
                        self.k = 16

                    else:
                        self.plocha[9][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[9][7] == "M" or self.k==16:
                    if self.k == 16:
                        pass
                    else:
                        self.plocha[9][7] = "*"
                    if i < (self.hod-1) and self.plocha[10][7]=="Č":
                        self.plocha[10][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[10][7] = "Č"
                        self.k = 17

                    else:
                        self.plocha[10][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[10][7] == "M" or self.k==17:
                    if self.k == 17:
                        pass
                    else:
                        self.plocha[10][7] = "*"
                    if i < (self.hod-1) and self.plocha[11][7]=="Č":
                        self.plocha[11][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[11][7] = "Č"
                        self.k = 18

                    else:
                        self.plocha[11][7] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[11][7] == "M" or self.k==18:
                    if self.k == 18:
                        pass
                    else:
                        self.plocha[11][7] = "*"
                    if i < (self.hod-1) and self.plocha[11][6]=="Č":
                        self.plocha[11][6] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[11][6] = "Č"
                        self.k = 19

                    else:
                        self.plocha[11][6] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[11][6] == "M" or self.k==19:
                    if self.k == 19:
                        pass
                    else:
                        self.plocha[11][6] = "*"
                    if i < (self.hod-1) and self.plocha[11][5]=="Č":
                        self.plocha[11][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[11][5] = "Č"
                        self.k = 20

                    else:
                        self.plocha[11][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[11][5] == "M" or self.k==20:
                    if self.k == 20:
                        pass
                    else:
                        self.plocha[11][5] = "*"
                    if i < (self.hod-1) and self.plocha[10][5]=="Č":
                        self.plocha[10][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[10][5] = "Č"
                        self.k = 21

                    else:
                        self.plocha[10][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[10][5] == "M" or self.k==21:
                    if self.k == 21:
                        pass
                    else:
                        self.plocha[10][5] = "*"
                    if i < (self.hod-1) and self.plocha[9][5]=="Č":
                        self.plocha[9][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[9][5] = "Č"
                        self.k = 22

                    else:
                        self.plocha[9][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[9][5] == "M" or self.k==22:
                    if self.k == 22:
                        pass
                    else:
                        self.plocha[9][5] = "*"
                    if i < (self.hod-1) and self.plocha[8][5]=="Č":
                        self.plocha[8][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[8][5] = "Č"
                        self.k = 23

                    else:
                        self.plocha[8][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[8][5] == "M" or self.k==23:
                    if self.k == 23:
                        pass
                    else:
                        self.plocha[8][5] = "*"
                    if i < (self.hod-1) and self.plocha[7][5]=="Č":
                        self.plocha[7][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][5] = "Č"
                        self.k = 24

                    else:
                        self.plocha[7][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][5] == "M" or self.k==24:
                    if self.k == 24:
                        pass
                    else:
                        self.plocha[7][5] = "*"
                    if i < (self.hod-1) and self.plocha[7][4]=="Č":
                        self.plocha[7][4] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][4] = "Č"
                        self.k = 25

                    else:
                        self.plocha[7][4] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][4] == "M" or self.k==25:
                    if self.k == 25:
                        pass
                    else:
                        self.plocha[7][4] = "*"
                    if i < (self.hod-1) and self.plocha[7][3]=="Č":
                        self.plocha[7][3] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][3] = "Č"
                        self.k = 26

                    else:
                        self.plocha[7][3] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][3] == "M" or self.k==26:
                    if self.k == 26:
                        pass
                    else:
                        self.plocha[7][3] = "*"
                    if i < (self.hod-1) and self.plocha[7][2]=="Č":
                        self.plocha[7][2] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][2] = "Č"
                        self.k = 27

                    else:
                        self.plocha[7][2] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][2] == "M" or self.k==27:
                    if self.k == 27:
                        pass
                    else:
                        self.plocha[7][2] = "*"
                    if i < (self.hod-1) and self.plocha[7][1]=="Č":
                        self.plocha[7][1] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][1] = "Č"
                        self.k = 28

                    else:
                        self.plocha[7][1] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[7][1] == "M" or self.k==28:
                    if self.k == 28:
                        pass
                    else:
                        self.plocha[7][1] = "*"
                    if i < (self.hod-1) and self.plocha[6][1]=="Č":
                        self.plocha[6][1] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[6][1] = "Č"
                        self.k = 29

                    else:
                        self.plocha[6][1] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[6][1] == "M" or self.k==29:
                    if self.k == 29:
                        pass
                    else:
                        self.plocha[6][1] = "*"
                    if i < (self.hod-1) and self.plocha[5][1]=="Č":
                        self.plocha[5][1] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][1] = "Č"
                        self.k = 30

                    else:
                        self.plocha[5][1] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][1] == "M" or self.k==30:
                    if self.k == 30:
                        pass
                    else:
                        self.plocha[5][1] = "*"
                    if i < (self.hod-1) and self.plocha[5][2]=="Č":
                        self.plocha[5][2] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][2] = "Č"
                        self.k = 31

                    else:
                        self.plocha[5][2] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][2] == "M" or self.k==31:
                    if self.k == 31:
                        pass
                    else:
                        self.plocha[5][2] = "*"
                    if i < (self.hod-1) and self.plocha[5][3]=="Č":
                        self.plocha[5][2] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][3] = "Č"
                        self.k = 32

                    else:
                        self.plocha[5][3] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][3] == "M" or self.k==32:
                    if self.k == 32:
                        pass
                    else:
                        self.plocha[5][3] = "*"
                    if i < (self.hod-1) and self.plocha[5][4]=="Č":
                        self.plocha[5][4] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][4] = "Č"
                        self.k = 33

                    else:
                        self.plocha[5][4] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None

                elif self.plocha[5][4] == "M" or self.k==33:
                    if self.k == 33:
                        pass
                    else:
                        self.plocha[5][4] = "*"
                    if i < (self.hod-1) and self.plocha[5][5]=="Č":
                        self.plocha[5][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][5] = "Č"
                        self.k = 34

                    else:
                        self.plocha[5][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[5][5] == "M" or self.k==34:
                    if self.k == 34:
                        pass
                    else:
                        self.plocha[5][5] = "*"
                    if i < (self.hod-1) and self.plocha[4][5]=="Č":
                        self.plocha[4][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[4][5] = "Č"
                        self.k = 35

                    else:
                        self.plocha[4][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[4][5] == "M" or self.k==35:
                    if self.k == 35:
                        pass
                    else:
                        self.plocha[4][5] = "*"
                    if i < (self.hod-1) and self.plocha[3][5]=="Č":
                        self.plocha[3][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[3][5] = "Č"
                        self.k = 36

                    else:
                        self.plocha[3][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[3][5] == "M" or self.k==36:
                    if self.k == 36:
                        pass
                    else:
                        self.plocha[3][5] = "*"
                    if i < (self.hod-1) and self.plocha[2][5]=="Č":
                        self.plocha[2][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[2][5] = "Č"
                        self.k = 37

                    else:
                        self.plocha[2][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[2][5] == "M" or self.k==37:
                    if self.k == 37:
                        pass
                    else:
                        self.plocha[2][5] = "*"
                    if i < (self.hod-1) and self.plocha[1][5]=="Č":
                        self.plocha[1][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[1][5] = "Č"
                        self.k = 38

                    else:
                        self.plocha[1][5] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
                elif self.plocha[1][5] == "M" or self.k==38:
                    if self.k == 38:
                        pass
                    else:
                        self.plocha[1][5] = "*"
                    if i < (self.hod-1) and self.plocha[1][6]=="Č":
                        self.plocha[1][6] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()

                    else:
                        self.plocha[1][6] = "M"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.k = None
            self.w.config(text="Aktuálne hádže: Červený")
            self.w.config(fg="Red")
            self.Console.config(state="normal")
            self.Console.delete('1.0', tkinter.END)
            self.vykresli()
            self.Console.config(state="disabled")
            self.root.update()
        else:
            self.padla = tkinter.Label(self.root, text=f"")
            self.padla.place(x=220, y=125)
            self.padla.config(text="                           ")
            self.padlo = tkinter.Label(self.root, text=f"Padlo {self.hod}")
            self.padlo.place(x=220, y=125)
            self.padlo.config(text=f"Padlo {self.hod}")
            self.root.update()
            if self.plocha[11][6] == "Č" and self.hod == 6:
                if self.plocha[10][6] == "V":
                    if self.plocha[9][6] == "Ý":
                        if self.plocha[8][6] == "H":
                            if self.plocha[7][6] == "R":
                                self.plocha[1][6] = "*"
                                self.plocha[6][6] = "A"
                                self.Console.config(state="normal")
                                self.Console.delete('1.0', tkinter.END)
                                self.vykresli()
                                self.Console.config(state="disabled")
                                self.root.update()
                                time.sleep(0.3)
                                self.vyhra("Č")
                            else:
                                self.plocha[11][6] = "*"
                                self.plocha[7][6] = "R"
                                self.Console.config(state="normal")
                                self.Console.delete('1.0', tkinter.END)
                                self.vykresli()
                                self.Console.config(state="disabled")
                                self.root.update()
                                return
                        else:
                            self.plocha[11][6] = "*"
                            self.plocha[8][6] = "H"
                            self.Console.config(state="normal")
                            self.Console.delete('1.0', tkinter.END)
                            self.vykresli()
                            self.Console.config(state="disabled")
                            self.root.update()
                            return

                    else:
                        self.plocha[11][6] = "*"
                        self.plocha[9][6] = "Ý"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        return

                else:
                    self.plocha[10][6] = "V"
                    self.plocha[11][6] = "*"
                    self.Console.config(state="normal")
                    self.Console.delete('1.0', tkinter.END)
                    self.vykresli()
                    self.Console.config(state="disabled")
                    self.root.update()
                    return

            for i in range(self.hod):
                time.sleep(0.3)
                if self.plocha[11][5] == "Č":
                    self.plocha[11][5] = "*"
                    if i < (self.hod - 1) and self.plocha[10][5] == "M":
                        self.plocha[10][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[10][5] = "M"
                        self.l = 1

                    else:
                        self.plocha[10][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None

                elif self.plocha[10][5] == "Č" or self.l == 1:
                    if self.l == 1:
                        pass
                    else:
                        self.plocha[10][5] = "*"
                    if i < (self.hod - 1) and self.plocha[9][5] == "M":
                        self.plocha[9][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[9][5] = "M"
                        self.l = 2

                    else:
                        self.plocha[9][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[9][5] == "Č" or self.l == 2:
                    if self.l == 2:
                        pass
                    else:
                        self.plocha[9][5] = "*"
                    if i < (self.hod - 1) and self.plocha[8][5] == "M":
                        self.plocha[8][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[8][5] = "M"
                        self.l = 3

                    else:
                        self.plocha[8][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[8][5] == "Č" or self.l == 3:
                    if self.l == 3:
                        pass
                    else:
                        self.plocha[8][5] = "*"
                    if i < (self.hod - 1) and self.plocha[7][5] == "M":
                        self.plocha[7][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][5] = "M"
                        self.l = 4

                    else:
                        self.plocha[7][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][5] == "Č" or self.l == 4:
                    if self.l == 4:
                        pass
                    else:
                        self.plocha[7][5] = "*"
                    if i < (self.hod - 1) and self.plocha[7][4] == "M":
                        self.plocha[7][4] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][4] = "M"
                        self.l = 5

                    else:
                        self.plocha[7][4] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                    self.root.update()
                elif self.plocha[7][4] == "Č" or self.l == 5:
                    if self.l == 5:
                        pass
                    else:
                        self.plocha[7][4] = "*"
                    if i < (self.hod - 1) and self.plocha[7][3] == "M":
                        self.plocha[7][3] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][3] = "M"
                        self.l = 6

                    else:
                        self.plocha[7][3] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][3] == "Č" or self.l == 6:
                    if self.l == 6:
                        pass
                    else:
                        self.plocha[7][3] = "*"
                    if i < (self.hod - 1) and self.plocha[7][2] == "M":
                        self.plocha[7][2] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][2] = "M"
                        self.l = 7

                    else:
                        self.plocha[7][2] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][2] == "Č" or self.l == 7:
                    if self.l == 7:
                        pass
                    else:
                        self.plocha[7][2] = "*"
                    if i < (self.hod - 1) and self.plocha[7][1] == "M":
                        self.plocha[7][1] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][1] = "M"
                        self.l = 8

                    else:
                        self.plocha[7][1] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][1] == "Č" or self.l == 8:
                    if self.l == 8:
                        pass
                    else:
                        self.plocha[7][1] = "*"
                    if i < (self.hod - 1) and self.plocha[6][1] == "M":
                        self.plocha[6][1] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[6][1] = "M"
                        self.l = 9

                    else:
                        self.plocha[6][1] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[6][1] == "Č" or self.l == 9:
                    if self.l == 9:
                        pass
                    else:
                        self.plocha[6][1] = "*"
                    if i < (self.hod - 1) and self.plocha[5][1] == "M":
                        self.plocha[5][1] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][1] = "M"

                        self.l = 10

                    else:
                        self.plocha[5][1] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][1] == "Č" or self.l == 10:
                    if self.l == 10:
                        pass
                    else:
                        self.plocha[5][1] = "*"
                    if i < (self.hod - 1) and self.plocha[5][2] == "M":
                        self.plocha[5][2] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][2] = "M"
                        self.l = 11

                    else:
                        self.plocha[5][2] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][2] == "Č" or self.l == 11:
                    if self.l == 11:
                        pass
                    else:
                        self.plocha[5][2] = "*"
                    if i < (self.hod - 1) and self.plocha[5][3] == "M":
                        self.plocha[5][3] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][3] = "M"
                        self.l = 12

                    else:
                        self.plocha[5][3] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][3] == "Č" or self.l == 12:
                    if self.l == 12:
                        pass
                    else:
                        self.plocha[5][3] = "*"
                    if i < (self.hod - 1) and self.plocha[5][4] == "M":
                        self.plocha[5][4] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][4] = "M"
                        self.l = 13

                    else:
                        self.plocha[5][4] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][4] == "Č" or self.l == 13:
                    if self.l == 13:
                        pass
                    else:
                        self.plocha[5][4] = "*"
                    if i < (self.hod - 1) and self.plocha[5][5] == "M":
                        self.plocha[5][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][5] = "M"
                        self.l = 14

                    else:
                        self.plocha[5][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                    self.root.update()
                elif self.plocha[5][5] == "Č" or self.l == 14:
                    if self.l == 14:
                        pass
                    else:
                        self.plocha[5][5] = "*"
                    if i < (self.hod - 1) and self.plocha[4][5] == "M":
                        self.plocha[4][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[4][5] = "M"
                        self.l = 15

                    else:
                        self.plocha[4][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[4][5] == "Č" or self.l == 15:
                    if self.l == 15:
                        pass
                    else:
                        self.plocha[4][5] = "*"
                    if i < (self.hod - 1) and self.plocha[3][5] == "M":
                        self.plocha[3][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[3][5] = "M"
                        self.l = 16

                    else:
                        self.plocha[3][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[3][5] == "Č" or self.l == 16:
                    if self.l == 16:
                        pass
                    else:
                        self.plocha[3][5] = "*"
                    if i < (self.hod - 1) and self.plocha[2][5] == "M":
                        self.plocha[2][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[2][5] = "M"
                        self.l = 17

                    else:
                        self.plocha[2][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[2][5] == "Č" or self.l == 17:
                    if self.l == 17:
                        pass
                    else:
                        self.plocha[2][5] = "*"
                    if i < (self.hod - 1) and self.plocha[1][5] == "M":
                        self.plocha[1][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[1][5] = "M"
                        self.l = 18

                    else:
                        self.plocha[1][5] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[1][5] == "Č" or self.l == 18:
                    if self.l == 18:
                        pass
                    else:
                        self.plocha[1][5] = "*"
                    if i < (self.hod - 1) and self.plocha[1][6] == "M":
                        self.plocha[1][6] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[1][6] = "M"
                        self.l = 19

                    else:
                        self.plocha[1][6] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[1][6] == "Č" or self.l == 19:
                    if self.l == 19:
                        pass
                    else:
                        self.plocha[1][6] = "*"
                    if i < (self.hod - 1) and self.plocha[1][7] == "M":
                        self.plocha[1][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[1][7] = "M"
                        self.l = 20

                    else:
                        self.plocha[1][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[1][7] == "Č" or self.l == 20:
                    if self.l == 20:
                        pass
                    else:
                        self.plocha[1][7] = "*"
                    if i < (self.hod - 1) and self.plocha[2][7] == "M":
                        self.plocha[2][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[2][7] = "M"
                        self.l = 21

                    else:
                        self.plocha[2][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[2][7] == "Č" or self.l == 21:
                    if self.l == 21:
                        pass
                    else:
                        self.plocha[2][7] = "*"
                    if i < (self.hod - 1) and self.plocha[3][7] == "M":
                        self.plocha[3][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[3][7] = "M"
                        self.l = 22

                    else:
                        self.plocha[3][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[3][7] == "Č" or self.l == 22:
                    if self.l == 22:
                        pass
                    else:
                        self.plocha[3][7] = "*"
                    if i < (self.hod - 1) and self.plocha[4][7] == "M":
                        self.plocha[4][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[4][7] = "M"
                        self.l = 23

                    else:
                        self.plocha[4][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[4][7] == "Č" or self.l == 23:
                    if self.l == 23:
                        pass
                    else:
                        self.plocha[4][7] = "*"
                    if i < (self.hod - 1) and self.plocha[5][7] == "M":
                        self.plocha[5][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][7] = "M"
                        self.l = 24

                    else:
                        self.plocha[5][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][7] == "Č" or self.l == 24:
                    if self.l == 24:
                        pass
                    else:
                        self.plocha[5][7] = "*"
                    if i < (self.hod - 1) and self.plocha[5][8] == "M":
                        self.plocha[5][8] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][8] = "M"
                        self.l = 25

                    else:
                        self.plocha[5][8] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][8] == "Č" or self.l == 25:
                    if self.l == 25:
                        pass
                    else:
                        self.plocha[5][8] = "*"
                    if i < (self.hod - 1) and self.plocha[5][9] == "M":
                        self.plocha[5][9] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][9] = "M"
                        self.l = 26

                    else:
                        self.plocha[5][9] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][9] == "Č" or self.l == 26:
                    if self.l == 26:
                        pass
                    else:
                        self.plocha[5][9] = "*"
                    if i < (self.hod - 1) and self.plocha[5][10] == "M":
                        self.plocha[5][10] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][10] = "M"
                        self.l = 27

                    else:
                        self.plocha[5][10] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][10] == "Č" or self.l == 27:
                    if self.l == 27:
                        pass
                    else:
                        self.plocha[5][10] = "*"
                    if i < (self.hod - 1) and self.plocha[5][11] == "M":
                        self.plocha[5][11] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[5][11] = "M"
                        self.l = 28

                    else:
                        self.plocha[5][11] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[5][11] == "Č" or self.l == 28:
                    if self.l == 28:
                        pass
                    else:
                        self.plocha[5][11] = "*"
                    if i < (self.hod - 1) and self.plocha[6][11] == "M":
                        self.plocha[6][11] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[6][11] = "M"
                        self.l = 29

                    else:
                        self.plocha[6][11] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[6][11] == "Č" or self.l == 29:
                    if self.l == 29:
                        pass
                    else:
                        self.plocha[6][11] = "*"
                    if i < (self.hod - 1) and self.plocha[7][11] == "M":
                        self.plocha[7][11] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][11] = "M"
                        self.l = 30

                    else:
                        self.plocha[7][11] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][11] == "Č" or self.l == 30:
                    if self.l == 30:
                        pass
                    else:
                        self.plocha[7][11] = "*"
                    if i < (self.hod - 1) and self.plocha[7][10] == "M":
                        self.plocha[7][10] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][10] = "M"
                        self.l = 31

                    else:
                        self.plocha[7][10] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][10] == "Č" or self.l == 31:
                    if self.l == 31:
                        pass
                    else:
                        self.plocha[7][10] = "*"
                    if i < (self.hod - 1) and self.plocha[7][9] == "M":
                        self.plocha[7][9] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][9] = "M"
                        self.l = 32

                    else:
                        self.plocha[7][9] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][9] == "Č" or self.l == 32:
                    if self.l == 32:
                        pass
                    else:
                        self.plocha[7][9] = "*"
                    if i < (self.hod - 1) and self.plocha[7][8] == "M":
                        self.plocha[7][8] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][8] = "M"
                        self.l = 33

                    else:
                        self.plocha[7][8] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None

                elif self.plocha[7][8] == "Č" or self.l == 33:
                    if self.l == 33:
                        pass
                    else:
                        self.plocha[7][8] = "*"
                    if i < (self.hod - 1) and self.plocha[7][7] == "M":
                        self.plocha[7][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[7][7] = "M"
                        self.l = 34

                    else:
                        self.plocha[7][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[7][7] == "Č" or self.l == 34:
                    if self.l == 34:
                        pass
                    else:
                        self.plocha[7][7] = "*"
                    if i < (self.hod - 1) and self.plocha[8][7] == "M":
                        self.plocha[8][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[8][7] = "M"
                        self.l = 35

                    else:
                        self.plocha[8][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[8][7] == "Č" or self.l == 35:
                    if self.l == 35:
                        pass
                    else:
                        self.plocha[8][7] = "*"
                    if i < (self.hod - 1) and self.plocha[9][7] == "M":
                        self.plocha[9][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[9][7] = "M"
                        self.l = 36

                    else:
                        self.plocha[9][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[9][7] == "Č" or self.l == 36:
                    if self.l == 36:
                        pass
                    else:
                        self.plocha[9][7] = "*"
                    if i < (self.hod - 1) and self.plocha[10][7] == "M":
                        self.plocha[10][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[10][7] = "M"
                        self.l = 37

                    else:
                        self.plocha[10][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[10][7] == "Č" or self.l == 37:
                    if self.l == 37:
                        pass
                    else:
                        self.plocha[10][7] = "*"
                    if i < (self.hod - 1) and self.plocha[11][7] == "M":
                        self.plocha[11][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.plocha[11][7] = "M"
                        self.l = 38

                    else:
                        self.plocha[11][7] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
                elif self.plocha[11][7] == "Č" or self.l == 38:
                    if self.l == 38:
                        pass
                    else:
                        self.plocha[11][7] = "*"
                    if i < (self.hod - 1) and self.plocha[11][8] == "M":
                        self.plocha[11][6] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()

                    else:
                        self.plocha[11][6] = "Č"
                        self.Console.config(state="normal")
                        self.Console.delete('1.0', tkinter.END)
                        self.vykresli()
                        self.Console.config(state="disabled")
                        self.root.update()
                        self.l = None
            self.w.config(text="Aktuálne hádže: Modrý")
            self.w.config(fg="Blue")
            self.Console.config(state="normal")
            self.Console.delete('1.0', tkinter.END)
            self.vykresli()
            self.Console.config(state="disabled")
            self.root.update()
class Manual():
    def __init__(self):
        print("""Hra je určená pre dvoch hráčov, pričom cieľom hry je dostať figúrku do domčeka. Pokiaľ sa to podarí 5x (a to skôr ako oponentovy), tak gratulujem :)
        
        Ak na hracej ploche nieje žiadna figárka, po kliknutí na tlačidlo "hoď kockou" sa v skutočnosti vykonajú 3 hody (najväčší je zobrazený) - ak to bude 6, tak
        sa panáčik ocitne na hracej ploche
        
        Panáčik môže ísť do domčeka iba v prípade, že stojí tesne predo dvermi a aj to iba v prípade, že padne číslo 6.
        
        Panáčik vyhodí oponenta za predpokladu, že skončí na jeho poziícií.
        
        Hráč môže mať v obehu iba jednu figúrku
        """)


Program()
