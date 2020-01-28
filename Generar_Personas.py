#!/usr/bin/python
import os
import sys
import random
import datetime
from random import randint
from itertools import cycle

paises_file = open("data/country.txt", "r", )
companies_file = open("data/companies.txt", "r")
languages_file = open("data/languages.txt", "r")
last_names_file = open("data/last_names.txt", "r")
men_names_file = open("data/men_names.txt", "r")
women_names_file = open("data/women_names.txt", "r")

genero = ['Femenino', 'Masculino','Femenino', 'Masculino', 'Idenfinido']

paises_array = []
companies_array = []
languages_array = []
last_names_array = []
men_names_array = []
women_names_array = []

def generar_fecha_random(desde, hasta):
    return datetime.date(randint(desde,hasta), randint(1,12),randint(1,28))

def buscar_listado_random(lista):
    return lista[random.randint(0, len(lista) - 1)]

def cargar_data_files(data_file, data_array):
    for x in data_file: data_array.append( str(x).strip() )

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def preparar_data_en_memoria():
    cargar_data_files(paises_file, paises_array)
    cargar_data_files(companies_file, companies_array)
    cargar_data_files(languages_file, languages_array)
    cargar_data_files(last_names_file, last_names_array)
    cargar_data_files(men_names_file, men_names_array)
    cargar_data_files(women_names_file, women_names_array)

def generar_registro_persona(genero):
    empleador = buscar_listado_random(companies_array)
    pais = buscar_listado_random(paises_array)
    apellido_1 = buscar_listado_random(last_names_array)
    apellido_2 = buscar_listado_random(last_names_array)
    idioma = buscar_listado_random(languages_array)
    fecha_nacimiento = str(generar_fecha_random(1950, 2019))
    genero_persona = genero
    run_num = str(randint(10000000, 30000000))
    run_dv = str(digito_verificador(run_num))
    nombre_persona = ''
    if (genero == 'Femenino'):
        nombre_persona = buscar_listado_random(women_names_array)
    elif (genero == 'Masculino'):
        nombre_persona = buscar_listado_random(men_names_array)
    else:
        moneda = random.randint(0, 1)
        if(moneda==1):
            nombre_persona = buscar_listado_random(men_names_array)
        else:
            nombre_persona = buscar_listado_random(women_names_array)

    return run_num+"|"+run_dv+"|"+nombre_persona+"|"+apellido_1+"|"+apellido_2+"|"+fecha_nacimiento+"|"+genero_persona+"|"+idioma+"|"+pais+"|"+empleador

if __name__ == "__main__":
    try:
        cantidad_registros_soliticados = int(sys.argv[1])
        fecha_proceso = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        preparar_data_en_memoria()

        nombre_archivo_salida = "salida/" +fecha_proceso + "_personas.csv"

        data_out_registros = open( nombre_archivo_salida, "w")

        print("generando archivo... : \n"+nombre_archivo_salida)

        print("formato de salida:")
        print("run_num|run_dv|nombre_persona|apellido_1|apellido_2|fecha_nacimiento|genero_persona|idioma|pais|empleador|fecha_proceso")
        for x in range(cantidad_registros_soliticados):
            data_out_registros.write(
                generar_registro_persona(buscar_listado_random(genero)) +"|"+ fecha_proceso + "\n")

        #####
        paises_file.close()
        companies_file.close()
        languages_file.close()
        last_names_file.close()
        men_names_file.close()
        women_names_file.close()
        data_out_registros.close()
        print( str(cantidad_registros_soliticados)+ " registros genarados!")

    except IndexError as e:
        print("Programa recibe un parametro numerico, cantidad de registros solicitados")
        print("ejemplo:")
        print("   python Generar_Personas.py 100")
    except IOError as e:
        print("directorio de salida no existe, entonces se crea, debes volver a ejecutar la instruccion!!!")
	os.mkdir("salida")


