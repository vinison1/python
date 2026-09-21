
def soma(n1,n2):
    resultado = n1 + n2
    print("A soma entre",n1,"+",n2,"é igual a",resultado)
    decisao = input("Deseja continuar? (s/n):")
def subtracao(n1,n2):
    resultado = n1 - n2
    print("A subtração entre",n1,"-",n2,"é igual a",resultado)
    decisao = input("Deseja continuar? (s/n):")
def multiplicacao(n1,n2):
    resultado = n1 * n2
    print("A multiplicação entre",n1,"*",n2,"é igual a",resultado)
    decisao = input("Deseja continuar? (s/n):")
def divisao(n1,n2):
    while n2 == 0:
        print("Não é possível dividir por zero.")
        n2 = float(input("Digite o segundo numero:"))
  
    resultado = n1 / n2
    print("A divisão entre",n1,"/",n2,"é igual a",resultado)
    decisao = input("Deseja continuar? (s/n):")
def media_aritmetica(quantidade):
    soma = 0
    contador = 0
    while quantidade > contador:    
        num = float(input("Digite um numero:"))
        soma += num
        contador += 1
    media = soma / quantidade  
    print(soma,"/",quantidade,"=",media)
    decisao = input("Deseja continuar? (s/n):")
def potenciacao(base, expoente):
    resultado = base ** expoente
    print(base,"^",expoente,"=",resultado)
    decisao = input("Deseja continuar? (s/n):")
def raiz_quadrada(num):
    if num < 0:
        print("Não é possível calcular a raiz quadrada de um número negativo.")
        return
    resultado = num ** 0.5
    print("A raiz quadrada de",num,"é igual a",resultado)
    decisao = input("Deseja continuar? (s/n):")
def raiz_cubica(num):
    if num < 0:
        print("Não é possível calcular a raiz cúbica de um número negativo.")
        return
    resultado = num ** (1/3)
    print("A raiz cúbica de",num,"é igual a",resultado)
    decisao = input("Deseja continuar? (s/n):")
print('bem vindo a calculadora')
decisao = 's'
while decisao == 's':
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')    
    print('5 - media aritimetica')
    print('6 - potenciação')
    print('7 - raiz quadrada')
    print('8 - raiz cúbica')
    print("9 - sair")
    escolha = input('Escolha uma opção:')
    contador = 0
    match escolha:
        case '1': 
            num1 = int(input("Digite o primeiro numero:"))
            num2 = int(input("Digite o segundo numero:"))
            soma(num1,num2)
            
        case '2':
            num1 = int(input("Digite o primeiro numero:"))
            num2 = int(input("Digite o segundo numero:"))
            subtracao(num1,num2)
            
        case '3':
            num1 = int(input("Digite o primeiro numero:"))
            num2 = int(input("Digite o segundo numero:"))
            multiplicacao(num1,num2)
           
        case '4':
            num1 = float(input("Digite o primeiro numero:"))
            num2 = float(input("Digite o segundo numero:"))
            divisao(num1,num2)
                
        case '5':
            num2 = 0
            quantidade = int(input("Digite a quantidade de numeros:"))
            media_aritmetica(quantidade)
          
        case '6':
            num1 = float(input("Digite a base:"))
            num2 = float(input("Digite o expoente:"))
            potenciacao(num1,num2)   
         
        case '7':
            num1 = float(input("Digite um numero:"))
            raiz_quadrada(num1)
        case '8':
            num1 = int(input("Digite um numero:"))
            raiz_cubica(num1)
        case '9':
            print("Saindo da calculadora...")
            decisao = False
            

