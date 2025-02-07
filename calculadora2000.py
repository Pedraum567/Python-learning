def entidade(a):
    if a == "me ajude calculadora2000":
        while a != 'me ajude Calculadora2000': #nota de aprendizado: no uso de 'while', não é correto, em maior parte dos casos, adicionar um 'return' na sua indentação, nesse caso, logo abaixo da input, pois isso vai encerrar a cadeia do 'while'. Então, a posição correta do 'return' é na mesma indentação do 'while', assim, o return só irá fornecer um valor após a condição do 'while' ser cumprida. 
            a = input("Como ousa me desrespeitar??? Calculadora2000, com C maiúsculo. Tente pedir ajuda de novo, direitinho: ")
        return a 
    elif a == 'me ajude Calculadora2000': #input correta
        print('Certo, irei conceder meu conhecimento a você')
        return a 
    elif a == 'me ajude Calculadora 2000':
        while a != 'me ajude Calculadora2000':
           a = input('Calculadora2000, tudo junto, voce não entende? Peça ajuda de novo: ')
        return a
    elif a == 'me ajude calculadora 2000':
        while a != 'me ajude Calculadora2000':
           a = input('C maiúsculo, Calculadora2000, tudo junto, voce está testando minha paciência. Vamos lá, tente pedir ajuda mais uma vez: ')
        return a
        
clamar = input("se ajoelhe e clame pela a ajuda da Calculadora2000 *me ajude Calculadora2000*: ") #input que define a variável que vai ser usada na fórmula 

print(entidade(clamar)) #esse comando vai printar o resultado da formula "entidade" de acordo com a input realizada no comando acima
        
def calculadora(n1,op,n2):
    if op == "somar":
        return n1+n2 
    elif op == "subtrair":
        return n1-n2
    elif op == "multiplicar":
        return n1*n2
    elif op == 'dividir':
        return n1/n2
    elif op == 'potencia': 
        x = n1
        while n2 > 1:
            x = (x * n1)
            n2 = n2 - 1
        return x
    elif op == 'raiz':
        return n1 ** (1/n2)
        
numero1 = int(input("digite um valor: "))
operacao = input("o que deseja fazer? Somar, dividir, multiplicar, subtrair, potencia, raiz?: ").lower() #o ".lower()" é responsável por transcrever a input do usuário para letras minúsculas
numero2 = int(input("digite o segundo valor: "))

print(calculadora(numero1,operacao,numero2))
print('Não precisa agradecer a Grande Calculadora2000, ela não tem tempo para ouvir isso')
