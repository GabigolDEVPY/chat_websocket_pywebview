

let ws = null;
const user = JSON.parse(document.getElementById("current-user").textContent);
window.friendSelected = null;


function ChangeStatusBar (friend_username, friend_id) {
    window.friendSelected = friend_username;
    document.getElementById("friend-name-id").classList.remove("d-none");
    document.getElementById("friend-name-id").classList.add("d-flex");

    document.querySelector("#friend-name-id strong").textContent = friend_username; 

    document.getElementById("messages").innerHTML = "";
    document.getElementById("footer-message").style.display = "block";

    const status_friend = document.getElementById(`status-${friend_id}`);
    console.log("restando user", friend_username)
    document.getElementById("status-friend").textContent = status_friend.innerText;
}

function OpenSocket (room) {
    if (ws) {
        ws.close()
    }


    const protocol = window.location.protocol === "https:" ? "wss" : "ws";

    ws = new WebSocket(
        `${protocol}://${window.location.host}/ws/chat/${room}/`
    );

    
    ws.onmessage = function(e) {
        const messages = document.getElementById("messages");
        
        const data = JSON.parse(e.data);
        if (data.type === "history") {
                document.getElementById("messages").innerHTML = "";
                if (data.messages === null) {

                const messageEL = document.createElement("div");
                messageEL.innerHTML = `
                <div class="text-danger rounded p-2">Erro ao carregar mensagens</div>
                `

                document.getElementById("messages").appendChild(messageEL);
            } else {
                 for ( const message of data.messages ) {
                   const messageEL = document.createElement("div");
                   messageEL.innerHTML = `
                        <div class="d-flex mb-3 ${message.user === user ? 'justify-content-end' : ''}">
                            <div class="${message.user === user ? 'bg-primary text-white' : 'bg-white'} rounded-3 px-3 py-2 shadow-sm" style="max-width: 70%;">
                                ${message.text}
                            </div>
                        </div>
                   `
                   document.getElementById("messages").appendChild(messageEL);       
                }
                messages.scrollTop = messages.scrollHeight;
            }
        }
        
        else if (data.type === "message") {
            const messageEL = document.createElement("div");
            messageEL.innerHTML = `
                <div class="d-flex mb-3 ${data.username === user ? 'justify-content-end' : ''}">
                     <div class="${data.username === user ? 'bg-primary text-white' : 'bg-white'} rounded-3 px-3 py-2 shadow-sm" style="max-width: 70%;">
                        ${data.message}
                    </div>
                </div>
            `
            messages.appendChild(messageEL);

            messages.scrollTop = messages.scrollHeight;
        }

    }
}


function SendMessage () {
    const message = document.getElementById("messageInput").value.trim()
    ws.send(JSON.stringify({
        "message": message,
        "type": "receive"
    }))
}



function CloseChatMobile() {
    document.body.classList.remove('chat-active');
}
