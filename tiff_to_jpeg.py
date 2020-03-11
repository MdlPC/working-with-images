import os
from PIL import Image
from tkinter import filedialog

def tiff_to_jpeg(calidad=75):
    '''
    Allows you to choose a folder in order to transform tiff images within the folder into new jpeg files 
    (creates a new file that shares name with initial tiff document)
    '''
    directorio = filedialog.askdirectory()

    for archivo in os.listdir(directorio):
        if archivo.endswith('.tif'):
            fin=archivo.index('.')
            nombre=''
            nombre_final = ''
            for letra in range(0,fin):
                nombre += archivo[letra]
            nombre_final = nombre + '.jpg'
            try:
                print(f'transformando {nombre}')
                imagen = Image.open(os.path.join(directorio,archivo))
                imagen.thumbnail(imagen.size)
                directorio_final = os.path.join(directorio, nombre_final)
                imagen.save(directorio_final, format='JPEG', quality=calidad)
            except:
                pass
        

tiff_to_jpeg()
