def calculadora(operacao_str):
    try:
        resultado = eval(operacao_str)  # Usando a função eval para avaliar a expressão
        return resultado
    except Exception:
        return "Erro: Operação inválida"

# Exemplo de uso:
operacao = input("Digite sua operação: ")
resultado = calculadora(operacao)
print("Resultado:", resultado)