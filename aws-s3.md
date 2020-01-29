
```aws s3 ls```

```aws s3 mb s3://pacc2020```

```aws s3 ls```

```aws s3 cp Generar_Personas.py s3://pacc2020```

```aws s3 ls s3://pacc2020```

```aws s3 cp s3://pacc2020/Generar_Personas.py```

```aws s3 cp s3://pacc2020/Generar_Personas.py . ```

```aws s3 sync salida s3://pacc2020/personas-data```

```python Generar_Personas.py 10000```

```aws s3 sync salida s3://pacc2020/personas-data```

```aws s3 presign s3://pacc2020/personas-data/20200128155352_personas.csv```
