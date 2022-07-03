from random import choices
quant = int(input('Digite a quantidade de caracteres que dever ter a senha: '))
caractes  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&'
gerador = choices(caractes, k = quant)
sa = str(gerador)
print(sa[2::5])
