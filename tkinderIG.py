from tkinter import *
from tkinter import messagebox
from basededatos import *
ANCHO = 600
ALTO = 620
POSX = 580
POSY = 580
anchoAlto = str(ANCHO)+"x"+str(ALTO)
posicionX = "+"+str(POSX)
posicionY = "+"+str(POSY)
colorventana = "white"
colorLetra = "blue"

def mostrarMensaje(titulo, mensaje):
  messagebox.showinfo(titulo, mensaje)
  
def limpiardatos():
    nombre.set("")
    descripcion.set("")
    tipo.set("")
    cantidad.set("")
    costo.set("")
    observacion.set("")
    codigo.set("")
    text.delete(1.0, END)
    
def guardar():
    creartabla()
    if((nombre.get() == "") or (descripcion.get() == "")):
        mostrarMensaje("error","debes rellenar los datos")
    else:
        datos = nombre.get(), descripcion.get(), tipo.get(), cantidad.get(), costo.get(), observacion.get()
        mostrarMensaje("guardar","producto guardado")
        insertar(datos)
        limpiardatos()
        mostrar()

def actualizar():
    creartabla()
    if((codigo.get()== "") and (nombre.get() == "")):
        mostrarMensaje("error","debes rellenar los datos")
    else: 
        modificar(codigo.get(),nombre.get(),descripcion.get(),tipo.get(),cantidad.get(),costo.get(),observacion.get())
        mostrarMensaje("modificar", "producto modificado")
        limpiardatos()
        
def eliminar():
    if((codigo.get() == "") or (codigo.get() == 0)):
        mostrarMensaje("error","debes insertar un identificador")
    else:
        try:
         borrar(codigo.get())
         mostrarMensaje("borrar","producto eliminado")
         limpiardatos()
         mostrar()
        except:
         mostrarMensaje("error", "identificador no encontrado")

def mostrar():
    listado = consultar()
    text.delete(1.0, END)
    text.insert(INSERT, "codigo\tnombre\tdescripcion\ttipo\tcantidad\tcosto\tobservacion\n")      
    for elemento in listado:
        codigo = elemento[0]
        nombre = elemento[1]
        descripcion = elemento[2]
        tipo = elemento[3] 
        cantidad = elemento[4]
        costo = elemento[5]
        observacion = elemento[6]
        text.insert(INSERT,codigo)
        text.insert(INSERT, "\t")
        text.insert(INSERT, nombre)
        text.insert(INSERT, "\t")
        text.insert(INSERT, descripcion)
        text.insert(INSERT, "\t")
        text.insert(INSERT, tipo)
        text.insert(INSERT, "\t")
        text.insert(INSERT, cantidad)
        text.insert(INSERT, "\t")
        text.insert(INSERT, costo)
        text.insert(INSERT, "\t")
        text.insert(INSERT, observacion)
        text.insert(INSERT, "\n") 

ventana = Tk()
ventana.config(bg=colorventana)
ventana.geometry(anchoAlto+posicionX+posicionY)
ventana.title("Agenda")
frame = Frame()
frame.config(width=ANCHO, height=ALTO)
frame.config(bg="black")
frame.pack()
codigo = IntVar()
nombre = StringVar()
descripcion = StringVar()
tipo = StringVar()
cantidad = IntVar()
costo = DoubleVar()
observacion = StringVar()

etiquetacodigo = Label(frame, text="codigo: ").place(x=50, y=50)
cajacodigo= Entry(frame,textvariable=codigo).place(x=130, y=50)
etiquetanombre = Label(frame,text="nombre: ").place(x=50, y=90)
cajanombre = Entry(frame,textvariable=nombre).place(x=130, y=90)
etiquetadescripcion = Label(frame,text="descripcion: ").place(x=50, y=130)
cajadescripcion = Entry(frame,textvariable=descripcion).place(x=130, y=130)
etiquetatipo = Label(frame,text="tipo: ").place(x=50, y=170)
cajateletipo = Entry(frame,textvariable=tipo).place(x=130, y=170)
etiquetacantidad = Label(frame,text="cantidad: ").place(x=50, y=210)
cajacantidad = Entry(frame,textvariable=cantidad).place(x=130, y=210)
etiquetacosto = Label(frame,text="costo: ").place(x=50, y=240)
cajacosto = Entry(frame,textvariable=costo).place(x=130, y=240)
etiquetaobservacion = Label(frame,text="observacion: ").place(x=50, y=280)
cajaobservacion = Entry(frame,textvariable=observacion).place(x=130, y=280)



text = Text(frame)
text.place(x=50, y=340, width=500, height=250)
botonañadir = Button(frame, text="Añadir", command=guardar).place(x=150, y=540)
botonborrar = Button(frame, text="Borrar", command=eliminar).place(x=200, y=540)
botonconsultar = Button(frame, text="Consultar", command=mostrar).place(x=250, y=540)
botonmodificar = Button(frame, text="Actualizar", command=actualizar).place(x=320, y=540)
ventana.mainloop()