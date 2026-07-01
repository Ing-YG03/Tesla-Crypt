from app.crypto.aes_manager import AESManager



aes = AESManager()



mensaje = b"Tesla Crypt funcionando"



key = aes.generate_key()



resultado = aes.encrypt(
    mensaje,
    key
)



print(
    "Cipher:",
    resultado["ciphertext"]
)



descifrado = aes.decrypt(

    resultado["ciphertext"],

    resultado["nonce"],

    key
)



print(
    "Original:",
    descifrado.decode()
)
