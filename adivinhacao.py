#import para usar o time.sleep()
import time
import random

#utils
numero_secreto = random.randint(0,100)
chances = 0

#head


print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('          JOGO DA ADVINHAÇÃO        ')
print('____________________________________')
print('Foi gerado um número aleatório entre 0 e 100 e cabe a você acertar')


#wait
time.sleep(2)

#chances
print('Você tem 4 chances de acertar')

#dica

if numero_secreto < 10 :
    print('Dica: O número gerado é menor do que 10')

elif numero_secreto >= 10 and numero_secreto < 20 :
    print('Dica: O número gerado é menor do que 20')

elif numero_secreto >= 20 and numero_secreto < 30:
    print('Dica: O número gerado é menor do que 30')

elif numero_secreto >= 30 and numero_secreto < 40:
    print('Dica: O número gerado é menor do que 40')

elif numero_secreto >= 40 and numero_secreto < 50:
    print('Dica: O número gerado é menor do que 50')

elif numero_secreto >= 50 and numero_secreto < 60:
    print('Dica: O número gerado é maior do que 50')

elif numero_secreto >= 60 and numero_secreto < 70:
    print('Dica: O número gerado é maior do que 60')

elif numero_secreto >= 70 and numero_secreto < 80:
    print('Dica: O número gerado é maior do que 70')

elif numero_secreto >= 80 and numero_secreto < 90:
    print('Dica: O número gerado é maior do que 80')

elif numero_secreto >= 90 :
    print('Dica: O número gerado é maior do que 90')

time.sleep(1)


#contagem de vidas  
for chances in range(1,5):

    #chances
    print('chance nº {}'.format(chances))


    

    time.sleep(1)


    #input do número

    chute = int(input('Digite um número: '))

    #opções
    acerto = numero_secreto == chute
    Menos = numero_secreto > chute
    Mais = numero_secreto < chute


    #verificação

    if acerto:
        print('VOCÊ ACERTOU... \n O número secreto era {}'.format(numero_secreto))
        print(' ')
        

        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        print('           CONGRATULATIONS          ')
        print('____________________________________')
        print('O número secreto era {}'.format(numero_secreto))
        print(' ')
        break

    else:
        if Mais:
            print('HUUUUL POR CIMA DA TRAVE... \n O número secreto é menor do que {}'.format(chute))
            print(' ')
            chances +=1

        elif Menos:
            print('ERROOOOOOU... \n O número secreto é maior do que {}'.format(chute))
            print(' ')
            chances +=1

        if chances == 5 :
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            print('              GAME OVER             ')
            print('____________________________________')
            print('O número secreto era {}'.format(numero_secreto))
            print(' ')
            
    





