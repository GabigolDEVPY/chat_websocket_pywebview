import webview
from modules.notification.notification_it import mostrar_notificacao

class API:
    def ShowNotification(self, title ,text):
        mostrar_notificacao(title, text)
        return 
    
api = API()
webview.create_window("NextZap", "http://127.0.0.1:8000/chat/home/", width= 1200, height=800, js_api=api)
webview.start(debug=True)