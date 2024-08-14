def validaCPF(cpf):
    #extrai os dígitos do CPF e transforma em inteiro
    num1 = int(cpf[0])
    num2 = int(cpf[1])
    num3 = int(cpf[2])
    num4 = int(cpf[4])
    num5 = int(cpf[5])
    num6 = int(cpf[6])
    num7 = int(cpf[8])
    num8 = int(cpf[9])
    num9 = int(cpf[10])
    num10 = int(cpf[12])
    num11 = int(cpf[13])

    #Validação dos CPFs inválidos conhecidos
    if(num1 == num2) and (num2 == num3) and (num3 == num4) and (num4 == num5) and (num5 == num6) and (num6 == num7) and (num7 == num8) and (num8 == num9) and (num9 == num10) and (num10 == num11):
      return False
    else:
        soma1 = num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 + num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2

        resto1 = (soma1 * 10) % 11

        if resto1 == 10:
           resto1 = 0
           
        soma2 = num1 * 11 + num2 * 10 + num3 * 9 + num4 * 8 + num5 * 7 + num6 * 6 + num7 * 5 + num8 * 4 + num9 * 3 + num10 * 2
        
        resto2 = (soma2 * 10) % 11

        if resto2 == 10:
           resto2 = 0
        
        if(resto1 == num10) and (resto2 == num11):
            return True
        else:
            return False

def main():      

    cpf = input("\nInsira o CPF (Formato: XXX.XXX.XXX-XX): \n")

    #validação se o cpf tem 14 caracteres para poder começar:
    while len(cpf) != 14:
        print("CPF Inválido, adicione o cpf no formato correto.")
        cpf = input("Insira o CPF (Formato: XXX.XXX.XXX-XX)")

    #Verificação de um CPF inválido
    if validaCPF(cpf) == True:
        print(f"O CPF {cpf} é válido!")
    else:
        print(f"O CPF {cpf} é inválido!")

main()
executar_novamente = int(input("\nGostaria de executar novamente? Responda 1 para Sim e 2 para Não: \n"))

if executar_novamente == 1:
    main()
elif executar_novamente == 2:
    print("Tchau tchau")
else:
    print("Digite 1 para Sim e 2 para Não")
    print(executar_novamente)






    
