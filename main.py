tarefa=('')
while True:
    escolha=input('     Menu da Lista de tarefas\n\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Sair ')
    try:
        int(escolha)
    except ValueError:
        print ('Opção Invalida.')
    else:
        if int(escolha)>0 and int(escolha)<=3:
            if str(escolha)==('1'):
                tarefa=('Lista de tarefas:')+tarefa+('\n')+str(input('Adicione a tarefa: '))
            elif str(escolha)==('2'):
                if tarefa==(''):
                    print ('Nenhuma tarefa.')
                else:
                    print (tarefa)
            else:
                break
        else:
            print ('Opção não faz parte do menu.')