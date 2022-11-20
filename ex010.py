real = float(input('Quanto dinheiro você tem na carteira? '))

dolar = real / 5.37
euro = real / 5.55

print('com R${:.2f} reais você pode ter US${:.2f} de dólares '.format(real, dolar))
print('com R${:.2f} reais você pode ter €{:.2f} de euros '.format(real, euro))