from flask import Flask, render_template
import requests

app = Flask(__name__)

# Definir o servidor ThingsBoard e o token de acesso
THINGSBOARD_SERVER = 'http://your-thingsboard-server-url'
ACCESS_TOKEN = 'your-access-token'

@app.route('/')
def index():
    # Fazer uma solicitação GET para a API ThingsBoard
    response = requests.get(f"{THINGSBOARD_SERVER}/api/v1/{ACCESS_TOKEN}/telemetry")

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
    else:
        data = {'error': 'Failed to retrieve data'}

    # Renderizar o modelo HTML com os dados
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

