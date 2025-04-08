entrada01hr = 21
entrada01min = 00
entrada02hr = 21
entrada02min = 00
hr1min = entrada01hr*60
hr2min = entrada02hr*60
mintotal = (hr1min+hr2min+entrada01min+entrada02min)
hrstotal = (mintotal/60)
hrsint = (mintotal//60)
hrfinal = hrsint-12
teste = (hrstotal-hrsint)
teste2 = teste*60
if hrfinal > 12:
    print(f"{hrfinal-12}:{teste2:.0f}")
else:
    print(f"{hrfinal}:{teste2:.0f}")