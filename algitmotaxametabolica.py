print ("Algoritmo de calculo para taxa metabólica basal masculina")
peso = float (input ("Insira o seu peso em Quilos: "))
altura = float (input ("Insira sua altura em Centímetros: "))
idade = float (input ("Insira sua Idade: "))

#Formula de taxa metabólica basal para homens
tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
print ("Sua taxa metabólica basal é de: ",tmb,"Kcal")
