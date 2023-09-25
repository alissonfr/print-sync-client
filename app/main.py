import webview

webview.create_window(title="Print-sync", url="template/index.html", width = 600, height = 800, resizable=False)
webview.start()

class InputValueReceiver:
    def send_value(self, value): 
        webview.handle_input_value(value)