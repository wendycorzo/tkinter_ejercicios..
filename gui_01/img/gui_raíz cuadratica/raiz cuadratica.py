# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

from requests import delete

# --------------------
# funciones de la app
# --------------------

def sumar():
    # messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar...")
    c = int(a.get()) + int(b.get())
    t_resultados.insert(INSERT, "La suma de " + a.get() + " + " + b.get() + " casi siempre es " + str(c)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará...")
    ventana_principal.destroy()

# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Wendy vanessa vargas corzo")

# establecer tamaño a la ventana
ventana_principal.geometry("800x500")

# icono de la ventana principal
# ventana_principal.iconbitmap("colegio.ico")

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

# color de fondo de la ventana pricipal
ventana_principal.config(bg="black")

# -------------------
# variables globales
# -------------------
a = StringVar()
b = StringVar()
c = IntVar()

# ------------------
# frame entrada
# ------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=780, height=240)
frame_entrada.place(x=10,y=10)

# Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text="Colegio San José de Guanentá")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=390, y=10)

# Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text="Especialidad en Sistemas")
subtitulo.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo.place(x=390, y=40)

# Etiqueta para el subtitulo2 de la app
subtitulo2 = Label(frame_entrada, text="RAÍZ CUADRATICA")
subtitulo2.config(bg="green1", fg="black", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=390, y=70)

# imagen - logo de la app
logo = PhotoImage(file="")
logo = PhotoImage(file="")
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=10,y=10)

# etiqueta para valor a
etiq_a = Label(frame_entrada, text="a = ")
etiq_a.config(bg="pink2", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=390, y= 100)

# entry para el valor a
entry_a = Entry(frame_entrada, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=440,y=100)

# etiqueta para valor b
etiq_b = Label(frame_entrada, text="b = ")
etiq_b.config(bg="pink2", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_b.place(x=390, y= 135)

# entry para el valor b
entry_b = Entry(frame_entrada, width=4, textvariable=b)
entry_b.config(font=("Arial", 20))
entry_b.place(x=440,y=135)

# etiqueta para valor c
etiq_c = Label(frame_entrada, text="c = ")
etiq_c.config(bg="pink2", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_c.place(x=390, y= 170)

# entry para el valor c
entry_c = Entry(frame_entrada, width=4, textvariable=c)
entry_c.config(font=("Arial", 20))
entry_c.place(x=440,y=170)

# ------------------
# frame operaciones
# ------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="ivory2", width=780, height=120)
frame_operaciones.place(x=10,y=260)

# boton para sumar los números - texto
bt_sum = PhotoImage(file="")
# bt_sumar = Button(frame_operaciones, text= "Sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)

# boton para borrar entradas y resultado
bt_bor = PhotoImage(file="")
# bt_borrar = Button(frame_operaciones, text="Borrar", width=10)
bt_borrar = Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)

# boton para salir - cerrar la app
bt_sal = PhotoImage(file="")
# bt_salir = Button(frame_operaciones, text="Salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=558, y=7)

# ------------------
# frame resultados
# ------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="green", width=780, height=100)
frame_resultados.place(x=10,y=390)

# area de texto para resultados
t_resultados = Text(frame_resultados, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Courier", 20))
t_resultados.pack()

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).  Cada accion del usuario se conoce como un evento.  El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()