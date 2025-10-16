variable_global: str = "Soy global"

def mi_funcion() -> None:
    variable_local: str = "Soy local"
    print(f"Dentro de la función, puedo ver la variable local: '{variable_local}'")
    print(f"Dentro de la función, también puedo leer la variable global: '{variable_global}'")

print(f"Fuera de la función, puedo leer la variable global: '{variable_global}'")
mi_funcion()

# La siguiente línea daría un error (NameError) porque la variable_local no existe aquí.
# print(f"Fuera de la función, no puedo ver la variable local: {variable_local}")
