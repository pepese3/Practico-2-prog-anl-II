# Importar módulo personalizado
import sys
sys.path.append('/content/mi_proyecto/src')

from src.operaciones import filtrar_pares
lista = [1,2,3,4,5,6]
print('Resultado filtrar_pares:', filtrar_pares(lista))