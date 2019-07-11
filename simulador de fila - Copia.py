##Aluno: Guilherme B. da Almeida
##Matricula: 2019303606



fila_idoso = []
fila_gesta = []
fila_comun = []

print()
print()
print('Fila dos idosos :',fila_idoso)
print('Fila das gestantes :',fila_gesta)
print('Fila dos cidadões comuns :',fila_comun)
print()
print()
dig = 1
while dig != '0':
    dig = str(input('Digite 1 se quer acrescentar, ou 2 se quer atender alguém  (E se você quer sair digite 0): '))
    print(80*'-')
    if dig == '1':
        g = str(input('Digite 1 se você é um idoso, 2 se você é uma gestante ou  3 se você é um cidadão comum: '))
        j = str(input('Digite seu nome: '))
        if g == '1':
            fila_idoso.append(j)
        elif g == '2':
            fila_gesta.append(j)
        elif g == '3':
            fila_comun.append(j)
    elif dig == '2':
        if len(fila_idoso) > 0:
            del(fila_idoso[0])
            print()
            print('Um idoso foi atendido!')
            print()
        else:
            if len(fila_gesta) > 0:
                print()
                print('Uma gestante foi atendida!')
                print()
                del(fila_gesta[0])
            else:
                if len(fila_comun) > 0:
                    print()
                    print('Uma pessoa comum foi atendida!')
                    print()
                    del(fila_comun[0])
                else:
                    print()
                    print('As filas estão vazias!!')
                    print()
                
    print()
    print()
    print('Fila dos idosos :',fila_idoso)
    print('Fila das gestantes :',fila_gesta)
    print('Fila dos cidadões comuns :',fila_comun)
    print()
    print()   
print('O banco ira fechar')            
        
    
