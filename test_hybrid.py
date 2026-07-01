from app.crypto.rsa_manager import RSAKeyManager

from app.crypto.hybrid_crypto import HybridCryptoEngine



rsa = RSAKeyManager()


public_key = rsa.load_public_key()

private_key = rsa.load_private_key()



engine = HybridCryptoEngine()



archivo = b"Archivo secreto Tesla Crypt"



encrypted = engine.encrypt_file_data(

    archivo,

    public_key

)



print(
    "Archivo cifrado correctamente"
)



decrypted = engine.decrypt_file_data(

    encrypted,

    private_key

)



print(

    decrypted.decode()

)
