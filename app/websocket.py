import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Conectado ao servidor Socket.IO')

@sio.event
def mensagem_do_cliente(data):
    print('Mensagem do servidor no tópico "mensagem_do_cliente":', data)

@sio.on('resposta_do_servidor')
def resposta_do_servidor(data):
    print('Mensagem do tópico "resposta_do_servidor":', data)

@sio.event
def disconnect():
    print('Desconectado do servidor Socket.IO')

sio.connect('ws://25.62.141.82:5000')

message = input('Digite uma mensagem para enviar ao servidor no tópico "mensagem_do_cliente": ')
sio.emit('mensagem_do_cliente', message)

sio.wait()