def entidade(a):
    if a == "me ajude calculadora2000":
        print("com c maiusculo, vou deixar isso passar dessa vez")
        return a 
    elif a == 'me ajude Calculadora2000':
        return a
    elif a == 'me ajude Calculadora 2000':
        print('Calculadora2000, tudo junto, voce não entende?')
        return a
    elif a == 'me ajude calculadora 2000':
        print('C maiusculo, Calculadora2000, tudo junto, voce está testando minha paciencia')
        return a 

clamar = input("se ajoelhe e clame pela a ajuda Calculadora2000 *me ajude Calculadora2000*: ")

print(entidade(clamar))
        
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
        
numero1 = int(input("digite um valor: "))
operacao = input("o que deseja fazer? Somar, dividir, multiplicar, subtrair, potencia?: ").lower()
numero2 = int(input("digite o segundo valor: "))

print(calculadora(numero1,operacao,numero2))
print('Não precisa agradecer à Grande Calculadora2000, ela não tem tempo para ouvir isso')
