entrada01hr = int(input("Digite a primeira hora: "))
entrada01min = int(input("Digite o primeiro minuto: "))
entrada02hr = int(input("Digite a segunda hora: "))
entrada02min = int(input("Digite o segundo minuto: "))
hrstotal = ((entrada01hr*60+entrada02hr*60+entrada01min+entrada02min)/60)
hrint = ((entrada01hr*60+entrada02hr*60+entrada01min+entrada02min)//60)
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