h1 = int(input("Digite a hora 1: "))
m1 = int(input("Digite o minuto 1: "))
h2 = int(input("Digite a hora 2: "))
m2 = int(input("Digite o minuto 2: "))

somaH = h1 + h2
somaM = m1 + m2
if somaM >59:
    somaH += 1
    somaM %= 60
if somaH >= 36:
    somaH = somaH - 36
elif somaH >= 24:
    somaH = somaH - 24
elif somaH >= 12:
    somaH = somaH - 12
print(f"{somaH:02d}:{somaM:02d}h")