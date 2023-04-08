def taxa_homem(p,a,i):
    tmb = 66 + (13.7 * p) + (5 * a) - (6.8 * i)
    print(tmb,"Kcal")
    
def taxa_mulher(p,a,i):
    tmb = 66 + (9.6 * p) + (1.8 * a) - (4.7 * i)
    print(tmb,"Kcal")
    
sex = str (input("Você é homem ou mulher? Responda com H para homem e M para mulher "))
p = int (input("Qual o seu peso em Kg? "))
a = int (input("Qual é a sua altura em centímetros? "))
i = int (input("Qual é a sua idade? "))

if sex == "homem" or sex == "h" or sex == "Homem" or sex == "H":
    taxa_homem(p,a,i)
    
if sex == "mulher" or sex == "m" or sex == "Mulher" or sex == "M":
    taxa_mulher(p,a,i)