from tkinter import *
from tkinter import messagebox
from Funciones import *


Raiz=Tk()
Raiz.title("CRUD")

Mimenu=Menu(Raiz)

miCanvas=Canvas(Raiz,width=450, height=500)
miCanvas.pack()

Raiz.config(menu=Mimenu)

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def Crear_registro():
	Insertar(NombreVar.get(),PassVar.get(),ApellidoVar.get(),DireccionVar.get(),Comentario.get("1.0", END))
	borrarTodo()

def Lee_Registro(ident):
	try:
		Comentario.delete("1.0", END)
		misUsuarios=Leer(ident)
		NombreVar.set(misUsuarios[1])
		PassVar.set(misUsuarios[2])
		ApellidoVar.set(misUsuarios[3])
		DireccionVar.set(misUsuarios[4])
		Comentario.insert("1.0",misUsuarios[5])
		
	except TypeError:
		messagebox.showinfo("Leer", "El Usuario que busca no se encuentra creado")
		borrarTodo()
	except IndexError:
		messagebox.showinfo("Leer", "El Usuario que busca no se encuentra creado")
		borrarTodo()

def EliminarTodo(ident):
	Eliminar(ident)
	borrarTodo()
	

def crear_etiquetas(x, y, ancho, alto, texto_label):
	Etiqueta=Label(Marco, text="{}".format(texto_label) ,bg="#353B3C", fg="white", font=("impact", 13), padx=2)
	Etiqueta.place(relx=x, rely=y, relwidth=ancho, relheight=alto)

def crear_entry(x, y, ancho, alto, texto_label, Variable, llevaPass=None):
	
	texto_label=Entry(Marco, textvariable=Variable, show=llevaPass, font=("BAUHS93", 12), justify=CENTER)
	texto_label.place(relx=x, rely=y, relwidth=ancho, relheight=alto)


def crear_botones(x, y, texto_label, func= None):
	Boton=Button(Marcoboton, text=texto_label, command=func)
	Boton.place(relx=x, rely=y, relwidth=0.2, relheight=0.5)
	

def borrarTodo():

	IDVar.set("")
	NombreVar.set("")
	PassVar.set("")
	ApellidoVar.set(""),
	DireccionVar.set("")
	Comentario.delete("1.0", END)


Imagen=PhotoImage(file="bg.png")
ImagenLabel=Label(Raiz,image=Imagen)
ImagenLabel.place(relwidth=1, relheight=1)

BBDDmenu=Menu(Mimenu, tearoff=0)
BBDDmenu.add_command(label="Conectar", command= Crear_BBDD)
BBDDmenu.add_command(label="Salir" , command=lambda:SalirPrograma(Raiz))

BorrarMenu=Menu(Mimenu, tearoff=0)
BorrarMenu.add_command(label="Borar todos los campos", command=borrarTodo)

CrudMenu=Menu(Mimenu, tearoff=0)
CrudMenu.add_command(label="Crear", command= Crear_registro)
CrudMenu.add_command(label="Leer", command=lambda:Lee_Registro(IDVar.get()))
CrudMenu.add_command(label="Actualizar",command= lambda:Modificar(IDVar.get(),NombreVar.get(),PassVar.get(),ApellidoVar.get(),DireccionVar.get(),Comentario.get("1.0", END)))
CrudMenu.add_command(label="Eliminar", command= lambda:EliminarTodo(IDVar.get()))

Mimenu.add_cascade(label="BBDD", menu=BBDDmenu)
Mimenu.add_cascade(label="Borrar", menu=BorrarMenu)
Mimenu.add_cascade(label="CRUD", menu=CrudMenu)

Marco=Frame(Raiz,bg="#353B3C",relief="groove", bd=3) #353B3C
Marco.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor="n")

Marcoboton=Frame(Marco, bg="#353B3C") #353B3C
Marcoboton.place(relx=0, rely=0.9, relwidth=1, relheight=0.1, )

IDVar=StringVar()
NombreVar=StringVar()
PassVar=StringVar()
ApellidoVar=StringVar()
DireccionVar=StringVar()


crear_etiquetas(0.05, 0.1 , 0.3, 0.05,  "ID :" )
crear_entry(0.35,0.1,0.5, 0.05, "ID:" , IDVar)

crear_etiquetas(0.05, 0.2 , 0.3, 0.05,  "Nombre :" )
crear_entry(0.35,0.2,0.5, 0.05, "Nombre:" , NombreVar)

crear_etiquetas(0.05, 0.3 , 0.3, 0.05,  "Password :" )
crear_entry(0.35,0.3,0.5, 0.05, "Password:" , PassVar, "*")

crear_etiquetas(0.05, 0.4 , 0.3, 0.05,  "Apellido :" )
crear_entry(0.35,0.4,0.5, 0.05, "Nombre:" , ApellidoVar)

crear_etiquetas(0.05, 0.5 , 0.3, 0.05,  "Direccion :" )
crear_entry(0.35,0.5,0.5, 0.05, "Direccion:" , DireccionVar)


Comentario=Text(Marco,width=30, height=5 )
Comentario.place(relx=0.35, rely=0.6, relheight=0.2, relwidth=0.5)

ScrollComent=Scrollbar(Marco, command=Comentario.yview)
ScrollComent.place(relx=0.8, rely=0.6, relheight=0.2, relwidth=0.05)


Comentario.config(yscrollcommand=ScrollComent.set)

crear_etiquetas(0.05,0.65,0.3,0.05, "Comentario: ")


crear_botones(0.05,0.30,"Create", Crear_registro)
crear_botones(0.29,0.30,"Read", lambda:Lee_Registro(IDVar.get()))
crear_botones(0.53, 0.30,"Update", lambda:Modificar(IDVar.get(),NombreVar.get(),PassVar.get(),ApellidoVar.get(),DireccionVar.get(),Comentario.get("1.0", END)))
crear_botones(0.77,0.30,"Delete", lambda:EliminarTodo(IDVar.get()))

center(Raiz)



Raiz.mainloop()
