#  Encriptador AES en Python

##  Descripción

Este proyecto implementa un programa en Python que permite **cifrar y descifrar archivos de texto plano** utilizando el algoritmo criptográfico AES.
El sistema funciona mediante línea de comandos (CLI), permitiendo generar una llave, cifrar archivos y posteriormente recuperar el contenido original.



##  Objetivo

Aplicar conceptos de criptografía simétrica, incluyendo:

* Generación de llaves seguras
* Cifrado de datos
* Descifrado y recuperación de información


##  Algoritmo utilizado

Se utilizó **AES (Advanced Encryption Standard)** en modo **EAX**.

###  ¿Por qué EAX?

* Permite **cifrado y autenticación al mismo tiempo**
* No requiere padding manual
* Evita errores comunes de seguridad
* Garantiza integridad de los datos (detecta modificaciones)



## Tamaño de la llave

Se utilizó una llave de:

* **256 bits (32 bytes)**

###  Justificación

* Mayor nivel de seguridad disponible en AES
* Recomendado para aplicaciones modernas

---

##  Requisitos

* Python 
* Librería PyCryptodome

Instalación:

```bash
pip install pycryptodome
```

---

##  Estructura del proyecto

```
encriptador-aes/
│
├── crypto_tool.py
├── mensaje_prueba.txt
├── archivo.cifrado
├── archivo_descifrado.txt
├── llave.key
├── requirements.txt
├── README.md
└── capturas/
```

---

##  Uso del programa

###  Generar llave

```bash
python crypto_tool.py generar
```

✔ Genera el archivo `llave.key`


### Cifrar archivo

```bash
python crypto_tool.py cifrar --archivo mensaje_prueba.txt
```

✔ Genera `archivo.cifrado`



###  Descifrar archivo

```bash
python crypto_tool.py descifrar
```

✔ Genera `archivo_descifrado.txt`



##  Verificación

El archivo original (`mensaje_prueba.txt`) y el archivo descifrado (`archivo_descifrado.txt`) deben ser **idénticos**, demostrando que el proceso de cifrado y descifrado es correcto.



##  Evidencia

En la carpeta `capturas/` se incluyen imágenes que muestran:

* Generación de llave
* Cifrado de archivo
* Descifrado exitoso



##  Conclusión

Este proyecto demuestra el uso práctico de criptografía simétrica mediante AES, permitiendo proteger información sensible y garantizar su integridad y confidencialidad.

