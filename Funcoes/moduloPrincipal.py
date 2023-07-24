# Importando as funções criadas
from Funcoes.funcoes import *

minhaLista=[]
escolhaMenu="0"

while escolhaMenu!="4":
    escolhaMenu = input("1 - Inserir dados \n2 - Exibir lista \n3 - Buscar \n4 - Finalizar \n:")
    if escolhaMenu=="1":
        # Chamando a função e colocando a lista como parâmetro
        preencherLista(minhaLista)
    elif escolhaMenu=="2":
        exibirLista(minhaLista)
    elif escolhaMenu=="3":
        buscarPorEquipamentoLista(minhaLista)