def calculadora(num1, num2, operacao):
    """
    Realiza a operação especificada entre dois números.

    Args:
        num1 (float): O primeiro número.
        num2 (float): O segundo número.
        operacao (int): O código da operação (1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão).

    Returns:
        float: O resultado da operação. Se o código de operação não for válido, retorna 0.
    """
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return 0
    else:
        print("Erro: Operação inválida. Use os códigos 1, 2, 3 ou 4.")
        return 0

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
codigo_operacao = int(input("Digite o código da operação (1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão): "))

resultado = calculadora(numero1, numero2, codigo_operacao)
print(f"Resultado: {resultado}")
