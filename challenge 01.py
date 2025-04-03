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
minfinal = mindec * 60
print(" ")
if hrfinal >= 12:
    hrfinal = hrfinal-12
else:
    hrfinal = hrfinal+0
if hrfinal >= 12:
    hrfinal = hrfinal-12
else:
    hrfinal = hrfinal+0
if hrfinal >= 12:
    hrfinal = hrfinal-12
else:
    hrfinal = hrfinal+0
if minfinal >= 10:
    print(f"{hrfinal:02d}:{minfinal:.0f}h")
else:
    print(f"{hrfinal:02d}:0{minfinal:.0f}h")