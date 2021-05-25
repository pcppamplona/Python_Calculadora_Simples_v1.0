def soma(a, b):
    return a + b

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

operacao = input("\n+:Soma\n-:Subtração\n*:Subtração\n/:Divisão\n**:expoente\n")
if operacao == '+':
    resultado = soma(a, b)
elif operacao == '-':
    resultado = a - b
elif operacao == '*':
    resultado = a * b
elif operacao == '/':
    resultado = a//b
elif operacao == '**':
    resultado = a ** b
print(resultado)
