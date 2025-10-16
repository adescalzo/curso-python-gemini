edad: int = 25
tiene_carnet: bool = True

# --- Operador `and` ---
if edad >= 18 and tiene_carnet:
    print("[and] Puedes conducir un coche.")
else:
    print("[and] NO puedes conducir.")

# --- Operador `or` ---
es_fin_de_semana: bool = True
estoy_de_vacaciones: bool = False

if es_fin_de_semana or estoy_de_vacaciones:
    print("[or] Hoy no se trabaja.")
else:
    print("[or] A trabajar.")

# --- Operador `not` ---
es_festivo: bool = False

if not es_festivo:
    print("[not] No es festivo, así que es un día laborable.")
