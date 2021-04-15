from tkinter import *
import numpy as np
window = Tk()

#Config Ventana
window.title("Calculadora Vectores")
window.geometry('400x300')
window.config(bg="lightblue")

#Ventanas-Funciones
def InterfazOpVectores():
    def v2D():
        frame_3d.grid_remove()
        frame_2d.grid()
        def suma2d():
            Vx1 = x1.get()
            Vy1 = y1.get()
            Vx2 = x2.get()
            Vy2 = y2.get()
            a = np.array([int(Vx1),int(Vy1)])
            b = np.array([int(Vx2),int(Vy2)])
            rSuma2d = a+b
            lrx.configure(text=rSuma2d[0])
            lry.configure(text=rSuma2d[1])
        def resta2d():
            Vx1 = x1.get()
            Vy1 = y1.get()
            Vx2 = x2.get()
            Vy2 = y2.get()
            a = np.array([int(Vx1),int(Vy1)])
            b = np.array([int(Vx2),int(Vy2)])
            rSuma2d = a-b
            lrx.configure(text=rSuma2d[0])
            lry.configure(text=rSuma2d[1])
        def borrar2d():
            x1.delete(0, END)
            y1.delete(0, END)
            x2.delete(0, END)
            y2.delete(0, END)

        Label(frame_2d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=1,column=0)
        Label(frame_2d,text="x1",bg="lightblue",font=("Arial",12)).grid(row=1,column=1)
        x1 = Entry(frame_2d,width=5)
        x1.grid(row=1,column=2)

        Label(frame_2d,text="y1",bg="lightblue",font=("Arial",12)).grid(row=1,column=3)
        y1 = Entry(frame_2d,width=5)
        y1.grid(row=1,column=4)

        Label(frame_2d,text="B->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_2d,text="x2",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        x2 = Entry(frame_2d,width=5)
        x2.grid(row=2,column=2)

        Label(frame_2d,text="y2",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        y2 = Entry(frame_2d,width=5)
        y2.grid(row=2,column=4)

        Label(frame_2d,text="AB->",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        Label(frame_2d,text="x",bg="lightblue",font=("Arial",12)).grid(row=3,column=1)
        lrx = Label(frame_2d,text="-",bg="lightblue",font=("Arial",12))
        lrx.grid(row=3,column=2)

        Label(frame_2d,text="y",bg="lightblue",font=("Arial",12)).grid(row=3,column=3)
        lry = Label(frame_2d,text="-",bg="lightblue",font=("Arial",12))
        lry.grid(row=3,column=4)

        suma2d = Button(frame_2d,text="+",activebackground="#38EB5C", bg="#FEEF06",font=("Arial",12),width=3,command=suma2d).grid(row=4,column=0)
        resta2d = Button(frame_2d,text="-", activebackground="#38EB5C",bg="#FEEF06",font=("Arial",12),width=3,command=resta2d).grid(row=5,column=0)
        delete2d = Button(frame_2d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar2d).grid(row=4,column=1,columnspan=2)
    def v3D():
        frame_2d.grid_remove()
        frame_3d.grid()
        def suma3d():
            Vx1 = d3_x1.get()
            Vy1 = d3_y1.get()
            Vz1 = d3_z1.get()
            Vx2 = d3_x2.get()
            Vy2 = d3_y2.get()
            Vz2 = d3_z2.get()
            a = np.array([int(Vx1),int(Vy1),int(Vz1)])
            b = np.array([int(Vx2),int(Vy2),int(Vz2)])
            rSuma3d = a+b
            d3_lrx.configure(text=rSuma3d[0])
            d3_lry.configure(text=rSuma3d[1])
            d3_lrz.configure(text=rSuma3d[2])
        def resta3d():
            Vx1 = d3_x1.get()
            Vy1 = d3_y1.get()
            Vz1 = d3_z1.get()
            Vx2 = d3_x2.get()
            Vy2 = d3_y2.get()
            Vz2 = d3_z2.get()
            a = np.array([int(Vx1),int(Vy1),int(Vz1)])
            b = np.array([int(Vx2),int(Vy2),int(Vz2)])
            rSuma3d = a-b
            d3_lrx.configure(text=rSuma3d[0])
            d3_lry.configure(text=rSuma3d[1])
            d3_lrz.configure(text=rSuma3d[2])
        def borrar3d():
            d3_x1.delete(0, END)
            d3_y1.delete(0, END)
            d3_z1.delete(0, END)
            d3_x2.delete(0, END)
            d3_y2.delete(0, END)
            d3_z2.delete(0, END)

        Label(frame_3d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=1,column=0)
        Label(frame_3d,text="x1",bg="lightblue",font=("Arial",12)).grid(row=1,column=1)
        d3_x1 = Entry(frame_3d,width=5)
        d3_x1.grid(row=1,column=2)

        Label(frame_3d,text="y1",bg="lightblue",font=("Arial",12)).grid(row=1,column=3)
        d3_y1 = Entry(frame_3d,width=5)
        d3_y1.grid(row=1,column=4)

        Label(frame_3d,text="z1",bg="lightblue",font=("Arial",12)).grid(row=1,column=5)
        d3_z1 = Entry(frame_3d,width=5)
        d3_z1.grid(row=1,column=6)

        Label(frame_3d,text="B->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_3d,text="x2",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        d3_x2 = Entry(frame_3d,width=5)
        d3_x2.grid(row=2,column=2)

        Label(frame_3d,text="y2",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        d3_y2 = Entry(frame_3d,width=5)
        d3_y2.grid(row=2,column=4)

        Label(frame_3d,text="z2",bg="lightblue",font=("Arial",12)).grid(row=2,column=5)
        d3_z2 = Entry(frame_3d,width=5)
        d3_z2.grid(row=2,column=6)

        Label(frame_3d,text="AB->",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        Label(frame_3d,text="x",bg="lightblue",font=("Arial",12)).grid(row=3,column=1)
        d3_lrx = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_lrx.grid(row=3,column=2)

        Label(frame_3d,text="y",bg="lightblue",font=("Arial",12)).grid(row=3,column=3)
        d3_lry = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_lry.grid(row=3,column=4)

        Label(frame_3d,text="z",bg="lightblue",font=("Arial",12)).grid(row=3,column=5)
        d3_lrz = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_lrz.grid(row=3,column=6)

        suma3d = Button(frame_3d,text="+",activebackground="#38EB5C", bg="#FEEF06",font=("Arial",12),width=3,command=suma3d).grid(row=4,column=0)
        resta3d = Button(frame_3d,text="-", activebackground="#38EB5C",bg="#FEEF06",font=("Arial",12),width=3,command=resta3d).grid(row=5,column=0)
        delete3d = Button(frame_3d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar3d).grid(row=4,column=1,columnspan=2)


    Sventana = Toplevel(window)
    Sventana.title("Operaciones con Vectores")
    Sventana.geometry('360x300')
    Sventana.config(bg="lightblue")
    tituloS = Label(Sventana,text="Operaciones con Vectores")
    tituloS.grid(row=0,column=0,columnspan=2)
    tituloS.config(fg="Black",font=("Arial",12),bg="lightblue")
    tipo2x2 = Button(Sventana,text="Vectores 2D",activebackground="#F50743", bg="#38EB5C", command=v2D)
    tipo2x2.grid(row=1,column=0)
    tipo3x3 = Button(Sventana,text="Vectores 3D",activebackground="#F50743", bg="#38EB5C", command=v3D)
    tipo3x3.grid(row=1,column=1)

    frame_2d = Frame(Sventana)
    frame_2d.grid(row=2,column=0,pady=10)
    frame_2d.config(bg="lightblue")

    frame_3d = Frame(Sventana)
    frame_3d.grid(row=2,column=0,pady=10)
    frame_3d.config(bg="lightblue")

def VectorporEscalar():
    def v2D():
        frame_3d.grid_remove()
        frame_2d.grid()
        def multi2d():
            vX = x.get()
            vY = y.get()
            vEsc = Esc.get()
            Escalar = int(vEsc)
            a = np.array([int(vX),int(vY)])
            resultado2d = a*Escalar
            d2_x.configure(text=resultado2d[0])
            d2_y.configure(text=resultado2d[1])
        def borrar2d():
            x.delete(0, END)
            y.delete(0, END)
            Esc.delete(0, END)
        Label(frame_2d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_2d,text="x",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        x = Entry(frame_2d,width=5)
        x.grid(row=2,column=2)

        Label(frame_2d,text="y",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        y = Entry(frame_2d,width=5)
        y.grid(row=2,column=4)

        Label(frame_2d,text="|",bg="lightblue",font=("Arial",12)).grid(row=2,column=5)
        Label(frame_2d,text="Escalar:",bg="lightblue",font=("Arial",12)).grid(row=2,column=6)
        Esc = Entry(frame_2d,width=5)
        Esc.grid(row=2,column=7)

        Label(frame_2d,text="A=",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        Label(frame_2d,text="x",bg="lightblue",font=("Arial",12)).grid(row=3,column=1)
        d2_x = Label(frame_2d,text="-",bg="lightblue",font=("Arial",12))
        d2_x.grid(row=3,column=2)
        Label(frame_2d,text="y",bg="lightblue",font=("Arial",12)).grid(row=3,column=3)
        d2_y = Label(frame_2d,text="-",bg="lightblue",font=("Arial",12))
        d2_y.grid(row=3,column=4)
        d2_Calcular = Button(frame_2d,text="=",activebackground="#38EB5C", bg="#FEEF06",width=5,command=multi2d).grid(row=4,column=0,columnspan=2)
        d2_Borrar = Button(frame_2d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar2d).grid(row=4,column=2,columnspan=2)

    def v3D():
        frame_2d.grid_remove()
        frame_3d.grid()
        def multi3d():
            vX = d3_x.get()
            vY = d3_y.get()
            vZ = d3_z.get()
            vEsc = d3_Esc.get()
            Escalar = int(vEsc)
            a = np.array([int(vX),int(vY),int(vZ)])
            resultado3d = a*Escalar
            d3_Rx.configure(text=resultado3d[0])
            d3_Ry.configure(text=resultado3d[1])
            d3_Rz.configure(text=resultado3d[2])
        def borrar3d():
            d3_x.delete(0, END)
            d3_y.delete(0, END)
            d3_z.delete(0, END)
            d3_Esc.delete(0, END)
        
        Label(frame_3d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_3d,text="x",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        d3_x = Entry(frame_3d,width=5)
        d3_x.grid(row=2,column=2)

        Label(frame_3d,text="y",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        d3_y = Entry(frame_3d,width=5)
        d3_y.grid(row=2,column=4)

        Label(frame_3d,text="z",bg="lightblue",font=("Arial",12)).grid(row=2,column=5)
        d3_z = Entry(frame_3d,width=5)
        d3_z.grid(row=2,column=6)

        Label(frame_3d,text="|",bg="lightblue",font=("Arial",12)).grid(row=2,column=7)
        Label(frame_3d,text="Escalar:",bg="lightblue",font=("Arial",12)).grid(row=2,column=8)
        d3_Esc = Entry(frame_3d,width=5)
        d3_Esc.grid(row=2,column=9)

        Label(frame_3d,text="A=",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        Label(frame_3d,text="x",bg="lightblue",font=("Arial",12)).grid(row=3,column=1)
        d3_Rx = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_Rx.grid(row=3,column=2)

        Label(frame_3d,text="y",bg="lightblue",font=("Arial",12)).grid(row=3,column=3)
        d3_Ry = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_Ry.grid(row=3,column=4)

        Label(frame_3d,text="z",bg="lightblue",font=("Arial",12)).grid(row=3,column=5)
        d3_Rz = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_Rz.grid(row=3,column=6)

        d3_Calcular = Button(frame_3d,text="=",activebackground="#38EB5C", bg="#FEEF06",width=5,command=multi3d).grid(row=4,column=0,columnspan=2)
        d3_Borrar = Button(frame_3d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar3d).grid(row=4,column=2,columnspan=2)

    Escaventana = Toplevel(window)
    Escaventana.title("Vector por Escalar")
    Escaventana.geometry('360x300')
    Escaventana.config(bg="lightblue")
    tituloEscalar = Label(Escaventana,text="Vector por Escalar")
    tituloEscalar.grid(row=0,column=0,columnspan=8)
    tituloEscalar.config(fg="Black",font=("Arial",12),bg="lightblue")
    tipo2x2 = Button(Escaventana,text="Vectores 2D",activebackground="#F50743", bg="#38EB5C",command=v2D)
    tipo2x2.grid(row=1,column=0)
    tipo3x3 = Button(Escaventana,text="Vectores 3D",activebackground="#F50743", bg="#38EB5C",command=v3D)
    tipo3x3.grid(row=1,column=1)

    frame_2d = Frame(Escaventana)
    frame_2d.grid(row=2,column=0,pady=10)
    frame_2d.config(bg="lightblue")

    frame_3d = Frame(Escaventana)
    frame_3d.grid(row=2,column=0,pady=10)
    frame_3d.config(bg="lightblue")

def ProductoPunto():
    def v2D():
        frame_3d.grid_remove()
        frame_2d.grid()
        def Producto2d():
            Vx1 = x1.get()
            Vy1 = y1.get()
            Vx2 = x2.get()
            Vy2 = y2.get()
            a = np.array([int(Vx1),int(Vy1)])
            b = np.array([int(Vx2),int(Vy2)])
            r2d = a.dot(b)
            lrx.configure(text=r2d)
        def borrar2d():
            x1.delete(0, END)
            y1.delete(0, END)
            x2.delete(0, END)
            y2.delete(0, END)

        Label(frame_2d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=1,column=0)
        Label(frame_2d,text="x1",bg="lightblue",font=("Arial",12)).grid(row=1,column=1)
        x1 = Entry(frame_2d,width=5)
        x1.grid(row=1,column=2)

        Label(frame_2d,text="y1",bg="lightblue",font=("Arial",12)).grid(row=1,column=3)
        y1 = Entry(frame_2d,width=5)
        y1.grid(row=1,column=4)

        Label(frame_2d,text="B->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_2d,text="x2",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        x2 = Entry(frame_2d,width=5)
        x2.grid(row=2,column=2)

        Label(frame_2d,text="y2",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        y2 = Entry(frame_2d,width=5)
        y2.grid(row=2,column=4)

        Label(frame_2d,text="AB->",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        lrx = Label(frame_2d,text="-",bg="lightblue",font=("Arial",12))
        lrx.grid(row=3,column=2)

        calcular_2d = Button(frame_2d,text="=",activebackground="#38EB5C", bg="#FEEF06",width=5,command=Producto2d).grid(row=4,column=0,columnspan=2)
        delete2d = Button(frame_2d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar2d).grid(row=4,column=2,columnspan=2)
    def v3D():
        frame_2d.grid_remove()
        frame_3d.grid()
        def Producto3d():
            Vx1 = d3_x1.get()
            Vy1 = d3_y1.get()
            Vz1 = d3_z1.get()
            Vx2 = d3_x2.get()
            Vy2 = d3_y2.get()
            Vz2 = d3_z2.get()
            a = np.array([int(Vx1),int(Vy1),int(Vz1)])
            b = np.array([int(Vx2),int(Vy2),int(Vz2)])
            r3d = a.dot(b)
            d3_lrx.configure(text=r3d)
        def borrar3d():
            d3_x1.delete(0, END)
            d3_y1.delete(0, END)
            d3_z1.delete(0, END)
            d3_x2.delete(0, END)
            d3_y2.delete(0, END)
            d3_z2.delete(0, END)

        Label(frame_3d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=1,column=0)
        Label(frame_3d,text="x1",bg="lightblue",font=("Arial",12)).grid(row=1,column=1)
        d3_x1 = Entry(frame_3d,width=5)
        d3_x1.grid(row=1,column=2)

        Label(frame_3d,text="y1",bg="lightblue",font=("Arial",12)).grid(row=1,column=3)
        d3_y1 = Entry(frame_3d,width=5)
        d3_y1.grid(row=1,column=4)

        Label(frame_3d,text="z1",bg="lightblue",font=("Arial",12)).grid(row=1,column=5)
        d3_z1 = Entry(frame_3d,width=5)
        d3_z1.grid(row=1,column=6)

        Label(frame_3d,text="B->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_3d,text="x2",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        d3_x2 = Entry(frame_3d,width=5)
        d3_x2.grid(row=2,column=2)

        Label(frame_3d,text="y2",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        d3_y2 = Entry(frame_3d,width=5)
        d3_y2.grid(row=2,column=4)

        Label(frame_3d,text="z2",bg="lightblue",font=("Arial",12)).grid(row=2,column=5)
        d3_z2 = Entry(frame_3d,width=5)
        d3_z2.grid(row=2,column=6)

        Label(frame_3d,text="AB->",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        d3_lrx = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_lrx.grid(row=3,column=2)

        calcular_3d = Button(frame_3d,text="=",activebackground="#38EB5C", bg="#FEEF06",width=5,command=Producto3d).grid(row=4,column=0)
        delete3d = Button(frame_3d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar3d).grid(row=4,column=1,columnspan=2)

    ventanaProducto = Toplevel(window)
    ventanaProducto.title("Producto Punto")
    ventanaProducto.geometry('360x300')
    ventanaProducto.config(bg="lightblue")
    tituloS = Label(ventanaProducto,text="Producto Punto")
    tituloS.grid(row=0,column=0,columnspan=2)
    tituloS.config(fg="Black",font=("Arial",12),bg="lightblue")
    tipo2x2 = Button(ventanaProducto,text="Vectores 2D",activebackground="#F50743", bg="#38EB5C", command=v2D)
    tipo2x2.grid(row=1,column=0)
    tipo3x3 = Button(ventanaProducto,text="Vectores 3D",activebackground="#F50743", bg="#38EB5C", command=v3D)
    tipo3x3.grid(row=1,column=1)

    frame_2d = Frame(ventanaProducto)
    frame_2d.grid(row=2,column=0,pady=10)
    frame_2d.config(bg="lightblue")

    frame_3d = Frame(ventanaProducto)
    frame_3d.grid(row=2,column=0,pady=10)
    frame_3d.config(bg="lightblue")

def ProductoCruz():
    def v2D():
        frame_3d.grid_remove()
        frame_2d.grid()
        def cruz2d():
            Vx1 = x1.get()
            Vy1 = y1.get()
            Vx2 = x2.get()
            Vy2 = y2.get()
            a = np.array([int(Vx1),int(Vy1)])
            b = np.array([int(Vx2),int(Vy2)])
            r2d = np.cross(a,b)
            lrx.configure(text=r2d)
        def borrar2d():
            x1.delete(0, END)
            y1.delete(0, END)
            x2.delete(0, END)
            y2.delete(0, END)

        Label(frame_2d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=1,column=0)
        Label(frame_2d,text="x1",bg="lightblue",font=("Arial",12)).grid(row=1,column=1)
        x1 = Entry(frame_2d,width=5)
        x1.grid(row=1,column=2)

        Label(frame_2d,text="y1",bg="lightblue",font=("Arial",12)).grid(row=1,column=3)
        y1 = Entry(frame_2d,width=5)
        y1.grid(row=1,column=4)

        Label(frame_2d,text="B->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_2d,text="x2",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        x2 = Entry(frame_2d,width=5)
        x2.grid(row=2,column=2)

        Label(frame_2d,text="y2",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        y2 = Entry(frame_2d,width=5)
        y2.grid(row=2,column=4)

        Label(frame_2d,text="AB->",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        lrx = Label(frame_2d,text="-",bg="lightblue",font=("Arial",12))
        lrx.grid(row=3,column=1)

        calcular2d = Button(frame_2d,text="=",activebackground="#38EB5C", bg="#FEEF06",width=5,command=cruz2d).grid(row=4,column=0)
        delete2d = Button(frame_2d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar2d).grid(row=4,column=1,columnspan=2)
    def v3D():
        frame_2d.grid_remove()
        frame_3d.grid()
        def cruz3d():
            Vx1 = d3_x1.get()
            Vy1 = d3_y1.get()
            Vz1 = d3_z1.get()
            Vx2 = d3_x2.get()
            Vy2 = d3_y2.get()
            Vz2 = d3_z2.get()
            a = np.array([int(Vx1),int(Vy1),int(Vz1)])
            b = np.array([int(Vx2),int(Vy2),int(Vz2)])
            r3d = np.cross(a,b)
            d3_lrx.configure(text=r3d[0])
            d3_lry.configure(text=r3d[1])
            d3_lrz.configure(text=r3d[2])
        def borrar3d():
            d3_x1.delete(0, END)
            d3_y1.delete(0, END)
            d3_z1.delete(0, END)
            d3_x2.delete(0, END)
            d3_y2.delete(0, END)
            d3_z2.delete(0, END)

        Label(frame_3d,text="A->",bg="lightblue",font=("Arial",12)).grid(row=1,column=0)
        Label(frame_3d,text="x1",bg="lightblue",font=("Arial",12)).grid(row=1,column=1)
        d3_x1 = Entry(frame_3d,width=5)
        d3_x1.grid(row=1,column=2)

        Label(frame_3d,text="y1",bg="lightblue",font=("Arial",12)).grid(row=1,column=3)
        d3_y1 = Entry(frame_3d,width=5)
        d3_y1.grid(row=1,column=4)

        Label(frame_3d,text="z1",bg="lightblue",font=("Arial",12)).grid(row=1,column=5)
        d3_z1 = Entry(frame_3d,width=5)
        d3_z1.grid(row=1,column=6)

        Label(frame_3d,text="B->",bg="lightblue",font=("Arial",12)).grid(row=2,column=0)
        Label(frame_3d,text="x2",bg="lightblue",font=("Arial",12)).grid(row=2,column=1)
        d3_x2 = Entry(frame_3d,width=5)
        d3_x2.grid(row=2,column=2)

        Label(frame_3d,text="y2",bg="lightblue",font=("Arial",12)).grid(row=2,column=3)
        d3_y2 = Entry(frame_3d,width=5)
        d3_y2.grid(row=2,column=4)

        Label(frame_3d,text="z2",bg="lightblue",font=("Arial",12)).grid(row=2,column=5)
        d3_z2 = Entry(frame_3d,width=5)
        d3_z2.grid(row=2,column=6)

        Label(frame_3d,text="AB->",bg="lightblue",font=("Arial",12)).grid(row=3,column=0)
        Label(frame_3d,text="x",bg="lightblue",font=("Arial",12)).grid(row=3,column=1)
        d3_lrx = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_lrx.grid(row=3,column=2)

        Label(frame_3d,text="y",bg="lightblue",font=("Arial",12)).grid(row=3,column=3)
        d3_lry = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_lry.grid(row=3,column=4)

        Label(frame_3d,text="z",bg="lightblue",font=("Arial",12)).grid(row=3,column=5)
        d3_lrz = Label(frame_3d,text="-",bg="lightblue",font=("Arial",12))
        d3_lrz.grid(row=3,column=6)

        calcular3d = Button(frame_3d,text="=",activebackground="#38EB5C", bg="#FEEF06",width=5,command=cruz3d).grid(row=4,column=0)
        delete3d = Button(frame_3d,text="Borrar",activebackground="#38EB5C", bg="#F50743",width=5,command=borrar3d).grid(row=4,column=1,columnspan=2)

    Sventana = Toplevel(window)
    Sventana.title("Producto Cruz")
    Sventana.geometry('360x300')
    Sventana.config(bg="lightblue")
    tituloS = Label(Sventana,text="Producto Cruz")
    tituloS.grid(row=0,column=0,columnspan=2)
    tituloS.config(fg="Black",font=("Arial",12),bg="lightblue")
    tipo2x2 = Button(Sventana,text="Vectores 2D",activebackground="#F50743", bg="#38EB5C", command=v2D)
    tipo2x2.grid(row=1,column=0)
    tipo3x3 = Button(Sventana,text="Vectores 3D",activebackground="#F50743", bg="#38EB5C", command=v3D)
    tipo3x3.grid(row=1,column=1)

    frame_2d = Frame(Sventana)
    frame_2d.grid(row=2,column=0,pady=10)
    frame_2d.config(bg="lightblue")

    frame_3d = Frame(Sventana)
    frame_3d.grid(row=2,column=0,pady=10)
    frame_3d.config(bg="lightblue")

#Función Seleccionar
opcion = IntVar()
def seleccionar():
    import numpy as np
    monitor.config(text="opcion {}".format(opcion.get()))
    selec = int(opcion.get())
    if selec == 1:
        InterfazOpVectores()
    elif selec == 2:
        VectorporEscalar()
    elif selec == 3:
        ProductoPunto()
    elif selec == 4:
        ProductoCruz()


#Interfaz Bienvenida
Bienvenida = Label(window,text="Bienvenido, elige una opción para trabajar con Vectores")
Bienvenida.grid(row=0,column=0)
Bienvenida.config(fg="Black",font=("Arial",12),bg="lightblue")
Radiobutton(window,text="Operaciones con Vectores",variable=opcion,value=1,command=seleccionar,font=("Arial,12"),bg="lightblue").grid(row=1,column=0)
Radiobutton(window,text="Vector por Escalar",variable=opcion,value=2,command=seleccionar,font=("Arial,12"),bg="lightblue").grid(row=2,column=0)
Radiobutton(window,text="Producto Punto",variable=opcion,value=3,command=seleccionar,font=("Arial,12"),bg="lightblue").grid(row=3,column=0)
Radiobutton(window,text="Producto Cruz",variable=opcion,value=4,command=seleccionar,font=("Arial,12"),bg="lightblue").grid(row=4,column=0)
monitor = Label(window)
monitor.grid(row=5,column=0)
monitor.config(fg="Black",font=("Arial",12),bg="lightblue")
window.mainloop()