import hashlib
import os

os.system("clear")

print("\033[34m   ___ ___               .__   ___.                   \033[0m")
print("\033[34m  /   |   \_____    _____|  |__\_ |__   _______  ___  \033[0m")
print("\033[34m /    ~    \__  \  /  ___/  |  \| __ \ /  _ \  \/  /  \033[0m")
print("\033[34m \    Y    // __ \_\___ \|   Y  \ \_\ (  <_> >    <   \033[0m")
print("\033[34m  \___|_  /(____  /____  >___|  /___  /\____/__/\_ \  \033[0m")
print("\033[34m        \/      \/     \/     \/    \/            \/  \033[0m")


filename = input("\033[1m\n[+] Ingresa la ubicación del archivo para analizar: \033[0m")
hasher = hashlib.sha256()

with open(filename, "rb") as f:
    # Leemos el archivo en bloques para que funcione con archivos grandes
    block = f.read(4096)
    while len(block) > 0:
        hasher.update(block)
        block = f.read(4096)

hash_value = hasher.hexdigest()
print("\033[1m\nHash SHA-256 de\033[0m", filename, ":", hash_value)

with open('hash.txt', 'r') as f:
    lista_hashes = f.readlines()

lista_hashes = [hash.strip() for hash in lista_hashes]

for i, hash in enumerate(lista_hashes):
    if hash == hash_value:
        print(f"\033[1mEl hash es malicioso\033[0m")
        break
else:
    print("\033[1mEl hash no es malicioso\033[0m")
