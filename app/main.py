from socket_client import SocketClient
import webview
import keyboard
import pyautogui
import base64
import tempfile
from io import BytesIO

class Api:
    def __init__(self):
        self._window = None
        self.client = None

    def set_window(self, window):
        self._window = window

    def init_connection(self, username):
        self.client = SocketClient('ws://25.62.141.82:5000', username)

    def capture_encode(self):
        photo = pyautogui.screenshot()
        output = BytesIO()
        photo.save(output, format='PNG')
        image_data = base64.b64encode(output.getvalue()).decode()
        return image_data

    def handle_capture(self):
        base64_string = self.capture_encode()
        self.client.capture_message(base64_string)

if __name__ == '__main__':
    api = Api()
    window = webview.create_window(title="Print-sync", url="template/index.html", width=600, height=800, resizable=False, js_api=api)
    api.set_window(window)
    webview.start()
    while True:
        if not keyboard.is_pressed('f'):
            is_pressed = False
        while not is_pressed:
            if keyboard.is_pressed('f'):
                api.handle_capture()
                is_pressed = True