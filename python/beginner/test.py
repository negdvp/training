def escribir_archivo(nombre, edad, pais):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n"+str(edad)+"\n"+pais+"\n")
    archivo_usuario.close()

    print(escribir_archivo("Nico",19,"Argentina"))