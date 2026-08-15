let ws_notification = null;

function NotificationSocket () {
    if (ws_notification) {
        ws_notification.close()
    }

    const protocol = window.location.protocol === "https:" ? "wss" : "ws";

    ws_notification = new WebSocket(`${protocol}://${window.location.host}/ws/notification/`)
    ws_notification.onmessage = function(e) {
        const data = JSON.parse(e.data);
        if (data.type === "friend_request_notification") {
            console.log("solicitação recebida")
            window.pywebview.api.ShowNotification("Solicitação de Amizade", `O usuário ${data.username} lhe enviou solicitação de amizade`);
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    NotificationSocket();
})