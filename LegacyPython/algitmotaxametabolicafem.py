print ("Algoritmo de calculo para taxa metabólica basal feminina")
peso = float (input ("Insira o seu peso em Quilos: "))
altura = float (input ("Insira sua altura em Centímetros: "))
idade = float (input ("Insira sua Idade: "))

#Formula de taxa metabólica basal para mulheres
tmb = 66 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
print ("Sua taxa metabólica basal é de: ",tmb,"Kcal")

#Bloco de instruções para calculo da taxa metabólica basal de acordo com nível de atividade física
print ("Qual seu nível de atividade física?")
print ("Responda de acordo com as intruções:")
print ("Nível Leve(L): Atividade física com duração de 30 minutos, praticada de 1 a 2 vezes por semana")
print ("Nível Moderado(M): Atividade física com duração acima de 30 minutos, praticada de 2 a 4 vezes por semana")
print ("Nível Intenso(I): Atividade física com duração acima de 1 hora, praticada 5 vezes por semana ou mais")
nivel = (input("Insira o nivel de atividade, 'L', 'M' ou 'I':"))

#Nível de atividade física leve
if nivel == str("L") or nivel == str("l"):
    atividade = tmb*1.56
    print("Sua taxa metabólica com atividade física leve é de: ", atividade,"Kcal")
    
#Nível de atividade física moderada 
elif nivel == str("M") or nivel == str("m"):
    atividade = tmb*1.64
    print("Sua taxa metabólica com atividade física moderada é de: ",atividade,"Kcal")
    
#Nível de atividade física intensa    
elif nivel == str("I") or nivel == str("i"):
    atividade = tmb*1.82
    print("Sua taxa metabólica com atividade física intensa é de: ", atividade,"Kcal")
