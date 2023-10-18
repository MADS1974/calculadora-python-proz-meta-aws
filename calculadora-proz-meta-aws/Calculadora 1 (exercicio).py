def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

    if operacao == 1:  # Soma
        resultado = num1 + num2
    elif operacao == 2:  # Subtração
        resultado = num1 - num2
    elif operacao == 3:  # Multiplicação
        resultado = num1 * num2
    elif operacao == 4:  # Divisão
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
    else:
        resultado = 0  # Operação não existente

    return resultado

# Exemplo de uso:
resultado = calculadora()
print("Resultado:", resultado)

