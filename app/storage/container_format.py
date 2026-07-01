"""
Tesla Crypt
Container Format Manager

Gestiona archivos .tesla

"""

import json
import struct



class TeslaContainer:


    MAGIC = b"TESLA01"



    def create_container(

            self,

            output_path,

            encrypted_package,

            metadata

    ):


        """
        Construye archivo .tesla

        """



        metadata_bytes = json.dumps(

            metadata

        ).encode()



        with open(
            output_path,
            "wb"
        ) as file:



            # Header

            file.write(
                self.MAGIC
            )



            # Metadata size

            file.write(

                struct.pack(

                    "I",

                    len(metadata_bytes)

                )

            )



            # Metadata

            file.write(

                metadata_bytes

            )



            # AES Key cifrada

            file.write(

                struct.pack(

                    "I",

                    len(
                        encrypted_package["encrypted_key"]

                    )

                )

            )


            file.write(

                encrypted_package["encrypted_key"]

            )



            # Nonce

            file.write(

                encrypted_package["nonce"]

            )



            # Datos cifrados

            file.write(

                encrypted_package["encrypted_data"]

            )




    def read_container(

            self,

            path

    ):


        """
        Lee archivo .tesla

        """



        with open(

            path,

            "rb"

        ) as file:



            header = file.read(7)



            if header != self.MAGIC:

                raise Exception(
                    "Archivo Tesla inválido"
                )



            metadata_size = struct.unpack(

                "I",

                file.read(4)

            )[0]



            metadata = json.loads(

                file.read(

                    metadata_size

                )

            )



            key_size = struct.unpack(

                "I",

                file.read(4)

            )[0]



            encrypted_key = file.read(

                key_size

            )



            nonce = file.read(12)



            encrypted_data = file.read()



        return {


            "metadata":
                metadata,


            "encrypted_key":
                encrypted_key,


            "nonce":
                nonce,


            "encrypted_data":
                encrypted_data

        }
