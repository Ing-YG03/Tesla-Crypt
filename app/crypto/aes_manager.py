"""
Tesla Crypt
AES-256-GCM Encryption Module

Responsable de:
- Cifrado simétrico
- Descifrado simétrico
- Integridad del contenido
"""


import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM



class AESManager:


    AES_KEY_SIZE = 32

    NONCE_SIZE = 12



    def generate_key(self):

        """
        Genera clave AES-256

        Retorna:
        bytes de 32 posiciones
        """

        return os.urandom(
            self.AES_KEY_SIZE
        )



    def generate_nonce(self):

        """
        Genera IV/Nonce seguro

        AES-GCM recomienda 12 bytes
        """

        return os.urandom(
            self.NONCE_SIZE
        )



    def encrypt(
            self,
            data: bytes,
            key: bytes
    ):

        """
        Cifra información usando AES-256-GCM


        Retorna:

        ciphertext
        nonce
        """

        nonce = self.generate_nonce()


        aes = AESGCM(key)


        ciphertext = aes.encrypt(

            nonce,

            data,

            None

        )


        return {

            "ciphertext": ciphertext,

            "nonce": nonce

        }



    def decrypt(

            self,

            ciphertext: bytes,

            nonce: bytes,

            key: bytes

    ):


        """
        Descifra AES-256-GCM
        """

        aes = AESGCM(key)


        plaintext = aes.decrypt(

            nonce,

            ciphertext,

            None

        )


        return plaintext