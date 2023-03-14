numero = int(input("Digite o numero que deseja que seja feito o calculo: "))
fibonacci = [0,1]

try:
    while fibonacci[-1] < numero and type(numero) == int:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    if numero in fibonacci:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

except:
    print("O valor digitado não é um numero")






