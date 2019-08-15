import random   
datos =[[1,1,1],[1,0,0],[0,1,0],[0,0,0]]
pesos = [random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)]
aprendiendo = True
salidaEntera = 0
iteracion=0
tasaAprende = 0.3
iteraciones = 0
while(aprendiendo==True):
    iteracion=iteracion + 1
    aprendiendo=False
    for cont in range(0,4):
        salidaReal =  (datos[cont][0] * pesos[0] + datos[cont][1] * pesos[1] + pesos[2])
        #print("salida real: ", datos[cont][0], " * ", pesos[0], " + ", datos[cont][1], " * ", pesos[1], " + ", pesos[2])
        #print("salida real: ",salidaReal)
        if salidaReal > 0:
            salidaEntera = 1
        else:
            salidaEntera = 0
        salidaEntera = int(salidaEntera)
        print(salidaEntera)
        error =  int(datos[cont][2] - salidaEntera)
        if (error != 0):
            pesos[0] += tasaAprende * error * datos[cont][0]
            pesos[1] += tasaAprende * error * datos[cont][1]
            pesos[2] += tasaAprende * error *1
            aprendiendo = True


    if aprendiendo == False:
        break
print("iteraciones: " , iteracion)
print("peso 1: ", pesos[0])
print("peso 2: ", pesos[1])
print("peso 3: ", pesos[2])
for cont in range (0,4):
    salidaReal= datos[cont][0] * pesos[0] + datos[cont][1] * pesos[1] + pesos[2]
    #print("formula: ( datos[cont][0]  *  pesos[0] + datos[cont][1] * pesos[1] + pesos[2])")
    #print("formula: (", datos[cont][0] , " * ", pesos[0], " + ", datos[cont][1], " * ", pesos[1], " + ", pesos[2], " )")
    #print(salidaReal)
    if salidaReal > 0 :
        salidaEntera = 1
    else:
        salidaEntera = 0
    print("entradas: ", datos[cont][0] , " y " ,datos[cont][1] , " = " , datos[cont][2] , "perceptron: " , salidaEntera)
