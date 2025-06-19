### ✅ **Estructuras de control**

#1. Uso de `while`
while 2 + 2 == 4:
    print('hola 1')
    break
#2. Uso de `for`
for a in 'b':
    print(a)
#3. Uso de `range()`
cadena = 'hola'
for i in range(3):
    print(cadena[i])

### ✅ **Variables y operaciones**

#4. Definición de variables
a = 'hola'
b = ' '
c = 'mundo'
d = 14
#5. Operaciones matemáticas
print(1 + 1,
2 - 2,
3 * 3,
4 / 4,
5 ** 5,
6 % 6)

### ✅ **Funciones**

#6. Función **con argumentos**
def funcion_con_argumento(a):
    print(a)
funcion_con_argumento('eeeella')
#7. Función **sin argumentos**
def funcion_sin_argumento(a=1, b=2):
    print(a+b)
funcion_sin_argumento()

### ✅ **Entrada y salida**

#8. Uso de `input()`
variable = input('ingrese algo: ')
print(variable)
#9. Uso de `print()` u otro tipo de `output`
print('¿otro tipo de output?')

### ✅ **Manejo de errores**

#10. Manejo de **división por cero** (`ZeroDivisionError`)
try:
    error = 0/0
    print(error)
except ZeroDivisionError:
    print('intentaste divir por cero')
#11. Manejo de **ValueError**
try:
    error_2 = int('j')
    print(error_2)
except ValueError:
    print('valores incompatibles')

### ✅ **Condicionales**

#12. Uso de `if`, `elif`, `else`
if 2+2 == 3:
    print('genius')
elif 2+2 == 8:
    print('supercalifragilistico')
else:
    print('espialidoso')
#13. Validar **varias condiciones en un mismo `if`**
if 2+2 == 4 and 1+1+1+1 == 4:
    print('ok')
#14. Uso de los operadores **lógicos `and` y `or`**
if len('perro') < 5 or len('gato') < 5:
    print('palabra de cuatro caracteres')

### ✅ **Estructuras de datos**

#15. Uso de **listas**, con al menos **2 operaciones `.append()`**
lista = []
for i in '10':
    mercado = input('compras?: ')
    lista.append(mercado)
print(lista)
#16. Uso de **diccionarios**, incluyendo:
diccionario = {'nombre': 'jorge',
               'genero': 'masculino',
               'personalidad': 'carismatico'}
#* Modificar un valor del diccionario
diccionario['personalidad'] = 'callado'
#* Mostrar un valor del diccionario
print(diccionario['personalidad'])

### ✅ **Estilo y presentación**

#17. Variables y funciones con **nombres en minúsculas** y **separadas con guion bajo** (`snake_case`)
#18. El trabajo debe ser un **trabajo serio** (bien presentado, con lógica clara y sin errores básicos)

### ✅ **Extras obligatorios**

#19. Subir el trabajo a **GitHub**
#20. Uso de **formateo de strings** (por ejemplo, con `f""`)
print(f'variables del programa: {cadena}, {a}, {b}, {c}, {d}, {variable}, {lista}, {i}, {mercado}, {diccionario}')
#21. Uso de **casting** a `int` y `float` (`int()`, `float()`)
casteo_a_entero = int(input('ingrese un numero: '))
casteo_a_decimal = float(input('ingrese un numero: '))
print(casteo_a_entero, casteo_a_decimal)

#extra
x = '0'
while x != '3':
    print('menú')
    print('opcion 1: impresion misteriora')
    print('opcion 2: impresion misteriora')
    print('opcion 3: salir')
    x = input('elección: ')
    if x == '1':
        print('hola')
    elif x == '2':
        print('eo')
    elif x == '3':
        print('adios')
        break

# --- fin --- 