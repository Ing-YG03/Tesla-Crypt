"""
Tesla Crypt
Decryption Service

Restaura archivos desde
contenedores .tesla
"""


from app.storage.file_manager import FileManager

from app.storage.container_format import TeslaContainer

from app.crypto.hybrid_crypto import HybridCryptoEngine





class DecryptionService:



    def __init__(self):

        self.files = FileManager()

        self.container = TeslaContainer()

        self.crypto = HybridCryptoEngine()




    def decrypt_file(

            self,

            encrypted_file,

            output_file,

            private_key

    ):


        # Leer contenedor

        package = self.container.read_container(

            encrypted_file

        )



        # Recuperar archivo original

        decrypted_data = self.crypto.decrypt_file_data(

            package,

            private_key

        )



        # Escribir resultado

        self.files.write_file(

            output_file,

            decrypted_data

        )


        return True
