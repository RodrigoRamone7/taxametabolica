def taxa_homem(p,a,i):
    tmb = 66 + (13.8 * p) + (5 * a) - (6.8 * i)
    tmbf = '{:,.2f}'.format(tmb).replace(',', '_').replace('.', ',').replace('_','.')
    print(f"Sua taxa metabólica basal é de {tmbf} Kcal")
    nivel_atividade_H(tmb)
    
def taxa_mulher(p,a,i):
    tmb = 655 + (9.6 * p) + (1.9 * a) - (4.7 * i)
    tmbf = '{:,.2f}'.format(tmb).replace(',', '_').replace('.', ',').replace('_','.')
    print(f"Sua taxa metabólica basal é de {tmbf} Kcal")
    nivel_atividade_M(tmb)
    
def nivel_atividade_H(tmb):
    a_leve = tmb*1.55
    a_mod = tmb*1.78
    a_int = tmb*2.10
    a_levef = '{:,.2f}'.format(a_leve).replace(',', '_').replace('.', ',').replace('_','.')
    a_modf = '{:,.2f}'.format(a_mod).replace(',', '_').replace('.', ',').replace('_','.')
    a_intf = '{:,.2f}'.format(a_int).replace(',', '_').replace('.', ',').replace('_','.')
    print(f"Sua taxa metabólica basal em nível de atividade leve é de {a_levef} Kcal")
    print(f"Sua taxa metabólica basal em nível de atividade moderada é de {a_modf} Kcal")
    print(f"Sua taxa metabólica basal em nível de atividade intensa é de {a_intf} Kcal")
    
def nivel_atividade_M(tmb):
    a_leve = tmb*1.56
    a_mod = tmb*1.64
    a_int = tmb*1.82
    a_levef = '{:,.2f}'.format(a_leve).replace(',', '_').replace('.', ',').replace('_','.')
    a_modf = '{:,.2f}'.format(a_mod).replace(',', '_').replace('.', ',').replace('_','.')
    a_intf = '{:,.2f}'.format(a_int).replace(',', '_').replace('.', ',').replace('_','.')
    print(f"Sua taxa metabólica basal em nível de atividade leve é de {a_levef} Kcal")
    print(f"Sua taxa metabólica basal em nível de atividade moderada é de {a_modf} Kcal")
    print(f"Sua taxa metabólica basal em nível de atividade intensa é de {a_intf} Kcal")
    
sex = str (input("Você é homem ou mulher? Responda com H para homem e M para mulher "))
p = int (input("Qual o seu peso em Kg? "))
a = int (input("Qual é a sua altura em centímetros? "))
i = int (input("Qual é a sua idade? "))

if sex == "homem" or sex == "h" or sex == "Homem" or sex == "H":
    taxa_homem(p,a,i)
    
if sex == "mulher" or sex == "m" or sex == "Mulher" or sex == "M":
    taxa_mulher(p,a,i)