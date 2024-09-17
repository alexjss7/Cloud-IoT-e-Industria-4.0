import time
import Adafruit_DHT
import requests

# Configuração do sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# URL da API do ThingsBoard
THINGSBOARD_SERVER = 'http://localhost:8080'
ACCESS_TOKEN = 'SEU_TOKEN_DE_ACESSO'
def enviar_dados(temp, umidade):
    url = f"{THINGSBOARD_SERVER}/api/v1/{ACCESS_TOKEN}/telemetry"
dados = {
    "temperature": temp,
    "humidity": umidade
}
requests.post(url, json=dados)

while True:
    umidade, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR,
                                                   DHT_PIN)
if umidade is not None and temperatura is not None:
    print(f"Temperatura: {temperatura:.1f}C Umidade:
{umidade:.1f}%")
enviar_dados(temperatura, umidade)
else:
print("Falha na leitura dos sensores.")
time.sleep(60)  # Coleta de dados a cada 60 segundos