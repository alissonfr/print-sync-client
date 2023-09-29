import socketio
import json
from datetime import datetime

class SocketClient:
    def __init__(self, server_url, user):
        self.sio = socketio.Client()
        self.username = user
        self.sio.connect(server_url)

        self.sio.on('connect', self.connect)
        self.sio.on('response', self.response)
        self.sio.on('capture', self.capture)
        self.sio.on('connect_error', self.connect_error)
        self.sio.on('disconnect', self.disconnect)

    def connect(self):
        print('Conectado ao servidor')

    def connect_error(self, data):
        print("Falha na comunicação com o servidor! ", data)

    def capture(self, data):
        print('Mensagem do servidor no tópico "capture":', data)

    def response(self, data):
        print('Mensagem do tópico "response":', data)

    def disconnect(self):
        print('Desconectado do servidor')

    def capture_message(self, string_image):
        dt_now = datetime.now()
        dt_formatted = dt_now.strftime("%Y-%m-%d %H-%M-%S-%f")
        data = {
            "username": self.username,
            "send_at": dt_formatted,
            "blb_image": string_image
        }
        print("Enviando...", self.username)
        self.sio.emit('capture', json.dumps(data))

