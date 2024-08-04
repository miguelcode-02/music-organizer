# Organizador
Organizador es un script que organiza archivos de música en carpetas de acuerdo a su artista y género.

# Requisitos
* Python 3  
* Biblioteca tinytag  
* Biblioteca tqdm

# Uso
1. Modifica las variables r y r2 para especificar los directorios de origen y destino de tus archivos de música.
2. Modifica las listas autores y genero para incluir los artistas y géneros por los que deseas organizar tus archivos de música.
3. Ejecuta el script usando python organizer.py.

# Notas
* El script creará un nuevo directorio en el destino especificado por r.
* El script creará subdirectorios dentro del directorio de destino para cada artista y género especificado en las listas autores y genero.
* Los archivos de música sin información de artista o género se organizarán en una carpeta llamada "Sin datos".
* El script utiliza la biblioteca TinyTag para leer la información de artista y género de los metadatos de los archivos de música. Si los metadatos están incompletos o faltan, el script puede no ser capaz de organizar los archivos con precisión.
