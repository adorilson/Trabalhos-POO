import opera

def main():
    entrada_a = input("Digite os valores da primeira coleção: ")
    entrada_b = input("Digite os valores da segunda coleção: ")
    
    colecao_a = list(map(int, entrada_a.split()))
    colecao_b = list(map(int, entrada_b.split()))
    
    print("\nResultados:\n")
    
    a_unicos = opera.obter_unicos(colecao_a)
    b_unicos = opera.obter_unicos(colecao_b)
    print(f"1. Valores únicos da primeira coleção: {' '.join(map(str, a_unicos))}")
    print(f"2. Valores únicos da segunda coleção: {' '.join(map(str, b_unicos))}")

if __name__ == "__main__":
    main()