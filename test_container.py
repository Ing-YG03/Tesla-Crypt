from app.crypto.rsa_manager import RSAKeyManager
from app.crypto.hybrid_crypto import HybridCryptoEngine
from app.storage.container_format import TeslaContainer



rsa = RSAKeyManager()


public = rsa.load_public_key()


engine = HybridCryptoEngine()



data = b"Archivo Tesla protegido"



encrypted = engine.encrypt_file_data(

    data,

    public

)



container = TeslaContainer()



container.create_container(

    "archivo.tesla",

    encrypted,

    {

        "name":"archivo.txt",

        "size":len(data)

    }

)



print(
    "Contenedor creado"
)



result = container.read_container(

    "archivo.tesla"

)



print(

result["metadata"]

)
