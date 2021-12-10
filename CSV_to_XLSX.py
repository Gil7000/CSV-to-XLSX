# Converter arquivos CSV em XLSX
import os, time, pandas as pd
os.chdir('.\Work')    # altera para esse diretório no Windows
#os.chdir('Work/')    # altera para esse diretório no Mac

print('Iniciando o programa : '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

#Percorre os arquivos do diretório de trabalho com um loop
for arqcsv in os.listdir('.'):
    # separa o nome do arquivo e a extensão
    arquivo, extensao = os.path.splitext(arqcsv)
    # verifica se a extensão do arquivo é .CSV
    if extensao.upper() == '.CSV':
        print('Lendo arquivo...: '+arqcsv)
        # em alguns casos os arquivos CSV possuem 0 (zero) a esquerda
        # para não perder esses 0 (zeros) precisa definir a coluna do arquivo CSV como texto
        # o comando abaixo informa que a coluna Codigo é texto.
        df_csv = pd.read_csv(arqcsv,sep = ";", dtype={"CDC":"string","Peso":"float"})
        # df_csv = pd.read_csv(arqcsv,sep = ";")
        del df_csv['Grade']
        print('Gravando arquivo: '+arquivo+'.xlsx')
        df_csv.to_excel(arquivo+'.xlsx',index=False)
print(' ')
print('Acabou: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#Acabou
# GAS 16/11/2021

