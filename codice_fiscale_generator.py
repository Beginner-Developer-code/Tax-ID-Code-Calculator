import tkinter as tk
from tkinter import ttk
from datetime import datetime
import codice_fiscale_encode as cf

def calcola_codice_fiscale():
    nome: str = entry_nome.get().lower()
    cognome: str = entry_cognome.get().lower()
    comune: str = entry_luogo_nascita.get().lower()
    sesso: str = selected_option_sesso.get()
    giorno: str = selected_option_giorno.get()
    mese: str = selected_option_mese.get()
    anno: str = selected_option_anno.get()

    codice_cognome = cf.surname_code(cognome)
    codice_nome = cf.name_code(nome)
    codice_comune = cf.municipality_code(comune)
    codice_giorno = cf.day_code(giorno, sesso)
    codice_mese = cf.month_code(mese)
    codice_fiscale_parziale = f"{codice_cognome}{codice_nome}{anno[2:]}{codice_mese}{codice_giorno}{codice_comune}"
    carattere_di_controllo = cf.control_character(codice_fiscale_parziale)

    CODICE_FISCALE = f"{codice_cognome}{codice_nome}{anno[2:]}{codice_mese}{codice_giorno}{codice_comune}{carattere_di_controllo}"


    label_result.configure(text="")
    label_result.configure(text=f"Codice fiscale: {CODICE_FISCALE}")


screen = tk.Tk()
screen.title("Codice Fiscale")
screen.geometry("570x340")
screen.resizable(False, False)
screen.configure(bg="lightgreen")

#widgdets

title = ttk.Label(screen, text="CALCOLO CODICE FISCALE", background="lightgreen", font=("Courier New", 18, "bold"))
title.pack()

label_cognome = ttk.Label(screen,text="COGNOME", background="lightgreen", font=("Courier New", 15))
label_cognome.place(x=70,y=50)

entry_cognome = ttk.Entry(screen, justify="center", font=("Courier New", 12))
entry_cognome.pack(pady=20)

label_nome = ttk.Label(screen,text="NOME", background="lightgreen", font=("Courier New", 15))
label_nome.place(x=106,y=115)

entry_nome = ttk.Entry(screen, justify="center", font=("Courier New", 12))
entry_nome.pack(pady=20)

label_luogo_nascita = ttk.Label(screen,text="LUOGO DI NASCITA", background="lightgreen", font=("Courier New", 15))
label_luogo_nascita.place(x=35,y=180)

entry_luogo_nascita = ttk.Entry(screen, justify="center", font=("Courier New", 12))
entry_luogo_nascita.place(x=270, y=180)

label_sesso = ttk.Label(screen,text="SESSO", background="lightgreen", font=("Courier New", 15))
label_sesso.place(x=15,y=250)

selected_option_sesso = tk.StringVar()
selected_option_sesso.set('M') 

opzioni_sesso = ['M', 'F']

dropdown_sesso = ttk.OptionMenu(screen, selected_option_sesso, *opzioni_sesso)
dropdown_sesso.place(x=90, y=250)

label_data_nascita = ttk.Label(screen,text="DATA DI NASCITA", background="lightgreen", font=("Courier New", 15))
label_data_nascita.place(x=180,y=250)

selected_option_giorno = tk.StringVar()
selected_option_giorno.set('01') 

opzioni_giorno = [f"{num:02}" for num in range(0, 32)]

dropdown_giorno = ttk.OptionMenu(screen, selected_option_giorno, *opzioni_giorno)
dropdown_giorno.place(x=375, y=250)

selected_option_mese = tk.StringVar()
selected_option_mese.set('M') 

opzioni_mese = [f"{num:02}" for num in range(0, 13)]

dropdown_mese = ttk.OptionMenu(screen, selected_option_mese, *opzioni_mese)
dropdown_mese.place(x=430, y=250)

current_year = datetime.now().year
selected_option_anno = tk.StringVar()

opzioni_anno = [str(year) for year in range(1899, current_year + 1)]

dropdown_anno = ttk.OptionMenu(screen, selected_option_anno, *opzioni_anno)
dropdown_anno.place(x=485, y=250)

btn = ttk.Button(screen, text="Calcolo codice fiscale", cursor="hand2", command=calcola_codice_fiscale)
btn.place(x=20, y=300)

label_result = ttk.Label(screen, text="Codice fiscale: ", font=("Courier New",12,"bold"), background="lightgreen")
label_result.place(x=200, y=300)

screen.mainloop()