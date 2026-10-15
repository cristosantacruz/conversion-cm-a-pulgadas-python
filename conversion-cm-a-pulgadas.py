# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en centimetros

medida_en_cms = float(input("Ingrese la medida de la pieza del mueble en centimetros: "))

# Paso 2: Convertir las medidas de centimetros a pulgadas

medida_en_pulgadas = medida_en_cms / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario

print("La medida de la pieza del mueble es de", medida_en_pulgadas, "pulgadas")