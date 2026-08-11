let ws_status = null;

function StatusSocket () {
    if (ws_status) {
        ws_status.close()
    }

    const protocol = window.location.protocol === "https:" ? "wss" : "ws";

    ws_status = new WebSocket(`${protocol}://${window.location.host}/ws/status/`)

    ws_status.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const item = document.querySelector(
            "#status-friend"
        );
        if (window.friendSelected === data.user_username) {
            item.innerHTML = data.online ? "Online" : "Offline"
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    StatusSocket();
});