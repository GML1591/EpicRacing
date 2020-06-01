# coding=utf-8
"""
PATH
Permite la importación múltiple, agrega librerías al path

Game template
Autor: GEORGIANA M. LOHAN
Fecha: Marzo 2020
"""

# Importa las librerías de sistema
import sys
from libdir import DIR_LIB, DIR_BIN

# Se agregan directorios al path
# noinspection PyCompatibility
reload(sys)
sys.path.append(DIR_LIB)
sys.path.append(DIR_BIN)
sys.path.append(DIR_LIB.replace("\\lib", ""))
