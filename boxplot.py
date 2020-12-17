import matplotlib.pyplot as plt
import dados

def ApresentarGraficoBoxplot():

  dados_proc = dados.dados()
  #dicionario contendo os meses do ano.
  meses = {1:'01',2:'02', 3:'03',4:'04',5:'05',6:'06',
          7:'07',8:'08',9:'09',10:'10',11:'11',12:'12'}
  print('#'*65)
  print('#',' '*61,'#')
  print('#',' '*18,'GRAFICO DE BOXPLOT',' '*23,'#')
  print('#',' '*61,'#')
  print('#'*65)
  #entrada referente ao semestre desejado.
  entrada = input('Escolha o semestre desejado\nDigite 1 para o primeiro semestre:\nDigite 2 para o segundo semestre: ')
  semestre = []
  lista_de_meses = []
  # Pegando energia gerada no semestre 1
  if entrada == '1':
      c = 1
      while c <= 6:
        for energia in dados_proc:
            mes = energia['dia'].split('-')
            if meses[c] == mes[1]:
              lista_de_meses.append(energia['energiaDia'])
              

        semestre.append(lista_de_meses)
        lista_de_meses = []
        c += 1
  # Pegando energia gerada no semestre 2
  if entrada == '2':
      c = 7
      while c <= 12:
        for energia in dados_proc:
            mes = energia['dia'].split('-')
            if meses[c] == mes[1]:
              lista_de_meses.append(energia['energiaDia'])
              
        semestre.append(lista_de_meses)
        lista_de_meses = []
        c += 1
  # plotando grafico boxplot do semestre 1
  if entrada == '1':
      meses = ['JAN','FEV','MAR','ABRI','MAI','JUN']
      plt.boxplot(semestre, labels = meses, patch_artist = True)
      plt.ylabel('TOTAL GERADO',color = 'white')
      plt.xlabel('MESES',color = 'white')
      plt.tick_params(labelcolor = 'white')
      plt.title('GRAFICO SEMESTRAL DE JAN - JUN',color = 'white')
      plt.savefig('boxplot.png',facecolor = '#404040', transparent = True)
      plt.close()
 # plotando grafico boxplot do semestre 2
  if entrada == '2':
      meses = ['JUL', 'AGO','SET', 'OUT', 'NOV','DEZ']
      plt.boxplot(semestre, labels = meses,patch_artist = True)
      plt.ylabel('TOTAL GERADO', color ='white')
      plt.xlabel('MESES', color ='white')
      plt.tick_params(labelcolor = 'white')
      plt.title('GRAFICO SEMESTRAL DE JUL-DEZ', color ='white')
      plt.savefig('boxplot.png',facecolor = '#404040', transparent = True)
      plt.close()


