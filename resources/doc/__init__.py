#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Directorio doc
# Fichero generado automáticamente usando __scan__.py
#
# Game template
# Autor: GEORGIANA M. LOHAN
# Archivos totales: 1
# Fecha: Marzo 2020

# Importación de liberías
import os


# Definición de variables
__actualpath = str(os.path.abspath(os.path.dirname(__file__))).replace("\\","/") + "/"

# Librería de /doc
DOC = {

	#Licence
	"CC": __actualpath + "licence/CC.txt"
}

# Función que retorna el elemento <index> de la librería DOC
def getDoc(index):
    try:
        return DOC[index]
    except:
        return -1

# Función que retorna los archivos en DOC
def getDocKeys():
    return DOC.keys()

# Función que imprime los archivos en DOC
def printDocValues():
    print "<KEY> DOC[<KEY>]"
    for file in DOC.keys():
        print file +" "+str(DOC[file])
    
