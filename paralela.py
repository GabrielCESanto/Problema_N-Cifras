import threading
import time

#Parâmetros da Senha
senha = "8192047356"
n_digitos = len(senha)
total = 10 ** n_digitos
encontrada = None

#Parâmetros para os threads
lock = threading.Lock()
n_threads = 4

# Função para a quebra de senha por faixa
def quebra_senha_faixa(inicio, fim):
    global encontrada
    
    # Encontra a senha por força bruta
    for tentativa in range(inicio, fim):
        if encontrada:
            return
        tentativa_str = str(tentativa).zfill(n_digitos)
        if tentativa_str == senha:
            with lock:
                encontrada = tentativa_str
            return

# Função para a quebra de senha de forma paralela
def quebra_senha_paralela(n_threads):
    global encontrada
    threads = []

    # Divisão para cada Thread
    tamanho_faixa = total // n_threads

    tempo_inicio = time.time()

    for i in range(n_threads):
        inicio = i * tamanho_faixa
        fim = total if i == n_threads - 1 else (i + 1) * tamanho_faixa
        t = threading.Thread(target=quebra_senha_faixa, args=(inicio, fim))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    tempo_fim = time.time()

    print(f"Senha encontrada (paralela): {encontrada}")
    print(f" Tempo de execução (paralela): {tempo_fim - tempo_inicio:.6f} segundos")

if __name__ == "__main__":
    quebra_senha_paralela(n_threads)
