### Setear las credenciasles
```
aws configure
AWS Access Key ID [****************PG7V]: keyleykeykey
AWS Secret Access Key [****************s73Q]: accesjjsjsjs
Default region name [us-east-1]: 
Default output format [None]:
```

### listar buckets existentes
```aws s3 ls```

### crear un nuevo bucket
```aws s3 mb s3://pacc2020```

### listar buckets existentes, ahora debe aparecer el nuevo bucket
```aws s3 ls```

### subir 1 archivo
```aws s3 cp Generar_Personas.py s3://pacc2020```

### listar contenido del bucket
```aws s3 ls s3://pacc2020```

### listar bajar un archivo hacia el cliente
```aws s3 cp s3://pacc2020/Generar_Personas.py . ```

### sicronizar el contenido de un directorio dentro de un bucket
```aws s3 sync salida s3://pacc2020/personas-data```

### generar data de prueba
```python Generar_Personas.py 10000```

### sicronizar el contenido de un directorio dentro de un bucket
```aws s3 sync salida s3://pacc2020/personas-data```

### generar un link prefirmado de descarga para compartir, con expiración
```aws s3 presign s3://pacc2020/personas-data/20200128155352_personas.csv```
