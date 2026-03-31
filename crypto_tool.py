from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import argparse

def generar_llave():
    key = get_random_bytes(32)
    with open("llave.key", "wb") as f:
        f.write(key)
    print("Llave generada")

def cifrar(archivo):
    with open("llave.key", "rb") as f:
        key = f.read()

    with open(archivo, "rb") as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open("archivo.cifrado", "wb") as f:
        f.write(cipher.nonce + tag + ciphertext)

    print("Archivo cifrado")

def descifrar():
    with open("llave.key", "rb") as f:
        key = f.read()

    with open("archivo.cifrado", "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    with open("archivo_descifrado.txt", "wb") as f:
        f.write(data)

    print("Archivo descifrado")

parser = argparse.ArgumentParser()
parser.add_argument("accion", choices=["generar", "cifrar", "descifrar"])
parser.add_argument("--archivo")

args = parser.parse_args()

if args.accion == "generar":
    generar_llave()
elif args.accion == "cifrar":
    cifrar(args.archivo)
elif args.accion == "descifrar":
    descifrar()