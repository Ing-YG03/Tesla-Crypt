from app.crypto.rsa_manager import (
    RSAKeyManager,
    generate_aes_key
)


manager = RSAKeyManager()


manager.generate_keys()


print("RSA generado correctamente")


aes_key = generate_aes_key()


print(
    "AES-256 generado:",
    len(aes_key),
    "bytes"
)