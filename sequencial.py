import time

# Função para a quebra de senha
def quebra_senha(senha_real, n_digitos):
    #Calcula o número de combinações possíveis 
    combinacoes = 10 ** n_digitos

    # Encontra a senha por força bruta
    for tentativa in range(combinacoes):
        tentativa_str = str(tentativa).zfill(n_digitos)
        if tentativa_str == senha_real:
            return tentativa_str, tentativa
    return None, combinacoes

# Função principal
if __name__ == "__main__":
    senha = "8192047356"
    n_digitos = len(senha)

    tempo_inicio = time.time()
    encontrada, tentativas = quebra_senha(senha, n_digitos)
    tempo_fim = time.time()

    print(f"Senha encontrada: {encontrada} após {tentativas} tentativas (sequencial)")
    print(f"Tempo de execução (sequencial): {tempo_fim - tempo_inicio:.6f} segundos")
