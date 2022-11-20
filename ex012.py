preço = float(input('Qual o preço do produto? '))
novo = preço - (preço * 5/100)

print('O produto de custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preço, novo))