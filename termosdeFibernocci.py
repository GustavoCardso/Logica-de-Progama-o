def fibonacci_sequence(n):
    fib_sequence = [0, 1]  # Começando a sequência com 0 e 1
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Próximo número é a soma dos dois anteriores
        if next_fib > n:  # Se o próximo número for maior que n, paramos
            break
        fib_sequence.append(next_fib)  # Adiciona o próximo número à sequência
    return fib_sequence

# Função principal
def main():
    # Entrada do usuário
    num = int(input("Informe um número: "))  # O usuário informa um número
    
    # Calcula a sequência de Fibonacci
    fib_sequence = fibonacci_sequence(num)
    
    # Verifica se o número informado pertence à sequência
    if num in fib_sequence:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

# Chama a função principal
if __name__ == "__main__":
    main()
