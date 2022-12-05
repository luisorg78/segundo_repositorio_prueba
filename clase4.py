#actividad entregada en la clase 4
#lista=[expresion for elementos in iterable]
cuadros=[]
for i in range(10):
    cuadros.append(i**2)
    
cuadrados2=[i**2 for i in range(10)]



def elevar2(i):
    return i**2
cuadrados3=[elevar2(i) for i in range(10)]

print(cuadros," ",cuadrados2," ",cuadrados3)


#con condicion
frase="cago en to"
letras_o=[i for i in frase if i=='o'] #if
print(letras_o)

letras_o_=[i if i=='o' else '-' for i in frase] #if-else
print(letras_o_)



#fin del código
