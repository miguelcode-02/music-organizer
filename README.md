# Organizer
Organizer is a script that organizes music files into folders according to their artist and genre.

# Requirements
* Python 3  
* tinytag library  
* tqdm library

# Usage
1. Modify the r and r2 variables to specify the source and destination directories for your music files.
2. Modify the autores and genero lists to include the artists and genres you want to organize your music files by.
3. Run the script using python organizer.py.

# Notes
* The script will create a new directory at the destination specified by r.
* The script will create subdirectories within the destination directory for each artist and genre specified in the autores and genero lists.
* Music files without artist or genre information will be organized into a "Sin datos" folder.
* The script uses the TinyTag library to read the artist and genre information from the music files' metadata. If the metadata is incomplete or missing, the script may not be able to accurately organize the files.
