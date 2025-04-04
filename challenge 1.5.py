hr1 = int(input("Digite a primeira hora: "))
min1 = int(input("Digite o primeiro minuto: "))
hr2 = int(input("Digite a segunda hora: "))
min2 = int(input("Digite o segundo minuto: "))
hrstotal = ((hr1*60+hr2*60+min1+min2)/60)
hrint = ((hr1*60+hr2*60+min1+min2)//60)
minfinal = ((hrstotal-hrint)*60)
if hrint >= 12:
    hrfinal = hrint-12
else:
    hrfinal = hrint+0
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
print(f"{hrfinal:.0f}:{minfinal:.0f}h")