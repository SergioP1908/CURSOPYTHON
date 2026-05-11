'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Todas las pizzas llevan de base la masa clásica, mozzarella y tomate. Los ingredientes 
extra para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento, aceitunas, cebolla y tofu.
Ingredientes no vegetarianos: Pepperoni, jamón, bacon y atún.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para 
que elija. Solo se pueden eligir dos ingredientes, además de la mozzarella y el tomate 
que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida 
es vegetariana o no y el listado de todos los ingredientes que lleva.'''


tipo = input("Quieres pizza vegetariana? (s/n): ")

print("Ingredientes base: mozzarella, tomate")

if tipo == "s":
    print("Ingredientes vegetarianos: pimiento, aceitunas, cebolla, tofu")
    
    ing1 = input("Elige el primer ingrediente: ")
    ing2 = input("Elige el segundo ingrediente: ")

    print("Tu pizza es vegetariana y lleva: mozzarella, tomate, " + ing1 + ", " + ing2)

else:
    print("Ingredientes no vegetarianos: pepperoni, jamon, bacon, atun")
    
    ing1 = input("Elige el primer ingrediente: ")
    ing2 = input("Elige el segundo ingrediente: ")

    print("Tu pizza no es vegetariana y lleva: mozzarella, tomate, " + ing1 + ", " + ing2)