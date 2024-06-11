import requests 
import re


web = "https://www.shopdutyfree.es/?gad_source=1&gclid=CjwKCAjw34qzBhBmEiwAOUQcFxUPzyBDexkSTcLzR9JCYgYIvGbAA67mt2nqDrXE7ItUVMON4aHMpBoCQ9YQAvD_BwE"
resultado = requests.get(web)
contenido = resultado.text

patron = r"es/comprar[\w-]*" 
maquinas_repetidas = re.findall(patron, str(contenido))
sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []
def pex5():
    for i in sin_duplicados:
        nombre_maquinas = i.replace("es/comprar", "")
        if nombre_maquinas.startswith("-iphone"):
            maquinas_final.append(nombre_maquinas.strip())
            print(nombre_maquinas)

    if "iphone-12-128gb-negro" in maquinas_final:
        print("No hay ningún dispositivo nuevo")
    else: 
        print("¡Nuevo Dispositivo Apple!!!")

# Llama a la función para ejecutar el código

