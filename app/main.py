from socket_client import SocketClient
import webview
import keyboard
import pyautogui
import base64
from io import BytesIO
from config.env import *
from os import environ

class Api:
    def __init__(self):
        self._window = None
        self.client = None
        self.isListening = False

    def set_window(self, window):
        self._window = window

    def init_connection(self, username):
        print("\nTentando iniciar conexão com o servidor...")
        self.client = SocketClient(environ.get("SERVER_URL"), username)
        print("Conexão com o servidor iniciada.\n")

    def capture_encode(self):
        photo = pyautogui.screenshot()
        output = BytesIO()
        photo.save(output, format='PNG')
        image_data = base64.b64encode(output.getvalue()).decode()
        return image_data

    def handle_capture(self):
        print("\nCaptura de tela registrada. Enviando ao servidor...")
        base64_string = self.capture_encode()
        self.client.capture_message(base64_string)

    def minimize(self):
        self._window.minimize()
        if not self.isListening:
            self.isListening = True
            while True:
                if not keyboard.is_pressed('print screen'):
                    is_pressed = False
                while not is_pressed:
                    if keyboard.is_pressed('print screen'):
                        keyboard.block_key('print screen')
                        api.handle_capture()
                        is_pressed = True


if __name__ == '__main__':
    api = Api()
    window = webview.create_window(title="Print-sync", url="web/index.html", width=600, height=800, resizable=False, js_api=api)
    api.set_window(window)
    webview.start()