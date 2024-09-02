# CI-0124 TP1 Avance 2


En el avance 2 se desarrolla el analizador léxico (Lexer), se crea una lista de tokens con etiquetas (tags) y atributos (attributes), del archivo XML, además en el archivo se observan algunos tags de HTML por lo cual también se toman en cuenta.


A la lista de tokens se les hace sus correspondientes expresiones regulares y se definen los atributos. También se revisa qué errores genera con la función `def t_error(t)`.


## Build Instructions


Assuming that you use Linux or UNIX-like operating system:

1. Open a terminal on `TP1/Avance2` directory.

1. Create a virtual environment:
	```bash
	$ python3 -m venv venv
	```

1. Activate virtual environment:
	```bash
	$ source venv/bin/activate
	```

1. Install requirements using pip:
	```bash
	$ pip3 install -r requirements.txt
	```

1. Run the program:
	```bash
	$ python3 main.py
	```
