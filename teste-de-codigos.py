
# =============================================================================
# ALGORITMOS GENÉTICOS - CODIFICAÇÃO E DECODIFICAÇÃO BINÁRIA
# =============================================================================

def codificar(pop, CromLim, Lbits):
    """
    Converte os valores decimais dos indivíduos para uma string binária.
    """
    Nind = len(pop)          # Tamanho da população
    Ncrom = len(CromLim)     # Número de cromossomos
    code = []                # Lista para armazenar a população codificada

    for i in range(Nind):
        temp = ""
        for j in range(Ncrom):
            inf = CromLim[j][0]
            sup = CromLim[j][1]
            
            # Normaliza o valor decimal e ajusta para a escala de bits
            aux = ((pop[i][j] - inf) / (sup - inf)) * ((2 ** Lbits[j]) - 1)
            
            # Arredonda e converte para inteiro
            aux_int = int(round(aux))
            
            # Converte para string binária preenchendo zeros à esquerda
            bin_str = format(aux_int, f'0{Lbits[j]}b')
            
            # Concatena os cromossomos do indivíduo
            temp += bin_str
            
        code.append(temp)
        
    return code

def decodificar(binpop, CromLim, Lbits):
    """
    Converte a string binária de volta para os valores decimais reais.
    """
    Nind = len(binpop)       # Tamanho da população binária
    Ncrom = len(CromLim)     # Número de cromossomos
    decoded_pop = []         # Lista para a população decodificada

    for i in range(Nind):
        ind_decoded = []
        start_idx = 0
        
        for j in range(Ncrom):
            inf = CromLim[j][0]
            sup = CromLim[j][1]
            
            # Extrai a substring binária correspondente ao cromossomo j
            bits_j = Lbits[j]
            bin_str = binpop[i][start_idx : start_idx + bits_j]
            start_idx += bits_j
            
            # Transforma de binário para decimal inteiro
            aux_dec = int(bin_str, 2)
            
            # Converte de volta para a escala do problema (número real)
            aux = aux_dec * (sup - inf) / ((2 ** bits_j) - 1) + inf
            
            ind_decoded.append(aux)
            
        decoded_pop.append(ind_decoded)
        
    return decoded_pop

# =============================================================================
# EXECUÇÃO E TESTES
# =============================================================================

if __name__ == "__main__":
    # 1. Configuração dos parâmetros
    populacao = [
        [2.5, 7.8], 
        [1.1, 9.5]
    ]

    limites = [
        [0.0, 5.0],  # Limites do 1º cromossomo
        [5.0, 10.0]  # Limites do 2º cromossomo
    ]

    bits_por_cromossomo = [8, 10]

    # 2. Testando a Codificação
    print("--- TESTE DE CODIFICAÇÃO ---")
    populacao_binaria = codificar(populacao, limites, bits_por_cromossomo)
    for i, ind in enumerate(populacao_binaria):
        print(f"Indivíduo {i+1} (Binário): {ind}")

    print("\n--- TESTE DE DECODIFICAÇÃO ---")
    # 3. Testando a Decodificação
    populacao_recuperada = decodificar(populacao_binaria, limites, bits_por_cromossomo)
    for i, ind in enumerate(populacao_recuperada):
        # Formatando a saída para facilitar a leitura dos números reais
        valores_formatados = [f"{valor:.2f}" for valor in ind]
        print(f"Indivíduo {i+1} (Decimal): {valores_formatados}")
