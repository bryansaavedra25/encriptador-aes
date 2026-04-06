import argparse
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

KEY_FILE = "key.bin"

# =========================
# Generar y guardar llave
# =========================
def generate_key():
    key = get_random_bytes(32)  # AES-256
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("[+] Llave generada y guardada en key.bin")
    return key

# =========================
# Cargar llave existente
# =========================
def load_key():
    try:
        with open(KEY_FILE, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print("[-] No existe key.bin. Generando nueva llave...")
        return generate_key()

# =========================
# Cifrar archivo
# =========================
def encrypt_file(input_file):
    key = load_key()

    with open(input_file, "rb") as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    output_file = input_file + ".enc"

    with open(output_file, "wb") as f:
        f.write(cipher.iv)  # Guardamos IV
        f.write(ciphertext)

    print(f"[+] Archivo cifrado guardado como: {output_file}")

# =========================
# Descifrar archivo
# =========================
def decrypt_file(input_file):
    key = load_key()

    with open(input_file, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    output_file = input_file.replace(".enc", ".dec.txt")

    with open(output_file, "wb") as f:
        f.write(plaintext)

    print(f"[+] Archivo descifrado guardado como: {output_file}")

# =========================
# CLI
# =========================
def main():
    parser = argparse.ArgumentParser(description="Herramienta de cifrado AES")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Acción a realizar")
    parser.add_argument("file", help="Archivo de entrada")

    args = parser.parse_args()

    if args.action == "encrypt":
        encrypt_file(args.file)
    elif args.action == "decrypt":
        decrypt_file(args.file)

if __name__ == "__main__":
    main()
