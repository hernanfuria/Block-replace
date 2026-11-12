# NAP Replace Script

Script en Python para automatizar el reemplazo o inserción de bloques DXF utilizando la librería `ezdxf`.

## ¿Qué hace?
El script lee un archivo DXF de entrada (`to_replace.dxf`), recorre todas las entidades de inserción de bloques (`INSERT`) presentes en el espacio modelo (`modelspace`), y añade un nuevo bloque especificado (`new_block_name`) en las mismas coordenadas `(x, y, z)` de cada bloque existente. 

Opcionalmente, permite eliminar los bloques originales (`delete_old_blocks = True`) y guarda el resultado en un nuevo archivo DXF (`replaced.dxf`).

## Dependencias
Este script requiere Python y la librería `ezdxf` para manipular archivos DXF.

Puedes instalar la dependencia ejecutando:
```bash
pip install ezdxf
```

## Configuración
Dentro del archivo `nap_replace.py` se pueden modificar los siguientes parámetros en la sección de configuración:

- `input_file`: Ruta del archivo DXF de entrada (por defecto: `"to_replace.dxf"`).
- `output_file`: Ruta del archivo DXF de salida (por defecto: `"replaced.dxf"`).
- `new_block_name`: Nombre del nuevo bloque que se va a insertar (por defecto: `"nap_placeholder"`).
- `new_layer_name`: Capa (layer) donde se insertará el nuevo bloque (por defecto: `"0"`).
- `delete_old_blocks`: Booleano (`True` o `False`). Si es `True`, elimina los bloques originales después de insertar los nuevos.

## Cómo ejecutarlo
Asegúrate de tener instalada la dependencia `ezdxf` y ejecuta el script con:

```bash
py nap_replace.py
```
*(O el comando equivalente según tu entorno de Python, como `python nap_replace.py`)*

## Información relevante
- Realiza una validación inicial ("sanity check") para garantizar que el nuevo bloque (`new_block_name`) existe en las definiciones de bloques del dibujo antes de procesar las inserciones.
- Al finalizar, imprime en consola la cantidad total de bloques procesados/reemplazados.
