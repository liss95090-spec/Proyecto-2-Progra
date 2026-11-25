import tkinter as tk



ventana = tk.Tk()
ventana.title("Proyecto Sanbox")
ventana.minsize(1000,667)
ventana.resizable(width="NO", height="NO")

aire=0
arena=1 
agua=2
piedra=3
tierra=4
fuego=5
semilla=6
pasto=7 #se genera por interaccion de agua y tierra no se puede seleccionar manualmente
planta_etapa1=8
planta_etapa2=9
planta_etapa3=10
animal=11

Plantas= (planta_etapa1,planta_etapa2,planta_etapa3)






ventana.mainloop()