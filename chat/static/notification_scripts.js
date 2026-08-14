let ws_notification = null;

function NotificationSocket () {
    if (ws_notification) {
        ws_notification.close()
    }

    const protocol = window.location.protocol === "https:" ? "wss" : "ws";

    ws_notification = new WebSocket(`${protocol}://${window.location.host}/ws/notification/`)
    console.log("criando a conexão com notification")
    ws_notification.onmessage = function(e) {
        print("notificação chegou")
        const data = JSON.parse(e.data);
        if (data.type === "friend_request.notification") {
            console.log("solicitação de amizade recebida")
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    NotificationSocket();
})