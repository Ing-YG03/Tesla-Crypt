"""
Tesla Crypt
RSA Key Management Module

Responsable de:
- Generación de claves RSA
- Gestión de claves PEM
- Generación de claves AES-256
"""

from pathlib import Path
import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class RSAKeyManager:

    def __init__(self, key_directory="keys"):
        self.key_directory = Path(key_directory)

        self.private_key_path = (
            self.key_directory / "private.pem"
        )

        self.public_key_path = (
            self.key_directory / "public.pem"
        )


    def generate_keys(self, key_size=3072):

        """
        Genera un par RSA:
        - Clave privada
        - Clave pública
        """

        self.key_directory.mkdir(
            exist_ok=True
        )


        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )


        public_key = private_key.public_key()


        # Guardar privada

        private_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,

            format=serialization.PrivateFormat.PKCS8,

            encryption_algorithm=
            serialization.NoEncryption()
        )


        with open(
            self.private_key_path,
            "wb"
        ) as file:

            file.write(private_bytes)



        # Guardar pública

        public_bytes = public_key.public_bytes(

            encoding=serialization.Encoding.PEM,

            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )


        with open(
            self.public_key_path,
            "wb"
        ) as file:

            file.write(public_bytes)



        return True



    def load_private_key(self):

        with open(
            self.private_key_path,
            "rb"
        ) as file:

            return serialization.load_pem_private_key(
                file.read(),
                password=None
            )



    def load_public_key(self):

        with open(
            self.public_key_path,
            "rb"
        ) as file:

            return serialization.load_pem_public_key(
                file.read()
            )



def generate_aes_key():

    """
    Genera una clave AES-256

    AES-256 = 32 bytes
    """

    return os.urandom(32)