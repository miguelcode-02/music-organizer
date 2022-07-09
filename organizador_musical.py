from pathlib import Path
import os
from tinytag import TinyTag
from tqdm import trange

r = Path(r"").as_posix()
r2 = Path(r"").as_posix()

autores = [] #! lista de autores de las canciones

genero = [] #! lista de generos musicales

def carpetas(origen,listas):
    os.mkdir(origen)
    print("Descomprimiendo informacion")
    barra = trange(len(listas),desc=f"Exportando datos de la lista")
    for i in listas: #! i = listas adentro
        for a in i: #! a = diccionario adentro
            for n1,v in a.items(): #! n1 = nombre del diccionario, v = dicionario
                if os.path.exists(f"{origen}/{n1}") == False:
                    os.mkdir(f"{origen}/{n1}")

                for n2,r2 in v.items(): #! n2 = nombre del archivo, r2 = url del archivo de la cancion
                    binario = open(r2,"rb")
                    with open(f"{origen}/{n1}/{n2}","wb") as escribir:
                        escribir.write(binario.read())
                    escribir.close()
        barra.update(1)
    barra.close()
    print("\nterminado\n")


def organizador(origen,directorio,artista,genero):
    sdatos = []
    grutas = []
    rutas = []
    datos = []
    dbarra = trange(len(directorio),desc="Extrayendo informacion de directorio")
    for d in directorio:
        cont=0
        for i in artista:
            tag = TinyTag.get(d.path)
            canciones = [d.name.casefold().count(i),str(tag.artist).casefold().count(i),str(tag.albumartist).casefold().count(i),str(tag.album).casefold().count(i)]
            cont+=1
            if canciones[0] > 0 or canciones[1] > 0 or canciones[2] > 0 or canciones[3] > 0:
                rutas.append({i : {d.name : d.path}})
                break
            else:
                if cont == len(artista):
                    sdatos.append(d.path) #sin informacion
        dbarra.update(1)
    dbarra.close()

    print("Informacion extraida\n")
    sbarra = trange(len(sdatos),desc="Organizando la informacion sin datos")
    for d in sdatos:
        cont=0
        for g in genero:
            tag = TinyTag.get(d)
            nombre = d.replace("C:/Users/miguel/Desktop/mi_musica\\","")
            gcanciones = [str(tag).casefold().count(g), d.casefold().count(g)]
            cont+=1

            if gcanciones[0] > 0 or gcanciones[1] > 0:
                grutas.append({g : {nombre: d}})
                break
            else:
                if cont == len(genero) and gcanciones[0] == 0 and gcanciones[1] == 0 :
                    datos.append({"Sin genero" : {nombre: d}}) #sin informacion
        sbarra.update(1)
    sbarra.close()

    print("Informacion organizada\n")
    lista = [rutas,grutas,datos]
    print("\nConstruyendo datos\n")
    carpetas(origen,lista)



directorio = list(os.scandir(r2))
organizador(r,directorio,autores,genero)
