"""
Tesla Crypt
Encryption Service

Orquesta:

Archivo
AES
RSA
Contenedor
"""


from app.storage.file_manager import FileManager

from app.storage.container_format import TeslaContainer

from app.crypto.hybrid_crypto import HybridCryptoEngine




class EncryptionService:



    def __init__(self):

        self.files = FileManager()

        self.container = TeslaContainer()

        self.crypto = HybridCryptoEngine()




    def encrypt_file(

            self,

            input_file,

            output_file,

            public_key

    ):


        # Leer archivo original

        data = self.files.read_file(

            input_file

        )



        # Metadata

        metadata = self.files.get_metadata(

            input_file

        )



        # Cifrado híbrido

        encrypted = self.crypto.encrypt_file_data(

            data,

            public_key

        )



        # Crear contenedor

        self.container.create_container(

            output_file,

            encrypted,

            metadata

        )


        return True