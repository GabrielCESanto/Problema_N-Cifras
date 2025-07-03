import asyncio
import time
import websockets
import json

senha = "928471"
n_digitos = len(senha)
maximo = 10 ** n_digitos
num_workers = 6
faixa = maximo // num_workers

async def enviar_tarefa(worker_url, inicio, fim, senha, ping_interval=60, ping_timeout=1000):
    async with websockets.connect(
        worker_url,
        ping_interval=ping_interval, 
        ping_timeout=ping_timeout    
    ) as ws:
        await ws.send(json.dumps({
            "senha": senha,
            "inicio": inicio,
            "fim": fim
        }))
        resposta = await ws.recv()
        return json.loads(resposta)

async def main():
    workers = [
        "ws://worker1:8765",
        "ws://worker2:8765",
        "ws://worker3:8765",
        "ws://worker4:8765",
        "ws://worker5:8765",
        "ws://worker6:8765",
    ]

    tarefas = []
    tempo_inicio = time.time()

    for i in range(num_workers):
        inicio = i * faixa
        fim = maximo if i == num_workers - 1 else (i + 1) * faixa
        tarefas.append(enviar_tarefa(workers[i], inicio, fim, senha))

    resultados = await asyncio.gather(*tarefas)

    for resultado in resultados:
        if resultado["senha"] is not None:
            tempo_fim = time.time()
            print(f"Senha encontrada: {resultado['senha']}")
            print(f"Tentativa: {resultado['tentativa']}")
            print(f"Tempo de execução distribuída: {tempo_fim - tempo_inicio:.6f} segundos")
            return

    print("Senha não encontrada.")

if __name__ == "__main__":
    asyncio.run(main())
