from setuptools import setup

setup(
    name='Paquete Calculos - Potencia y Porcentaje',
    version='1.0',
    description='Paquete para calcular la potencia y el porcentaje',
    author='Eliab Hernandez',
    author_email='moises_hl_zod@hotmail.com', # Dato no obligatorio
    url='www.eh.com',
    packages=['calculos','calculos.potencia_porcentaje'] # Aqui tenemos que indicar donde se encuentra (ruta) el paquete o subpaquetes que queremos empaquetar. No se necesario especificar la carpeta raiz. Para anotar la ruta es necesario hacerle entre corchetes y primero va la carpeta consecutiva a la raiz y despues el subpaquete con la ruta completa, es decir de nueva cuenta la carpeta anotada al inicio que es la que le sigue de la carpeta raiz
)

# Con esto ya estaria completo el setup