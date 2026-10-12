def obter_unicos(colecao):
    """Retorna os valores distintos de uma coleção ordenados."""
    return sorted(list(set(colecao)))

def diferenca_a_b(a, b):
    """Retorna os elementos presentes em A, mas não em B."""
    return sorted(list(set(a) - set(b)))