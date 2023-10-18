
#Escribe una función que reciba dos strings (de largo > 2) como parámetros, y retorne un string de largo 4 q
#Que consista de las dos primeras letras del primer string y las últimas dos letras del segundo.
#Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función debe retornar "fase".
def mezclador(string_a, string_b):
  return string_a[0:2]+string_b[-2]+string_b[-1]

mezclador("familia","abrigarse")

#Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero, 
#pero con el segundo string intercalado entre cada letra del primero.
#Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"
def intercalar(string_a, string_b):
  return string_a[0:1]+string_b+string_a[1:2]+string_b+string_a[-1]+string_b

intercalar("PAZ","so")