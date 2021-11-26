#import para usar o time.sleep() e random
import time
import random

#utils
numero_secreto = random.randint(0,100)
chances = 0
maxChances = 0
nivel = 1 # 1- facil 2- médio 3- difícil

#head


print('\n\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('          JOGO DA ADVINHAÇÃO        ')
print('____________________________________ \n')
print('Foi gerado um número aleatório entre 0 e 100 e cabe a você acertar \n')


#wait
time.sleep(2)

#dificuldade

nivel = int(input('Escolha a dificuldade entre: \n \n 1 - fácil \n 2 - médio \n 3 - difícil \n \n'))

if (nivel == 1) :
    maxChances = 10
    print('\nFoi escolhido a dificuldade FÁCIL ')

elif (nivel == 2) :
    maxChances = 5
    print('\nFoi escolhido a dificuldade MÉDIA ')

elif (nivel == 3):
    maxChances = 3
    print('\nFoi escolhido a dificuldade DIFÍCIL ')

else :
    print('\nOpção inválida\n será atribuido a dificuldade MÉDIA \n ')
    maxChances = 5

#chances
print(' \n Você tem {} chances de acertar'.format(maxChances))

#dica

if numero_secreto < 10 :
    print('\nDica: O número gerado é menor do que 10')

elif numero_secreto >= 10 and numero_secreto < 20 :
    print('\nDica: O número gerado é menor do que 20')

elif numero_secreto >= 20 and numero_secreto < 30:
    print('\nDica: O número gerado é menor do que 30')

elif numero_secreto >= 30 and numero_secreto < 40:
    print('\nDica: O número gerado é menor do que 40')

elif numero_secreto >= 40 and numero_secreto < 50:
    print('\nDica: O número gerado é menor do que 50')

elif numero_secreto >= 50 and numero_secreto < 60:
    print('\nDica: O número gerado é maior do que 50')

elif numero_secreto >= 60 and numero_secreto < 70:
    print('\nDica: O número gerado é maior do que 60')

elif numero_secreto >= 70 and numero_secreto < 80:
    print('\nDica: O número gerado é maior do que 70')

elif numero_secreto >= 80 and numero_secreto < 90:
    print('\nDica: O número gerado é maior do que 80')

elif numero_secreto >= 90 :
    print('\nDica: O número gerado é maior do que 90')

time.sleep(1)


#contagem de vidas  
for chances in range(1, maxChances + 1):

    #chances
    print('\nchance nº {}'.format(chances))


    

    time.sleep(1)


    #input do número

    chute = int(input('Digite um número: '))

    #verificação 
    acerto = numero_secreto == chute
    Menos = numero_secreto > chute
    Mais = numero_secreto < chute


    #main


    #se acertou entra nesse if
    if acerto:
        print('\nVOCÊ ACERTOU... \n O número secreto era {}\n'.format(numero_secreto))
        
        

        print('\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        print('           CONGRATULATIONS          ')
        print('____________________________________\n')
        
        break
    
    #se não acertou, entra nesse else
    else:

        #te dá uma interação de acordo com o número que você digitou
        if Mais:
            print('\nHUUUUL POR CIMA DA TRAVE... \n O número secreto é menor do que {}\n'.format(chute))
            
            chances +=1

        elif Menos:
            print('\nERROOOOOOU... \n O número secreto é maior do que {}\n'.format(chute))

            chances +=1

        #quando acabar as chances, encerra
        if chances == maxChances + 1:

            print('\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            print('              GAME OVER             ')
            print('____________________________________\n')
            print('O número secreto era {}\n'.format(numero_secreto))
           
            
    





