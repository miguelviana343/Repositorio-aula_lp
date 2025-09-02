def exibir_menu():
    print("\n---Calculadora---")
    print("Opção 1: Somar")
    print("Opção 2: Subtrair")
    print("Sair")

def soma(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            n1 = float(input("Escreva um número: "))
            n2 = float(input("Escreva outro número:"))
            resultado = soma(n1, n2)
            print(f"Resultado: {resultado}")    
        elif escolha == "2":
            n1 = float(input("Escreva um número: "))
            n2 = float(input("Escreva outro número:"))
            resultado = subtrair(n1, n2)
            print(f"Resultado: {resultado}")
        elif escolha == "3":
            print("Programaa encerrado")
            break


