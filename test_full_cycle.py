from app.crypto.rsa_manager import RSAKeyManager

from app.storage.encryption_service import EncryptionService

from app.storage.decryption_service import DecryptionService



# Crear archivo original

original_text = "Tesla Crypt E2EE funcionando"


with open(

    "original.txt",

    "w"

) as file:

    file.write(original_text)



rsa = RSAKeyManager()



public_key = rsa.load_public_key()

private_key = rsa.load_private_key()



# CIFRAR


encryptor = EncryptionService()



encryptor.encrypt_file(

    "original.txt",

    "original.txt.tesla",

    public_key

)



print(
    "Cifrado terminado"
)



# DESCIFRAR


decryptor = DecryptionService()



decryptor.decrypt_file(

    "original.txt.tesla",

    "restaurado.txt",

    private_key

)



print(
    "Descifrado terminado"
)



# Verificación

with open(

    "restaurado.txt",

    "r"

) as file:

    result = file.read()



print(
    result
)
