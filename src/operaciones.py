def filtrar_pares(lista: list) -> list:
    'Recibe una lista de numeros y devuelve solo los numeros pares'
    lista_resultado = []
    for numero in lista:
        if numero % 2 == 0:
            lista_resultado.append(numero)
    return lista_resultado
