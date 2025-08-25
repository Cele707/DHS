print ("Hola Mundo\n")

nros = list(range(5, 15))

# Lista vacía
lista_vacia = []

# Lista con elementos
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")  # Agregar un elemento al final
frutas.remove("banana")    # Eliminar un elemento específico
frutas[0] = "kiwi"        # Modificar un elemento por índice                                                
for fruta in frutas:
    print(fruta)
    
palabra = "Por que Ineffa?"
for letra in list(range(len(palabra)-1, -1, -1)):
    print(palabra[letra])    
    
name = "Peter"
age = 25
palabra2 = f"Mi nombre es {name} y tengo {age} años"

print(palabra2)


print("\n" + palabra)

print("\n" + palabra[::-1])       

palabra1 = "Por que Ineffa?"
palabra2 = palabra1.split(" ")
cadena_unida = " ".join(palabra2)
print(cadena_unida)  


for palabra in palabra2:
        print(palabra)
        



texto = "  Hola mundo  "
texto_sin_espacios = texto.strip()
print(texto_sin_espacios)  # Output: "Hola mundo"


#Ejemplo de función 
def cuadrado(x):
    return x ** 2

#Clase
class Persona:
    def __init__(self, nombre, edad): #constructor, inicializa los atributos
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
  
    def __str__(self): #toString
       return f"\nNombre={self.nombre}\nEdad={self.edad}"
    
# Crear una instancia de la clase Persona
persona1 = Persona("Pedro", 30)
# Llamar al método presentarse
print(persona1)

#Conjunto
conjunto = set([1, 2, 3, 4, 5])
conjunto1 = {6, 7, 8, 9, 10}
conjunto & conjunto1  # Intersección
conjunto | conjunto1  # Unión
conjunto ^ conjunto1  # Diferencia simétrica

#Diccionario
diccionario = {"a" : 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

print(diccionario["a"])  # Acceder a un valor por su clave
print(diccionario.get("b"))  # Otra forma de acceder a un valor

#Archivos
with open("archivo.txt", "w") as archivo:
    archivo.write("Brant el mejor B)\n")  # Escribir en el archivo
   
   
with open("archivo.txt", "r") as archivo:
    contenido = archivo.readlines() #Leer todas las líneas del archiv
    for linea in contenido:
        print(linea.strip())  # Imprimir cada línea sin espacios al inicio o al final.