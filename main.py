#cria uma lista de tarefas vazia
Lista_de_tarefas=[]

#cria o loop principal do menu
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
            if str(escolha)==('1'):
                Lista_de_tarefas.append(input("Adicione a tarefa: "))
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
                    try:
                        str(item_a_ser_deletado)
                    except:
                        print ('Um erro aconteceu.')
                    else:
                        if str(item_a_ser_deletado)==('sair'):
                            break



                    #quebra se item_a_ser_deletado não pode virar int
                    try:
                        item_a_ser_deletado=int(item_a_ser_deletado)
                    except:
                        print("tarefa não existe.")
                        break

                    #Deleta o numero selecionado
                    if item_a_ser_deletado>len(Lista_de_tarefas):
                        print ('tarefa não faz parte da lista ou lista está vazia.')
                    elif Lista_de_tarefas==0:
                        print ('tarefa não faz parte da lista.')
                    else:
                        if Lista_de_tarefas!=[]:
                            Lista_de_tarefas.pop(item_a_ser_deletado-1)
                            print ("Tarefa foi deletada.")
                            break
                        else:
                            print ('lista está vazia.')
                            break
            #quebra menu da escolha 3
            else:
                break

        #Mensagem de erro.
        else:
            print ('Opção não faz parte do menu.')