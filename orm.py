import tkinter as tk
import random
import math
import json

personas = []
numeropersonas = 5
class Persona:
    def __init__(self):
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,1024)
        self.radio = 30
        self.direccion = random.randint(0,360)
        self.color = "blue"
        self.entidad = ""
    def dibuja(self):
        self.entidad = lienzo.create_oval(self.posx-self.radio/2,self.posy-self.radio/2,self.posx+self.radio/2,self.posy+self.radio/2,fill=self.color)
    def mueve(self):
        self.colisiona()
        lienzo.move(self.entidad,math.cos(self.direccion),math.sin(self.direccion))
        self.posx +=  math.cos(self.direccion)
        self.posy +=  math.sin(self.direccion)
    def colisiona(self):
        if self.posx < 0 or self.posx > 1024 or self.posy < 0 or self.posy > 1024:
            self.direccion += math.pi

def guardarPersonas():
     print("Guardo a los jugadores")
     cadena = json.dumps([vars(persona) for persona in personas])
     print(cadena)
     archivo = open("jugadores.json",'w')
     archivo.write(cadena)
     
#Creo una ventana
raiz = tk.Tk()

#Boton de guardar
boton = tk.Button(raiz,text="Guarda",command=guardarPersonas)
boton.pack()

#En la ventana creo un lienzo
lienzo = tk.Canvas(raiz,width=1024,height=1024)
lienzo.pack()

#Cargar personas desde le disco duro
try:
    carga = open("jugadores.json",'r')
    cargado = carga.read()
    cargadolista = json.loads(cargado)
    for elemento in cargadolista:
        persona = Persona()
        persona.__dict__.update(elemento)
        personas.append(persona)
except:
    print("Error")

#En la coleccion introduzco instancias de personas
if len(personas) == 0:
    numeropersonas = 1
    for i in range(0,numeropersonas):
        personas.append(Persona())
    
#Para cada una de las personas en la coleccion las pinto 
for persona in personas:
    persona.dibuja()
    
#Creo un bucle repetitivo
def bucle():
    #Para cada persona en la coleccion
    for persona in personas:
        persona.mueve()
    raiz.after(10,bucle)
    
#Ejecuto el bucle
bucle()
raiz.mainloop()
