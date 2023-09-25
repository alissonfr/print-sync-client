import base64
import threading
import pyautogui
import keyboard

def capture_and_print():
    while True:
        try:
            # Aguarda até que a tecla PrintScreen seja pressionada
            keyboard.wait("print_screen")

            # Captura a tela
            screenshot = pyautogui.screenshot()

            # Converte a imagem para Base64
            screenshot_base64 = base64.b64encode(screenshot.tobytes()).decode('utf-8')

            # Imprime a representação Base64 da imagem
            print(screenshot_base64)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    # Inicia a thread que captura a tela
    capture_thread = threading.Thread(target=capture_and_print)
    capture_thread.daemon = True
    capture_thread.start()

    print("Pressione PrintScreen para capturar e exibir a imagem (Ctrl+C para sair)...")

    # Mantém o programa em execução
    while True:
        try:
            pass
        except KeyboardInterrupt:
            break