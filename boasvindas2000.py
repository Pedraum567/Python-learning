nome = input('Qual é o seu nome?: ').capitalize()
print('Boas-vindas,', nome + '.')

dia = int(input('Em que dia você nasceu?: '))
while dia <1 or dia > 31:
    dia = input('Por favor, insira um dia válido: ')
    dia = int(dia)

def m(a): #if a != 'outubro' or a != 'novembro' or a != 'dezembro' or a != 'janeiro' or a != 'fevereiro' or a != 'março' or a != 'abril' or a != 'maio' or a != 'junho' or a != 'julho' or a != 'agosto' or a != 'setembro':
    if a == '10':
       a = 'outubro'
       return a
    elif a == '11':
       a = 'novembro'
       return a 
    elif a == '12':
       a = 'dezembro'
       return a
    elif a == '1' or a == '01':
       a = 'janeiro'
       return a
    elif a == '2' or a == '02':
       a = 'fevereiro'
       return a
    elif a == '3' or a == '03':
       a = 'março'
       return a 
    elif a == '4' or a == '04':
       a = 'abril'
       return a 
    elif a == '5' or a == '05':
       a = 'maio'
       return a 
    elif a == '6' or a == '06':
       a = 'junho'
       return a
    elif a == '7' or a == '07':
       a = 'julho'
       return a 
    elif a == '8' or a == '08':
       a = 'agosto'
       return a 
    elif a == '9' or a == '09':
       a = 'setembro'
       return a
    elif a == 'outubro' or a == 'novembro' or a == 'dezembro' or a == 'janeiro' or a == 'fevereiro' or a == 'março' or a == 'abril' or a == 'maio' or a == 'junho' or a == 'julho' or a == 'agosto' or a == 'setembro':
       return a
    elif a != 'outubro':
        while a != 'outubro' or a != 'novembro' or a != 'dezembro' or a != 'janeiro' or a != 'fevereiro' or a != 'março' or a != 'abril' or a != 'maio' or a != 'junho' or a != 'julho' or a != 'agosto' or a != 'setembro':
          a = input('Por favor, digite um mês válido: ').lower()
          if a == '10':
               a = 'outubro'
               return a
          elif a == '11':
               a = 'novembro'
               return a 
          elif a == '12':
               a = 'dezembro'
               return a
          elif a == '1' or a == '01':
               a = 'janeiro'
               return a
          elif a == '2' or a == '02':
               a = 'fevereiro'
               return a
          elif a == '3' or a == '03':
               a = 'março'
               return a 
          elif a == '4' or a == '04':
               a = 'abril'
               return a 
          elif a == '5' or a == '05':
               a = 'maio'
               return a 
          elif a == '6' or a == '06':
               a = 'junho'
               return a
          elif a == '7' or a == '07':
               a = 'julho'
               return a 
          elif a == '8' or a == '08':
               a = 'agosto'
               return a 
          elif a == '9' or a == '09':
               a = 'setembro'
               return a
          elif a == 'outubro' or a == 'novembro' or a == 'dezembro' or a == 'janeiro' or a == 'fevereiro' or a == 'março' or a == 'abril' or a == 'maio' or a == 'junho' or a == 'julho' or a == 'agosto' or a == 'setembro':
               return a
        return a
     
mes = input('De qual mês?: ').lower()
mes = str(mes)

ano = input('Em qual ano?: ')

print('Entendo, então você nasceu no dia', dia, 'de', m(mes), 'de', ano + '. Prazer em te conhecer,', nome + '.')