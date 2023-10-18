
#Escribe una función que reciba dos strings (de largo > 2) como parámetros, y retorne un string de largo 4 q
#Que consista de las dos primeras letras del primer string y las últimas dos letras del segundo.
#Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función debe retornar "fase".
def mezclador(string_a, string_b):
  return string_a[0:2]+string_b[-2]+string_b[-1]

mezclador("familia","abrigarse")

