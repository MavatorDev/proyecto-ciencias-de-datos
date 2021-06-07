# Pasos para ejecutar el proyecto.

- Para poder ejecutar el código de manera correcta, se necesita inicialmente descargar los datos que están en el repositorio.

- Luego de tener los datos, hay dos posibles caminos:

1) El primero, es el mas completo, que es el que realizamos, crear un bucket en S3, formar la estructura de un datalake y como en github ya están los datos limpios, guardarlos en la zona "trusted", una vez con los datos en S3, dentro del código cambiar las credenciales por las de la cuenta en la cual se creó el aws, el nombre del bucket y de la carpeta en caso de haberla llamado diferente.

2) El segundo paso, es simplemente subir los archivos al drive y conectarse a este.


- Por último, las variables training_path y testeo_path, por las rutas en donde están almacenados nuestros archivos. 

- Ya en el proceso de verificación, de igual manera se deben cambiar las rutas por donde están las imágenes propias.

