# Descripcion.
print("Este programa va a convertir las todas las vocales de su oracion en i.")
# Toma la frase a transformar.
input = input("Escriba su oracion: ")
# Transforma cada vocal en i.
input = input.replace("a", "i")
input = input.replace("e", "i")
input = input.replace("o", "i")
input = input.replace("u", "i")
input = input.replace("A", "I")
input = input.replace("E", "I")
input = input.replace("O", "I")
input = input.replace("I", "I")
# Print los resultados.
print()
print("Su nueva oracion es: ")
print(input)
