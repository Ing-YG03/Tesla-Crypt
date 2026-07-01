"""
Tesla Crypt
File Manager Service

Gestiona lectura y escritura
de archivos físicos
"""


from pathlib import Path



class FileManager:



    def read_file(self, file_path):

        """
        Lee archivo como bytes
        """

        path = Path(file_path)


        if not path.exists():

            raise FileNotFoundError(
                "Archivo no encontrado"
            )


        with open(
            path,
            "rb"
        ) as file:


            return file.read()



    def write_file(

            self,

            file_path,

            data

    ):

        """
        Escribe archivo desde bytes
        """

        path = Path(file_path)



        with open(

            path,

            "wb"

        ) as file:


            file.write(data)




    def get_metadata(

            self,

            file_path

    ):


        """
        Obtiene información
        del archivo original
        """

        path = Path(file_path)


        return {


            "name":
                path.name,


            "extension":
                path.suffix,


            "size":
                path.stat().st_size


        }