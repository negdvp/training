
#Escribe una función que reciba dos strings (de largo > 2) como parámetros, y retorne un string de largo 4 q
#Que consista de las dos primeras letras del primer string y las últimas dos letras del segundo.
#Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función debe retornar "fase".
def mezclador(string_a, string_b):
  return string_a[0:2]+string_b[-2]+string_b[-1]

print("Ejercicio 1")
print(mezclador("familia","abrigarse"))

#Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero, 
#pero con el segundo string intercalado entre cada letra del primero.
#Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"
def intercalar(string_a, string_b):
  return string_a[0:1]+string_b+string_a[1:2]+string_b+string_a[-1]+string_b

print("Ejercicio 2")
print(intercalar("PAZ","so"))


def intercalar(string1, string2):
    resultado = ""
    i = 0
    j = 0

    while i < len(string1) or j < len(string2):
        if i < len(string1):
            resultado += string1[i]
            i += 1
        if j < len(string2):
            resultado += string2[j]
            j += 1

    return resultado

# Ejemplo de uso:
cadena1 = "Hola"
cadena2 = "MT"
resultado = intercalar(cadena1, cadena2)
print("Ejercicio 2 bis")
print(resultado)  # Esto imprimirá "HMoLunodao"



#Escriba una función que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.
#Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)
def ocurrencias(string):
  return string.count('1')- string.count('0')

print("Ejercicio 3")
print(ocurrencias("11000110101"))


#Escriba una función que reciba un string s y un número n como parámetros y retorne el mismo string s pero sin el elemento en el índice n.
#Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".
#Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.
def remover_enesimo(s, n):
    # Verificar si el índice n está dentro de los límites del string
    if 0 <= n < len(s):
        # Usar slicing para eliminar el carácter en el índice n
        s = s[:n] + s[n+1:]
    else:
        print("El índice está fuera de los límites del string.")
    
    return s

cadena_original = "Hasta luego"
nuevo_string = remover_enesimo(cadena_original, 3)
print("Ejercicio 4")
print(nuevo_string) 


#Escriba una función que reciba un string como parámetro y retorne el string, 
# pero con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.
#Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".
def reemplazo(string):

    resultado = ""
    for caracter in string:
        if caracter.isupper():
            resultado += "$"
        else:
            resultado += caracter
    return resultado

cadena_original = "Viva la Vida"
nueva_cadena = reemplazo(cadena_original)
print("Ejercicio 5")
print(nueva_cadena)  