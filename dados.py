import json
import urllib.request as req
def dados():
    # Endereço do qual se obterá uma resposta no formato JSON. Representa o resumo
   

    url = "http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json"

    # Cria uma requisição para a URL passada e define no cabeçalho um browser conhecido como
    # cliente (agent) para que o site não proíba o acesso

    requisicao = req.Request(url, headers={'User-Agent': 'Chrome/5.0'})

    # Isto faz com que a URL seja acessa e todo o seu conteúdo seja lido
    # e guardado na variável "dados"

    dados = req.urlopen(requisicao).read().decode()

    # json.loads transforma os dados guardados na string em uma estrutura de dados
    # equivalente em Python, que pode ser um dicionário ou lista.
    # Neste caso é um dicionário
    dados_proc = json.loads(dados)
    return dados_proc
