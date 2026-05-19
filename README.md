'# Filtrar números pares

Proyecto práctico de estructuración en Python + uso de GitHub.

---

## Contenidos

- Inicio rapido
- Resumen
- Estructura del Proyecto
- Ejemplo de uso
- Notas

---

##  Inicio rapido

Clonar el repositorio:
git clone https://github.com/pepese3/Practico-2-prog-anl-II.git
cd Practico-2-prog-anl-II

Ejecutar el programa:
python mi_proyecto/main.py

## Resumen

Este proyecto implementa una función filtrar_pares(lista) que:

Recibe una lista de números
Filtra los números pares
Devuelve una nueva lista

La implementación utiliza estructuras for e if.

## Estructura del Proyecto
```bash
mi_proyecto/
│── main.py
│── src/
│   └── operaciones.py
│── notebooks/
│   └── uso_funciones.ipynb
│── README.md
│── requirements.txt
```

## Ejemplo de uso
from src.operaciones import filtrar_pares

lista = [1, 2, 3, 4, 5, 6]
resultado = filtrar_pares(lista)

print(resultado)  # [2, 4, 6]

## Notas
No requiere dependencias externas

'