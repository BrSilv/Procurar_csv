
import os
import time
nome = os.getenv('USERNAME')
caminho = fr'C:\Users\{nome}\Desktop\Relatorios'

arq = os.listdir(caminho)
retorno = input('Busca: ')
print('Processo em execução...\n')


lista = list(arq)

obj = open(fr'C:\Users\{nome}\Desktop\Relatorios\{lista[0]}','r')


for c in arq:
    if c == "Arquivo.csv":
        continue
    else:
        obj = open(fr'C:\Users\{nome}\Desktop\Relatorios\{c}','r')
        cont = 0
    while cont < 10:
        x = obj.readline()
        if x == "":
            cont += 1
        if retorno in x:
            arquivo = open(fr'C:\Users\{nome}\Desktop\Relatorios\Arquivo.csv','a')
            arquivo.writelines(x)
        
    print(c)

print('Processo Concluído')
time.sleep(3)
