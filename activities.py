def bigger_number(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2

def positive_negative(n1):
    if n1>0:
        return "valor positivo!"
    if n1<0:
        return "valor negativo!"
    if n1==0:
        return "valor neutro!"

def get_sex(sex):
    if sex.lower()[0]=="f": return "feminine"
    if sex.lower()[0]=="m": return "masculine"
    else: return "unknown"

def vowel_consonant(caracter):
    vowels=["a","e","i","o","u"]
    i=0
    while i<len(vowels):
        if caracter in vowels[i]: return caracter + "{0} is a vowel".format(caracter)
    return "{0} isn't a vowel".format(caracter)

def grade_verify(n1,n2,n3):
    grade=(n1+n2+n3)/3

    gradeMsg="Reprovado"
    if grade>=70:
        gradeMsg="Aprovado"
        if grade==100: gradeMsg = "Aprovado com Distinção"
    return gradeMsg

def biggerBetween(n1,n2,n3):
    n1 = int(input("Digite um numero inteiro\n"))
    n2 = int(input("Digite um numero inteiro\n"))
    n3 = int(input("Digite um numero inteiro\n"))

    if n1 == n2 and n1 == n3:
        print("Todos são iguais")
    elif n1 > n2 and n1 > n3:
        print(f"Maior: {n1}")
    elif n2 > n1 and n2 > n3:
        print(f"Maior: {n2}")
    else:
        print(f"Maior: {n3}")

def biggerAndSmaller(n1,n2,n3):
    n1 = int(input("Digite um numero inteiro\n"))
    n2 = int(input("Digite um numero inteiro\n"))
    n3 = int(input("Digite um numero inteiro\n"))

    if n1 == n2 and n1 == n3:
        print("Todos são iguais")
    elif n1 < n2 and n1 < n3:
        print(f"Menor: {n1}")
    elif n2 < n1 and n2 < n3:
        print(f"Menor: {n2}")
    else:
        print(f"Menor: {n3}")

def cheapest(n1,n2,n3):
    n1 = float(input("Digite o preço de um produto\n"))
    n2 = float(input("Digite o preço de um produto\n"))
    n3 = float(input("Digite o preço de um produto\n"))

    if n1 == n2 and n1 == n3:
        print("Todos os preços são iguais")
    elif n1 < n2 and n1 < n3:
        print(f"Menor preço: {n1:.2}")
    elif n2 < n1 and n2 < n3:
        print(f"Menor preço: {n2:.2}")
    else:
        print(f"Menor preço: {n3:.2}")

def orderDescrese(n1,n2,n3):
    n1n2=(n1>n2)
    n2n3=(n2>n3)
    nums=[n1,n2,n3]

    if n1n2!=n2n3


    if n1n2==n2n3:


def helloMsg():
    t = str(input("Qual turno você estuda?\n" +
                  "[M] - Matutino\n" +
                  "[V] - Vespertino\n" +
                  "[N] - Noturno\n" +
                  ">> "
                  ))

    if t.lower() == 'm':
        print("Bom dia!")
    elif t.lower() == 'v':
        print("Boa tarde!")
    elif t.lower() == 'n':
        print("Boa noite!")
    else:
        print("Valor inválido!")

