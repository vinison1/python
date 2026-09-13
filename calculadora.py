
print('bem vindo a calculadora')
decisao = 's'
while decisao == 's':
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')    
    print('5 - media aritimetica')
    print('6 - potenciação')
    print('7 - sair')
    escolha = int(input('Escolha uma opção:'))
    contador = 0
    match escolha:
        case 1: 
            num1 = int(input("Digite o primeiro numero:"))
            num2 = int(input("Digite o segundo numero:"))
            soma = num1 + num2
            print("A soma entre",num1,"+",num2,"é igual a",soma)
            decisao = input("Deseja continuar? (s/n):")
            
        case 2:
            num1 = int(input("Digite o primeiro numero:"))
            num2 = int(input("Digite o segundo numero:"))
            subtracao = num1 - num2
            print("A subtração entre",num1,"-",num2,"é igual a",subtracao)
            decisao = input("Deseja continuar? (s/n):")
            
        case 3:
            num1 = int(input("Digite o primeiro numero:"))
            num2 = int(input("Digite o segundo numero:"))
            multiplicacao = num1 * num2
            print("A multiplicação entre",num1,"*",num2,"é igual a",multiplicacao)
            decisao = input("Deseja continuar? (s/n):")
           
        case 4:
            num1 = float(input("Digite o primeiro numero:"))
            num2 = float(input("Digite o segundo numero:"))
            while num2 == 0:
                print("Não é possível dividir por zero.")
                num2 = float(input("Digite o segundo numero:"))
            else:
                divisao = num1 / num2
                print("A divisão entre",num1,"/",num2,"é igual a",divisao)  
                decisao = input("Deseja continuar? (s/n):") 
                
        case 5:
            num2 = 0
            quantidade = int(input("Digite a quantidade de numeros:"))
            while quantidade == 0:
                print("Quantidade inválida. Digite um número positivo.")
                quantidade = int(input("Digite a quantidade de numeros:"))   
            while quantidade > contador:    
             num1 = float(input("Digite um numero:"))
             num2 = num2 + num1
             contador = contador + 1
            media = num2 / quantidade  
            print(num2,"/",quantidade,"=",media)
            decisao = input("Deseja continuar? (s/n):")
          
        case 6:
            num1 = float(input("Digite a base:"))
            num2 = float(input("Digite o expoente:"))
            potencia = num1 ** num2
            print(num1,"^",num2,"=",potencia)
            decisao = input("Deseja continuar? (s/n):")     
            
        case 7:
            print("Saindo da calculadora...")
            decisao = False
            

