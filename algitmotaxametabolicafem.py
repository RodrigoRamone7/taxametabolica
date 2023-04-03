print ("Algoritmo de calculo para taxa metabólica basal feminina")
peso = float (input ("Insira o seu peso em Quilos: "))
altura = float (input ("Insira sua altura em Centímetros: "))
idade = float (input ("Insira sua Idade: "))

#Formula de taxa metabólica basal para mulheres
tmb = 66 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
print ("Sua taxa metabólica basal é de: ",tmb,"Kcal")
