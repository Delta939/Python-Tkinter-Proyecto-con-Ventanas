import tkinter as tk
from tkinter import *
from tkinter import messagebox

def ingresar():
    ventana2 = tk.Toplevel(ventanaPrincipal)
    ventana2.title("Pantalla Menu")
    canvas1=tk.Canvas(ventana2,width=550, height=550)
    canvas1.configure(bg="cyan")
    canvas1.pack()

    def sin():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 1 Singleton','Singleton: limita a uno el número de instancias posibles de una clase en nuestro programa, y proporciona un acceso global al mismo')
    def af():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 2 Abstract Factory','Abstract Factory: Nos provee una interfaz que delega la creación de un conjunto de objetos relacionados sin necesidad de especificar en ningún momento cuáles son las implementaciones concretas')
    def bp():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 3 Builder Pattern','Builder: Separa la creación de un objeto complejo de su estructura, de tal forma que el mismo proceso de construcción nos puede servir para crear representaciones diferentes')
    def ap():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 4 Adapter Pattern','Adapter: Permite a dos clases con diferentes interfaces trabajar entre ellas, a través de un objeto intermedio con el que se comunican e interactúan')
    def dp():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 5 Decorator Pattern','Decorator: Permite añadir funcionalidad extra a un objeto (de forma dinámica o estática) sin modificar el comportamiento del resto de objetos del mismo tipo')
    def ip():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 6 Iterator Pattern','Iterator: Se utiliza para poder movernos por los elementos de un conjunto de forma secuencial sin necesidad de exponer su implementación específica')
    def op():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 7 Observer Pattern','Observer: Los objetos son capaces de suscribirse a una serie de eventos que otro objetivo va a emitir, y serán avisados cuando esto ocurra')
    def sp():
        #if command.label=='Singleton':
            tk.messagebox.askquestion ('Patron de Diseño 8 Strategy Pattern','Strategy: Permite la selección del algoritmo que ejecuta cierta acción en tiempo de ejecución')        
            
            
    # Crear el menu principal
    menubarra = tk.Menu(ventana2)

    # Crea un menu desplegable y lo agrega al menu barra
    menuarchivo = Menu(menubarra, tearoff=0)
    menuarchivo.add_command(label="Singleton", command=sin)
    menuarchivo.add_command(label="Abstract Factory", command=af)
    menuarchivo.add_command(label="Builder Pattern", command=bp)
    menuarchivo.add_command(label="Adapter Pattern", command=ap)
    menuarchivo.add_command(label="Decorator Pattern", command=dp)
    menuarchivo.add_command(label="Iterator Pattern", command=ip)
    menuarchivo.add_command(label="Observer Pattern", command=op)
    menuarchivo.add_command(label="Strategy Pattern", command=sp)
    menuarchivo.add_separator()
    menuarchivo.add_command(label="Salir", command=ventana2.quit)
    menubarra.add_cascade(label="Patrones de Diseño", menu=menuarchivo)
    ventana2.config(menu=menubarra)
    
    
    
    canvas1.create_window(250,160,window=button1)
    img = tk.PhotoImage(file="logo.png")
    fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=180)
    ventana2.mainloop()

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Pantalla Principal")
ventanaPrincipal.geometry('380x200')
canvas2=tk.Canvas(ventanaPrincipal,width=550, height=550)
canvas2.configure(bg="cyan")
canvas2.pack()


button1=tk.Button(ventanaPrincipal, text="Ingresar", command=ingresar,
          font=("Agency FB", 14), width=10).place(x=50, y=50)
button2=tk.Button (ventanaPrincipal, text="Grupo=GITI110",bg="yellow")
button3=tk.Button (ventanaPrincipal, text="Asignatura=Programación de aplicaciones",bg="yellow")
canvas2.create_window(250,120,window=button2)
canvas2.create_window(250,150,window=button3)
ventanaPrincipal.mainloop()
