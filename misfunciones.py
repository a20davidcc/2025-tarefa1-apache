from subprocess import PIPE,Popen
from re import compile,findall

def execComando(comando):
    ejecComando = Popen(comando, shell=True, stdout=PIPE, stderr=PIPE)
    erro = ejecComando.stderr.read().decode('utf-8')
    sComando = ejecComando.stdout.read().decode("utf-8")
    ejecComando.stdout.close()

    if not erro:
        return sComando
    else:
        return erro 
    
##Otra opción
# from subprocess import run
# run(c, shell=True, capture_output=True, text=True).stdout


#from subprocess import run, call
#from re import findall    
## salidaComando = run(comando, shell=True, capture_output=True, text=True).stdout


#####################################################################
## Función que elimina tildes de un texto

import unicodedata
def eliminaTildes(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')



#####################################################################
## Función que dado un archivo del tipo clave:valor 
## me devuelve un diccionario con todo su contenido

def fileToDict(pathArchivo):
    dArchivo = {}

    with open(pathArchivo, 'r') as fr:
        lLineas = fr.readlines()
    for l in lLineas:
        ll = l.strip().split(':')
        try:
            k = ll[0].strip()
            v = ll[1].strip()
            # print(f'{k}:{v}')
            dArchivo.setdefault(k,v)
        except:
            pass
    return dArchivo