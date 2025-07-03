import asyncio
import websockets
import json

async def handler(websocket):
    async for message in websocket:
        dados = json.loads(message)
        senha = dados["senha"]
        inicio = dados["inicio"]
        fim = dados["fim"]
        n_digitos = len(senha)

        for tentativa in range(inicio, fim):
            tentativa_str = str(tentativa).zfill(n_digitos)
            if tentativa_str == senha:
                await websocket.send(json.dumps({
                    "senha": tentativa_str,
                    "tentativa": tentativa
                }))
                return

        await websocket.send(json.dumps({
            "senha": None,
            "tentativa": fim
        }))

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
