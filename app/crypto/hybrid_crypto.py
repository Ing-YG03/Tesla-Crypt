"""
Tesla Crypt
Hybrid Encryption Engine

Combina:

AES-256-GCM
+
RSA-3072-OAEP

"""

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


from app.crypto.aes_manager import AESManager



class HybridCryptoEngine:


    def __init__(self):

        self.aes = AESManager()



    def encrypt_file_data(
            self,
            data: bytes,
            public_key
    ):

        """
        Cifra información usando:

        AES -> archivo
        RSA -> clave AES
        """


        # 1.
        # Crear clave AES

        aes_key = self.aes.generate_key()



        # 2.
        # Cifrar archivo

        aes_result = self.aes.encrypt(

            data,

            aes_key

        )



        # 3.
        # Proteger AES con RSA

        encrypted_aes_key = public_key.encrypt(

            aes_key,


            padding.OAEP(

                mgf=padding.MGF1(

                    algorithm=hashes.SHA256()

                ),

                algorithm=hashes.SHA256(),

                label=None

            )

        )



        return {


            "encrypted_data":
                aes_result["ciphertext"],


            "nonce":
                aes_result["nonce"],


            "encrypted_key":
                encrypted_aes_key

        }




    def decrypt_file_data(

            self,

            encrypted_package,

            private_key

    ):


        """
        Recupera archivo original
        """



        # 1.
        # Recuperar AES Key


        aes_key = private_key.decrypt(


            encrypted_package["encrypted_key"],


            padding.OAEP(

                mgf=padding.MGF1(

                    algorithm=hashes.SHA256()

                ),


                algorithm=hashes.SHA256(),


                label=None

            )

        )



        # 2.
        # Descifrar archivo


        original = self.aes.decrypt(

            encrypted_package["encrypted_data"],

            encrypted_package["nonce"],

            aes_key

        )


        return original
