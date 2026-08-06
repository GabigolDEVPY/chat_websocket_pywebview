import webview

class API:
    def teste():
        return {}
    
api = API()
webview.create_window("NextZap", "http://127.0.0.1:8000/chat/home/", width= 1200, height=800,)
webview.start(debug=True)