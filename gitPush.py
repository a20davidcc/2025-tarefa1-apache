from misfunciones import execComando
from datetime import datetime

fecha_actual = datetime.now().strftime("%Y/%m/%d")
comandoAdd = 'git add .'
comandoCommit = f'git commit -m {fecha_actual}'
comandoPush = 'git push origin main'
muestraResultado = 'git status'


execComando(comandoAdd)
execComando(comandoCommit)
execComando(comandoPush)
result = execComando(muestraResultado)
print(result)