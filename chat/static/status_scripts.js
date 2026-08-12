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
        console.log("está offline")
        console.log(data.user_username, "está offline")
        if (window.friendSelected === data.user_username) {
            console.log("funcão sendo chamada")
            item.innerHTML = data.online ? "online" : "offline"
        }
        document.getElementById(`status-${data.user_id}`).textContent = data.online ? "online" : "offline"
    }
}

document.addEventListener("DOMContentLoaded", () => {
    StatusSocket();
});