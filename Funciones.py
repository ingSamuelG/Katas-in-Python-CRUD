from tkinter import messagebox
import sqlite3 as sql
import io




def Crear_BBDD():
	
	conexion= sql.connect("Personal")
	puntero= conexion.cursor()

	try:
		puntero.execute('''

		CREATE TABLE USUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PASSWORD VARCHAR(8),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIO VARCHAR(100)
		)

		''')

		mensaje=messagebox.showinfo("Base de datos", "La base de datos a sido creada con exito")

	except :
			alerta=messagebox.showerror("Error creando Base de datos", "La base de datos ya existe!!!!")

	conexion.close()


def Insertar(nombre, password, apellido, direccion,comentario):

	try:
		chek=io.open("Personal", "r")
		conexion= sql.connect("Personal")
		puntero=conexion.cursor()
		puntero.execute("INSERT INTO USUARIOS VALUES(null,?,?,?,?,?)", (nombre,password,apellido,direccion,comentario))
		conexion.commit()
		conexion.close()
		mensaje=messagebox.showinfo("Crear", "El usuario: " + nombre + " a sido creado")
		chek.close()


	except:
		alerta=messagebox.showerror("Crear", "La base de datos no existe!!!!, para crearla utilice el menu BBDD, ubicado en el tope izquierdo de la ventana")


def Leer(ident):

	try:
		chek=io.open("Personal", "r")
		conexion= sql.connect("Personal")
		puntero=conexion.cursor()
		puntero.execute("SELECT * FROM USUARIOS WHERE ID = :ident", {"ident": ident})
		return puntero.fetchone()
		conexion.close()
		chek.close()
		

	except FileNotFoundError:
		alerta=messagebox.showerror("Leer", "La base de datos no existe!!!!, para crearla utilice el menu BBDD, ubicado en el tope izquierdo de la ventana")
	else:
		alerta=messagebox.showerror("Leer", "El usuario con el id: " + str(ident) + "  no existe")

def Modificar(ident,nombre, password, apellido, direccion,comentario):

	 try:
	 	chek=io.open("Personal", "r")
	 	conexion= sql.connect("Personal")
	 	puntero=conexion.cursor()
	 	puntero.execute("UPDATE USUARIOS SET 'NOMBRE'=?, 'PASSWORD'=? , 'APELLIDO'=?, 'DIRECCION'=?, 'COMENTARIO'=? WHERE ID=?", (nombre,password,apellido,direccion,comentario,int(ident)))
	 	conexion.commit()
	 	conexion.close()
	 	mensaje=messagebox.showinfo("Modificar", "El usuario: " + nombre + " a sido Modificado")
	 	chek.close()

	 except:
	 	alerta=messagebox.showerror("Modificar", "La base de datos no existe!!!!, para crearla utilice el menu BBDD, ubicado en el tope izquierdo de la ventana")


def Eliminar(ident):

	 try:
		 chek=io.open("Personal", "r")
		 conexion= sql.connect("Personal")
		 puntero=conexion.cursor()
		 puntero.execute("DELETE FROM USUARIOS WHERE ID=:ident", {"ident": ident})
		 conexion.commit()
		 conexion.close()
		 mensaje=messagebox.showinfo("Eliminar", "El usuario a sido Eliminado")
		 chek.close()
		

	 except:
	 	alerta=messagebox.showerror("Eliminar", "La base de datos no existe!!!!, para crearla utilice el menu BBDD, ubicado en el tope izquierdo de la ventana")


def SalirPrograma(raiz):
	PreguntaSalida=messagebox.askquestion("Salir"," ¿Deseas salir del programa ?")
	raiz.destroy()	