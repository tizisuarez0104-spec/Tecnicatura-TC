"""## palabra reservada break
for letra in "el mundo de alemania":
    if letra == "e":
        print(f"Letra encontrada: {letra}")
        break
else:
    print("fin de ciclo for")"""

#palabra reservada continue
for i in range(6):
    if i % 2== 0:
        print(f"valor {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"valor {i}")