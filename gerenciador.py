# -*- coding: utf-8 -*-
"""Part two

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A5fRg1gpGmWj4XLKmtZgvOB3KITiO8Z7
"""

#Importando as bibliotecas necessárias para a execução do programa
import pandas as pd
import numpy as np
import datetime as dt

#definindo as listas e dicionários que serão utilizados para armazenar os dados coletados
funcao = int(input('1 - Novo cadastro\n2 - Relatório\nEscolha a opção desejada: '))
date = []
nomes = []
moeda_origemtb = []
moeda_destinotb = []
valor_origemtb = []
valor_destinotb = []
taxa_cambiotb = []
op_reais = []
tx_reais = []
report = {}

#definindo variáveis acumuladoras
somaop = 0
somatx = 0

#criando um laço de repetição
while True:
  if funcao == 1:
    nome = input('\nDigite o nome do cliente (sem acentuação): ')
    nome = nome.upper()
    data = input('\nDigite a data no formato (24/05/2022)')
    data_formatado = dt.datetime.strptime(data, '%d/%m/%Y')
    date.append(data_formatado)
    nomes.append(nome)
  
    #Calculadora de conversão de moedas
 
    #Criando a função que vai deixar a saída dos dados alinhada
    def formatar(valor):
      return f'{valor:>8}'
 
    #Informando ao usuário os valores previamente cadastrados
    print('\nLista de Conversões unitárias cadastradas em R$ ')
 
    #Cadastrando os valores em listas
    moeda = ['EUR', 'USD', 'CAD', 'AUD', 'BRL']
    valor = [6.36, 5.23, 4.32, 4.10, 1.00]
 
    #criando o dicionário que conterá as listas
    dicio = {}
 
    #organizando a forma como é apresentado ao usuário
    print(''.join(map(formatar, moeda)))
    print(''.join(map(formatar, valor)))
    print('\nTaxa de operação: 10%')
 
    #atribuindo as listas ao dicionário
    dicio['moeda'] = moeda
    dicio['valor'] = valor
 
    #criando o laço de repetição para o programa se manter em execução até que o usuário escolha sair
    opt = int(input('\nDeseja cadastrar uma nova moeda antes de iniciar? Digite (1) para sim e (2) para não: '))
    while True:
      #cadastrando uma nova moeda
      if opt == 1:
        
        #criando a mensagem de erro caso o usuário digite um valor inválido
        while True:
          try: 
            n = int(input('\nQuantas novas moedas você deseja cadastrar?: '))
            if 0>= n:
              raise ValueError('\nVocê digitou um valor inválido. Favor inserir um valor maior que 0: ')
          except ValueError as e:
            print('\nValor inválido, tente digitar um número inteiro: ')
          else:
            break    
        
        #criando o laço de repetição para entrada de dados
        for i in range(n):
          moe = input('\nQual o nome da moeda? ')
          while True:
            #criando a mensagem de erro caso o usuário digite um valor inválido
            try: 
              val = float(input('\nQual o valor atual da moeda em reais? R$ '))
              if 0>= val:
                raise ValueError('\nVocê digitou um valor inválido. Favor inserir um valor maior que 0: ')
            except ValueError as e:
              print('\nValor inválido, tente novamente. Tente usar (.) ao invés de (,) para a casa decimal: ')
            else:
              break
          
          #adicionando a nova moeda ao dicionário
          dicio['moeda'].append(moe)
          dicio['valor'].append(val)
          opt = 2
      
      #calculando a conversão da moeda    
      elif opt == 2:
        
        #mostrando as opções cadastradas para o usuário
        print(''.join(map(formatar, range(len(moeda)))))
        print(''.join(map(formatar, moeda)))
        print(''.join(map(formatar, valor)))
        
        #criando a mensagem de erro caso o usuário digite um valor inválido
        while True:
          try:
            orig = int(input('\nDigite o código da moeda de origem (ex: digite 0 para EUR): '))
            if 0> orig or orig > len(moeda):
              raise ValueError('\nVocê digitou um valor inválido. Favor escolha uma das opções apresentadas anteriormente!')
          except ValueError as e:
            print('\nValor inválido, tente digitar um número inteiro!')
          else:
            break
        
        #criando a mensagem de erro caso o usuário digite um valor inválido
        while True:
          try:
            v = float(input('\nDigite o valor na moeda de origem a ser convertido: {} '.format(moeda[orig])))
            if 0>= v:
              raise ValueError('\nVocê digitou um valor inválido. Favor inserir um valor maior que 0!')
          except ValueError as e:
            print('\nValor inválido, tente utilizar o "." para separar a casa decimal!')
          else:
            break
        
        #criando a mensagem de erro caso o usuário digite um valor inválido
        while True:
          try:
            x = int(input('\nDigite o código da moeda em que deseja converter (ex: digite 0 para EUR): '))
            if 0> x or x > len(moeda):
              raise ValueError('\nVocê digitou um valor inválido. Favor inserir um valor maior que 0!')
          except ValueError as e:
            print('\nValor inválido, tente digitar um número inteiro!')
          else:
            break
        
        #criando o laço de repetição para varredura na lista e cálculo das conversões      
        for itens in valor:
          val = valor[x]
          
          #adicionando a taxa de corretagem na cotação da moeda 
          valtx = valor[x] * 1.1
          cambio = valor[orig] * v / valtx
          opt = 4
          break
 
      #caso o usuário digite um valor fora do intervalo especificado
      elif opt == 4:
        break
 
      else:
        print('\nValor inválido. Digite um valor no intervalo especificado!')
        continue
 
    #relacionando variáveis, listas e dicionários
    moeda_orig = moeda[orig]
    moeda_dest = moeda[x]
    valor_orig = v
    valor_dest = cambio
    somaop += (valor_dest * valtx)
    taxa_cambi = ((valor[orig] * v) / valor[x]) - ((valor[orig] * v) / valtx)
    somatx += (taxa_cambi * valtx)
    moeda_origemtb.append(moeda_orig)
    moeda_destinotb.append(moeda_dest)
    valor_origemtb.append(valor_orig)
    valor_destinotb.append(valor_dest)
    taxa_cambiotb.append(taxa_cambi)
    op_reais.append(somaop)
    tx_reais.append(somatx)
    report['nome'] = nomes
    report['data'] = date
    report['moeda_origem'] = moeda_origemtb
    report['moeda_destino'] = moeda_destinotb
    report['valor_origem'] = valor_origemtb
    report['valor_destino'] = valor_destinotb
    report['taxa_cambio'] = taxa_cambiotb
    report['valor_op_reais'] = op_reais
    report['valor_tx_reais'] = tx_reais
    #Exibindo os resultados na tela
    for i,j in report.items():
      print('{} = {}'.format(i,j))

    funcao = int(input('\n1 - Novo cadastro\n2 - Relatório\nEscolha a opção desejada: '))
    
    continue
  
  elif funcao == 2:
    #criando os Dataframes a partir do dicionário
    operacoes_db = pd.DataFrame(report)
    operacoes_db_filter = pd.DataFrame(report)
    operacoes_db['data'] = pd.to_datetime(operacoes_db['data'])

    #gerando relatórios e filtrando os dataframes
    rprt = input('Digite "R" para gerar um relatório ou "S" para sair: ')
    if rprt == "R" or rprt == 'r':
      ##criando a mensagem de erro caso o usuário digite um valor inválido
      while True:
              try:
                fil = int(input('\n1 - Filtrar por nome\n2 - Filtrar por intervalo\n3 - Filtar por nome e intervalo\n'))
                if 0> fil or fil > 3:
                  raise ValueError('\nVocê digitou um valor inválido. Favor escolha uma das opções apresentadas anteriormente!')
              except ValueError as e:
                print('\nValor inválido, tente digitar um número inteiro!')
              else:
                break
      #condições para execução dos blocos de instruções
      if fil == 1:
        pes_nome = input('\nInforme o nome para realizar o filtro: ')
        pes_nome = pes_nome.upper()
        operacoes_db_filter = operacoes_db.loc[operacoes_db['nome'] == pes_nome]
        break
      
      elif fil == 2:
        data_inicial = input('\nInforme a data incial no formato (12/10/2020): ')
        data_inicial = dt.datetime.strptime(data_inicial, '%d/%m/%Y')
        data_final  = input('\nInforme a data final no formato (12/10/2020): ')
        data_final = dt.datetime.strptime(data_final, '%d/%m/%Y') 
        start_date = operacoes_db['data'] >= data_inicial
        end_date = operacoes_db['data'] <= data_final
        entre_datas = start_date & end_date
        operacoes_db_filter = operacoes_db.loc[entre_datas]
        break

      elif fil == 3:
        pes_nome = input('\nInforme o nome para realizar o filtro: ')
        pes_nome = pes_nome.upper()
        data_inicial = input('\nInforme a data incial no formato (12/10/2020): ')
        data_inicial = dt.datetime.strptime(data_inicial, '%d/%m/%Y')
        data_final  = input('\nInforme a data final no formato (12/10/2020): ')
        data_final = dt.datetime.strptime(data_final, '%d/%m/%Y') 
        start_date = operacoes_db['data'] >= data_inicial
        end_date = operacoes_db['data'] <= data_final
        entre_datas = start_date & end_date
        operacoes_db_filter = operacoes_db.loc[entre_datas].copy()
        operacoes_db_filter = operacoes_db_filter.loc[operacoes_db_filter['nome'] == pes_nome]
        break

      else:
        print('Digite um valor válido!')
    #exibindo os resultados na tela
    
    elif rprt == 'S' or rprt == 's':
      print('Encerrando  o programa ... ')
      break
operacoes_db_filter.append(operacoes_db_filter[['valor_op_reais', 'valor_tx_reais']].sum().rename('Totais')).fillna('') #mostrando a soma das colunas de interesse