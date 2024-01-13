# 1-
def maximo_2(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2
print(maximo_2(39,39))
# 2-
def maximo_3(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2> num3):
        return num2
    else:
        return num3
print(maximo_3(300,200,1000))

# 3-
def largo_list(lista):
    L=0
    for i in lista:
        L+=1
    return L

mi_lista=["Pepe","Roberto","Juan"]

print(largo_list(mi_lista))

# 4- 

def is_vocal(carac):
    carac=carac.upper()
    if()
