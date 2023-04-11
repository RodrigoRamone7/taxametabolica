def taxa_homem(p,a,i):
    tmb = 66 + (13.8 * p) + (5 * a) - (6.8 * i)
    print("Sua taxa metabólica basal é de", tmb,"Kcal")
    nivel_atividade_H(tmb)
    
def taxa_mulher(p,a,i):
    tmb = 655 + (9.6 * p) + (1.9 * a) - (4.7 * i)
    print("Sua taxa metabólica basal é de", tmb,"Kcal")
    nivel_atividade_M(tmb)
    
def nivel_atividade_H(tmb):
    a_leve = tmb*1.55
    a_mod = tmb*1.78
    a_int = tmb*2.10
    print("Sua taxa metabólica basal em nível de atividade leve é de", a_leve,"Kcal")
    print("Sua taxa metabólica basal em nível de atividade moderada é de", a_mod,"Kcal")
    print("Sua taxa metabólica basal em nível de atividade intensa é de", a_int,"Kcal")
    
def nivel_atividade_M(tmb):
    a_leve = tmb*1.56
    a_mod = tmb*1.64
    a_int = tmb*1.82
    print("Sua taxa metabólica basal em nível de atividade leve é de", a_leve,"Kcal")
    print("Sua taxa metabólica basal em nível de atividade moderada é de", a_mod,"Kcal")
    print("Sua taxa metabólica basal em nível de atividade intensa é de", a_int,"Kcal")
    
sex = str (input("Você é homem ou mulher? Responda com H para homem e M para mulher "))
p = int (input("Qual o seu peso em Kg? "))
a = int (input("Qual é a sua altura em centímetros? "))
i = int (input("Qual é a sua idade? "))

if sex == "homem" or sex == "h" or sex == "Homem" or sex == "H":
    taxa_homem(p,a,i)
    
if sex == "mulher" or sex == "m" or sex == "Mulher" or sex == "M":
    taxa_mulher(p,a,i)