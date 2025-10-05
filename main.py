import tkinter as gui
from tkinter import HORIZONTAL, messagebox
import serial
import time
import numpy as np

arduino = serial.Serial("COM5", 9600)
time.sleep(2)
home_cero = 90
home_hombro = 58
home_brazo = 77
home_mano1 = 32

pos_cuerpo = np.linspace(home_cero, home_cero, num=1)
pos_hombro = np.linspace(home_hombro, home_hombro, num=1)
pos_brazo = np.linspace(home_brazo, home_brazo, num=1)
pos_mano1 = np.linspace(home_mano1, home_mano1, num=1)
pos_mano2 = np.linspace(home_cero, home_cero, num=1)
pos_mano3 = np.linspace(home_cero, home_cero, num=1)
pos_pinza = np.linspace(home_cero, home_cero, num=1)

def mov_cuerpo(a):
    a = 's1' + str(val_cuerpo.get()) + '\n'
    arduino.write(a.encode('utf-8'))

def mov_hombro(a):
    a = 's2' + str(val_hombro.get()) + '\n'
    arduino.write(a.encode('utf-8'))

def mov_brazo(a):
    a = 's3' + str(val_brazo.get()) + '\n'
    arduino.write(a.encode('utf-8'))

def mov_mano1(a):
    a = 's4' + str(val_mano1.get()) + '\n'
    arduino.write(a.encode('utf-8'))

def mov_mano2(a):
    a = 's5' + str(val_mano2.get()) + '\n'
    arduino.write(a.encode('utf-8'))

def mov_mano3(a):
    a = 's6' + str(val_mano3.get()) + '\n'
    arduino.write(a.encode('utf-8'))

def mov_pinza(a):
    a = 's7' + str(val_pinza.get()) + '\n'
    arduino.write(a.encode('utf-8'))

def guardar_pos():
    global pos_cuerpo, pos_hombro, pos_brazo, pos_mano1, pos_mano2, pos_mano3, pos_pinza
    aux = np.linspace(pos_cuerpo[-1], val_cuerpo.get(), num=10)
    pos_cuerpo = np.append(pos_cuerpo, aux)
    aux = np.linspace(pos_hombro[-1], val_hombro.get(), num=10)
    pos_hombro = np.append(pos_hombro, aux)
    aux = np.linspace(pos_brazo[-1], val_brazo.get(), num=10)
    pos_brazo = np.append(pos_brazo, aux)
    aux = np.linspace(pos_mano1[-1], val_mano1.get(), num=10)
    pos_mano1 = np.append(pos_mano1, aux)
    aux = np.linspace(pos_mano2[-1], val_mano2.get(), num=10)
    pos_mano2 = np.append(pos_mano2, aux)
    aux = np.linspace(pos_mano3[-1], val_mano3.get(), num=10)
    pos_mano3 = np.append(pos_mano3, aux)
    aux = np.linspace(pos_pinza[-1], val_pinza.get(), num=10)
    pos_pinza = np.append(pos_pinza, aux)

def trayectoria():
    for i in range(len(pos_cuerpo)):
        a = 's1' + str(pos_cuerpo[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's2' + str(pos_hombro[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's3' + str(pos_brazo[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's4' + str(pos_mano1[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's5' + str(pos_mano2[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's6' + str(pos_mano3[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's7' + str(pos_pinza[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        val_cuerpo.set(pos_cuerpo[i])
        val_hombro.set(pos_hombro[i])
        val_brazo.set(pos_brazo[i])
        val_mano1.set(pos_mano1[i])
        val_mano2.set(pos_mano2[i])
        val_mano3.set(pos_mano3[i])
        val_pinza.set(pos_pinza[i])

def home_robot():
    print('posicion a home')
    h_cuerpo = np.linspace(val_cuerpo.get(), home_cero, num=20)
    h_cuerpo=np.round(h_cuerpo, 0)
    val_cuerpo.set(home_cero)

    h_hombro = np.linspace(val_hombro.get(), home_cero, num=20)
    h_hombro=np.round(h_hombro, 0)
    val_hombro.set(home_cero)

    h_brazo = np.linspace(val_brazo.get(), home_cero, num=20)
    h_brazo=np.round(h_brazo, 0)
    val_brazo.set(home_cero)

    h_mano1 = np.linspace(val_mano1.get(), home_cero, num=20)
    h_mano1=np.round(h_mano1, 0)
    val_mano1.set(home_cero)

    h_mano2 = np.linspace(val_mano2.get(), home_cero, num=20)
    h_mano2=np.round(h_mano2, 0)
    val_mano2.set(home_cero)

    h_mano3 = np.linspace(val_mano3.get(), home_cero, num=20)
    h_mano3=np.round(h_mano3, 0)
    val_mano3.set(home_cero)

    h_pinza = np.linspace(val_pinza.get(), home_cero, num=20)
    h_pinza=np.round(h_pinza, 0)
    val_pinza.set(home_cero)

    for i in range(len(h_cuerpo)):
        a = 's1' + str(h_cuerpo[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's2' + str(h_hombro[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's3' + str(h_brazo[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's4' + str(h_mano1[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's5' + str(h_mano2[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's6' + str(h_mano3[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)
        a = 's7' + str(h_pinza[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.005)

    messagebox.showinfo('Atencion', 'Robot en posicion de home')

control = gui.Tk()
control.title("Arduino Day - Robot Antropomorfico 6GDL")
control.geometry('800x600')
control.config(cursor="hand1")
control.columnconfigure(0, weight=3)
# Img = gui.PhotoImage(file="Robot1.PNG")
# Img = img.zoom(5)
# img = img.subsample(11)

for i in range(7):
    control.rowconfigure(i, weight=1)


val_cuerpo = gui.IntVar(value=home_cero)
val_hombro = gui.IntVar(value=home_hombro)
val_brazo = gui.IntVar(value=home_brazo)
val_mano1 = gui.IntVar(value=home_mano1)
val_mano2 = gui.IntVar(value=home_cero)
val_mano3 = gui.IntVar(value=home_cero)
val_pinza = gui.IntVar(value=home_cero)


cuerpo_s = gui.Scale(control, variable=val_cuerpo, command=mov_cuerpo, to=180, orient=HORIZONTAL, length=100,
                     label='Cuerpo', font=("ProductSans",14), cursor="hand1")
hombro_s = gui.Scale(control, variable=val_hombro, command=mov_hombro, to=180, orient=HORIZONTAL, length=100,
                     label='Hombro', font=("ProductSans",14))
brazo_s = gui.Scale(control, variable=val_brazo, command=mov_brazo, to=180, orient=HORIZONTAL, length=100,
                     label='Brazo', font=("ProductSans",14))
mano1_s = gui.Scale(control, variable=val_mano1, command=mov_mano1, to=180, orient=HORIZONTAL, length=100,
                     label='Roll: Alabeo', font=("ProductSans",14))
mano2_s = gui.Scale(control, variable=val_mano2, command=mov_mano2, to=180, orient=HORIZONTAL, length=100,
                     label='Pitch: Elevacion', font=("ProductSans",14))
mano3_s = gui.Scale(control, variable=val_mano3, command=mov_mano3, to=180, orient=HORIZONTAL, length=100,
                     label='Yaw: Cabeceo', font=("ProductSans",14))
pinza_s = gui.Scale(control, variable=val_pinza, command=mov_pinza, to=180, orient=HORIZONTAL, length=100,
                     label='Herramienta', font=("ProductSans",14))

btn_guardar = gui.Button(text="Guardar Posicion", command=guardar_pos, pady=1, width=20, bg="#1E90ff", bd=5, height=2, 
                         relief="raised", borderwidth=5, font=("productSans", 14), cursor="plus")
btn_run = gui.Button(text="Ejecutar", command=trayectoria, pady=1, width=20, bg="green", bd=5, height=2, 
                         relief="raised", borderwidth=5, font=("productSans", 14), cursor="exchange")
btn_home = gui.Button(text="ir a home", command=home_robot, pady=1, width=20, bg="#FFA500", bd=5, height=2, 
                         relief="raised", borderwidth=5, font=("productSans", 14), cursor="heart")

cuerpo_s.grid(row=0, column=0, sticky="nsew")
hombro_s.grid(row=1, column=0, sticky="nsew")
brazo_s.grid(row=2, column=0, sticky="nsew")
mano1_s.grid(row=3, column=0, sticky="nsew")
mano2_s.grid(row=4, column=0, sticky="nsew")
mano3_s.grid(row=5, column=0, sticky="nsew")
pinza_s.grid(row=6, column=0, sticky="nsew")

btn_guardar.grid(row=4, column=1, sticky="nsew")
btn_run.grid(row=5, column=1, sticky="nsew")
btn_home.grid(row=6, column=1, sticky="nsew")

#fondo = gui.Label(control, image=img).grid(row=0, column=1, sticky="nsew", rowspan=4)
fondo = gui.Label(control).grid(row=0, column=1, sticky="nsew", rowspan=4)

# run TK event loop

control.mainloop()
