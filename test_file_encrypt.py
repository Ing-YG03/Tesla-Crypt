from app.crypto.rsa_manager import RSAKeyManager

from app.storage.encryption_service import EncryptionService



# Crear archivo prueba

with open(
    "prueba.txt",
    "w"
) as f:

    f.write(
        "Tesla Crypt archivo real"
    )



rsa = RSAKeyManager()


public = rsa.load_public_key()



service = EncryptionService()



service.encrypt_file(

    "prueba.txt",

    "prueba.txt.tesla",

    public

)



print(
    "Archivo cifrado correctamente"
)