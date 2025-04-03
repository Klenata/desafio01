entrada01hr = int(input("Digite a primeira hora: "))
entrada01min = int(input("Digite o primeiro minuto: "))
entrada02hr = int(input("Digite a segunda hora: "))
entrada02min = int(input("Digite o segundo minuto: "))
hr1min = entrada01hr*60
hr2min = entrada02hr*60
mintotal = (hr1min+hr2min+entrada01min+entrada02min)
hrstotal = (mintotal/60)
hrsint = (mintotal//60)
hrfinal = hrsint-12
mindec = (hrstotal-hrsint)
minfinal = mindec*60
if hrfinal >= 12:
    hrfinal = hrfinal-12
else:
    print(f"{hrfinal}:{minfinal:.0f}h")
if hrfinal >= 12:
    hrfinal = hrfinal-12
else:
    print(f"{hrfinal}:{minfinal:.0f}h")
if hrfinal >= 12:
    hrfinal = hrfinal-12
else:
    print(f"{hrfinal}:{minfinal:.0f}h")


print(f"{hr1min} hr1min")
print(f"{hr2min} hr2min")
print(f"{mintotal} mintotal")
print(f"{hrstotal} hrstotal")
print(f"{hrsint} hrsint")
print(f"{hrfinal} hrfinal")
print(f"{mindec} teste")
print(f"{minfinal:.0f} teste2")
print(" ")
print(f"{hrfinal}:{minfinal:.0f}h")