import boto3
import json
import decimal


data_entrada = open('/Users/pedrodonte/developer/random-data/salida/20200128155352_personas.csv')

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('persona')


for x in data_entrada:
    reg = str(x).strip().split("|")

    table.put_item(
        Item={
            'pais': reg[8],
            'dni': reg[0]+"-"+reg[1],
            'info': {
                'nombre': reg[2],
                'apellido_1': reg[3],
                'apellido_2': reg[4]
            }
        }
    )
