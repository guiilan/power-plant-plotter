
import matplotlib.pyplot as plt
import dados
def ApresentarGraficoDeLinha():

    dados_proc = dados.dados()



    meses = {'janeiro':'01','fevereiro':'02', 'março':'03','abril':'04','maio':'05','junho':'06',
    'julho':'07','agosto':'08','setembro':'09','outubro':'10','novembro':'11','dezembro':'12'}
    energia_ger_mes = []
    print('#'*65)
    print('#',' '*61,'#')
    print('#',' '*18,'GRAFICO DE LINHA',' '*25,'#')
    print('#',' '*61,'#')
    print('#'*65)
    mes_desejado = input('Qual o mes desejado\nexemplo " outubro ": ').lower()
    # pegando dias e energia gerada no dia de um determinador mes
    for energia in dados_proc:
        mes = energia['dia'].split('-')
        if mes[1] == meses[mes_desejado]:
          energia_ger_mes.append((energia['dia'], energia['energiaDia']))
    #cologando em ordem do primeiro dia ate o ultimo
    energia_ger_mes.sort()
    energia_ger_mes_ordenada = []
    #pegando apenas a energia do mes já na ordem correta dos dias
    for dia , energia in energia_ger_mes:
        energia_ger_mes_ordenada.append(energia)
    #plotagem do grafico
    tamanho_do_mes = range(1, len(energia_ger_mes_ordenada) + 1,1)
    title = ('ENERGIA GERADA NO MES DE' + ' ' + mes_desejado).upper()
    plt.plot(tamanho_do_mes ,energia_ger_mes_ordenada)
    plt.title(title, color = 'white')
    plt.xlabel('DIAS DO MES',color = 'white')
    plt.ylabel('ENERGIA GERADA', color = 'white')
    plt.tick_params(labelcolor = 'white')
    plt.stem(tamanho_do_mes ,energia_ger_mes_ordenada, use_line_collection=True)
    plt.fill_between(tamanho_do_mes ,energia_ger_mes_ordenada, facecolor ='#a5f5ff')
    plt.grid(True, linestyle ='-.')
    plt.legend(['Mes'])
    plt.savefig('linha.png',facecolor = '#404040', transparent = True)
    plt.close()
    