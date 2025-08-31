# demonstraçao de como subir no github

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"IMC: {imc:.2f} → Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return f"IMC: {imc:.2f} → Peso adequado"
    elif 25 <= imc <= 29.9:
        return f"IMC: {imc:.2f} → Sobrepeso"
    elif 30 <= imc <= 34.9:
        return f"IMC: {imc:.2f} → Obesidade grau I"
    elif 35 <= imc <= 39.9:
        return f"IMC: {imc:.2f} → Obesidade grau II"
    else:
        return f"IMC: {imc:.2f} → Obesidade grau III"

# Entrada do usuário
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Saída
print(calcular_imc(peso, altura))


