def obter_unicos(colecao):
    """Retorna os valores distintos de uma coleção ordenados."""
    return sorted(list(set(colecao)))

def diferenca_a_b(a, b):
    """Retorna os elementos presentes em A, mas não em B."""
    return sorted(list(set(a) - set(b)))

def diferenca_b_a(a, b):
    """Retorna os elementos presentes em B, mas não em A."""
    return sorted(list(set(b) - set(a)))