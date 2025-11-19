Lista_de_tarefas=[]
while True:
    escolha=input('     Menu da Lista de tarefas\n\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. deletar tarefas\n4. Sair\n\nEscolha um numero: ')
    try:
        int(escolha)
    except ValueError:
        print ('Opção Invalida.')
    else:
        if int(escolha)>0 and int(escolha)<=4:
            if str(escolha)==('1') and Lista_de_tarefas==[]:
                Lista_de_tarefas.insert(1,input("Adicione a tarefa: "))
            if str(escolha)==('1') and Lista_de_tarefas!=[]:
                Lista_de_tarefas.append(input("Adicione a tarefa: "))
            elif str(escolha)==('2'):
                if Lista_de_tarefas==[]:
                    print ('Nenhuma tarefa.')
                else:
                    print ('Lista de tarefas:')
                    for tarefa in enumerate(Lista_de_tarefas,1):
                        print (tarefa)
            elif str(escolha)=='3':
                while True:
                    item_a_ser_deletado= input('Escreva o numero da tarefa a deletar ou digite sair para cancelar: ')
                    try:
                        str(item_a_ser_deletado)
                    except:
                        print ('Um erro aconteceu.')
                    else:
                        if str(item_a_ser_deletado)==str('sair'):
                            break
                    try:
                        int(item_a_ser_deletado)
                    except:
                        print("tarefa não existe.")
                  
                    if int(item_a_ser_deletado)<len(Lista_de_tarefas):
                        Lista_de_tarefas.pop(item_a_ser_deletado)
                        print ("Tarefa foi deletada.")
                        break
                    else:
                        print('item não faz parte da lista.')
            else:
                break
        else:
            print ('Opção não faz parte do menu.')