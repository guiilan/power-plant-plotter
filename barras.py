

import matplotlib.pyplot as plt
import dados
def ApresentarGraficoDeBarras():
    
    dados_proc = dados.dados()
      
    meses = {'janeiro':'01','fevereiro':'02', 'março':'03','abril':'04','maio':'05','junho':'06',
        'julho':'07','agosto':'08','setembro':'09','outubro':'10','novembro':'11','dezembro':'12'}
    potencias_do_mes = []
    print('#'*65)
    print('#',' '*61,'#')
    print('#',' '*18,'GRAFICO DE BARRAS',' '*24,'#')
    print('#',' '*61,'#')
    print('#'*65)
    diaEmes = input('Informe o dia e o mes desajado\nexemplo " 5/novembro ": ').split('/')
    
        # pegando a data e as pontencias do mes selecionado.
    for watts in dados_proc:
            mes = watts['dia'].split('-')
            if meses[diaEmes[1]] == mes[1]:
                potencias_do_mes.append((watts['dia'],watts['potencia']))
        #usar a função sort() para por em ordem do dia primeiro até o ultimo do mes
    potencias_do_mes.sort()
    potencias = []
        #tirando a data e pegando apenas as potencias já em ordem.
    for data, potencia in potencias_do_mes:
            potencias.append(potencia)
        #pegando a lista de pontencias de um derterminado dia
    potencia_do_dia = potencias[(int(diaEmes[0])-1)]



        #Separando as potencias de cada 5min em medias das
        #potencias em cada uma hora.
    media_do_dia = []
    media_da_hora = []
    for watts in potencia_do_dia:
            if len (media_da_hora) < 12:
                if watts < 0:
                    media_da_hora.append(0)

                else:
                    media_da_hora.append(watts)

            else:
                mediaDaHora = sum(media_da_hora)/12
                media_do_dia.append(mediaDaHora)
                media_da_hora = []
                if watts < 0:
                  media_da_hora.append(0)
                else:
                  media_da_hora.append(watts)
  

    mediaDaHora = sum(media_da_hora)/12
    media_do_dia.append(mediaDaHora)
        #plotagem do gráfico. 
    horarios = ['5-6h','6-7h','7-8h','8-9h','9-10h','10-11h','11-12h','12-13h','13-14h','14-15h','15-16h','16-17h','17-18h','18-19h','19-20h','20-21h']
    nulo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    title = ('MEDIA DAS POTENCIAS GERADAS NO DIA'+ ' ' + diaEmes[0] + ' ' + 'de' + ' ' + diaEmes[1]).upper()
    plt.figure(figsize=(15,10))
    plt.bar(horarios, media_do_dia)
    plt.bar(horarios, nulo, color = '#ADD8E6' )
    plt.bar(horarios, nulo, color = '#ADD8E6' )
    plt.bar(horarios, nulo, color = '#ADD8E6' )
    plt.xlabel('HORARIOS DO DIA: 5:00 as 21:00',color = 'white')
    plt.ylabel('POTENCIAS EM WATTS',color = 'white')
    plt.title(title,color = 'white')
    plt.tick_params(labelcolor = 'white')
    plt.grid(True)
    plt.legend(['Dia','Mes','Ano','Total'])    
    plt.savefig('barras.png', facecolor = '#404040', transparent = True)
    plt.close()