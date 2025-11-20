#Importa os

import os


#cria uma lista vazia
Lista_de_tarefas = []

# 1. CARREGAR (Tenta ler o arquivo se ele existir)
if os.path.exists('Lista_de_tarefas.txt'):
    with open('Lista_de_tarefas.txt', 'r') as arquivo:
        # Lê todas as linhas e remove o \n do final de cada uma
        for linha in arquivo:
            Lista_de_tarefas.append(linha.strip())

# 2. LOOP PRINCIPAL (Agora fora do 'with open')
while True:
        #menu principal
        escolha=input('     Menu da Lista de tarefas\n\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. deletar tarefas\n4. Sair\n\nEscolha um numero: ')
        
        #tenta tranformar escolha em int
        try:
            int(escolha)
        except:
            print ('Opção Invalida.')
        
        #principal logica do menu
        else:
            if int(escolha)>0 and int(escolha)<=4:
                if str(escolha)==('1'): #Coloca imput no final da lista de tarefas, depois escreve cada 'tarefa'...
                    Lista_de_tarefas.append(input("Adicione a tarefa: "))
                    with open('Lista_de_tarefas.txt', 'w') as arquivo:
                        for tarefa in Lista_de_tarefas: #...no arquivo, usando ('tarefa + '\n') para pular linha cada vez.
                            arquivo.write(tarefa + '\n')
                    print('tarefa adicionada.')
                    
                elif str(escolha)==('2'):
                    if Lista_de_tarefas==[]:
                        print ('Nenhuma tarefa.')
                    else:
                        #logica do submenu da escolha 2
                        print ('Lista de tarefas:')
                        for indice, tarefa in enumerate(Lista_de_tarefas,1):
                            print (f"{indice}. {tarefa}")
                        input('digite qualquer coisa para sair. ')

                #logica da escolha 3
                elif str(escolha)=='3':
                    #cria o loop do submenu da escolha 3
                    while True:
                        item_a_ser_deletado= input('Escreva o numero da tarefa a deletar ou digite qualquer palavra para sair.')

                        #quebra se item_a_ser_deletado não pode virar int
                        try:
                            item_a_ser_deletado=int(item_a_ser_deletado)
                        except:
                            break

                        #Deleta o numero selecionado e re-escreve o arquivo usando a lista ja sem o deletado.
                        if 0<item_a_ser_deletado<=len(Lista_de_tarefas):
                            Lista_de_tarefas.pop(item_a_ser_deletado-1)
                            with open('Lista_de_tarefas.txt', 'w') as arquivo:
                                for tarefa in Lista_de_tarefas:
                                    arquivo.write(tarefa + '\n')
                            print ("Tarefa foi deletada.")
                            break
                        else:
                            print('item é menor ou igual a zero, ou não faz parte da lista.')
            
                #quebra menu da escolha 3
                else:
                    break

            #Mensagem de erro.
            else:
                print ('Opção não faz parte do menu.')