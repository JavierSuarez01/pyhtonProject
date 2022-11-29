'''
CALCULADORA DE IMC
IMC = PESO / (ALTURA * ALTURA)
peso < 19: Delgadez
peso entre 20 y 25: normal
entre 26 y 30: Sobrepeso
> a 30: Obesidad '''

peso = float(input("Ingrese el Peso en KG"))
alturaEnCM = int(input('Ingrese la altura en CM'))
alturaEnMTS = alturaEnCM /100
imc = peso / (alturaEnMTS * alturaEnMTS)

print('El Indice de Masa Corporal es: ' + str(imc) )

if imc < 20:
    print('Iniciar Control por Delgadez')
if imc >= 20 and imc < 25:
    print('Su peso es Normal sigue asi XD XD')
if imc >= 25 and imc < 30:
    print('Estas Manejando Sobrepeso, Inicia Tratamiento')
if imc >= 30:
    print('Inicia tratamiento para tu obesidad inmediatamente')


