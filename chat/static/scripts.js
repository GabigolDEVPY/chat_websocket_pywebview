

let ws = null;
const user = JSON.parse(document.getElementById("current-user").textContent);


function OpenSocket (room) {
    if (ws) {
        ws.close()
    }

    const protocol = window.location.protocol === "https:" ? "wss" : "ws";

    ws = new WebSocket(
        `${protocol}://${window.location.host}/ws/chat/${room}/`
    );

    ws.onopen = async () => {
        document.getElementById("messages").innerHTML = "";
        const footerEl = `
            <div class="input-group">
                <input id="messageInput" type="text" class="form-control rounded-pill border-secondary-subtle" placeholder="Digite uma mensagem..." aria-label="Mensagem">
                <button class="btn btn-primary rounded-circle ms-2 d-flex align-items-center justify-content-center" onclick="SendMessage()" id="sendButton" style="width:45px;height:45px;" title="Enviar mensagem">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16"><path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576 6.636 10.07Zm6.787-8.201L1.591 6.602l4.339 2.76 7.494-7.493Z"/></svg>
                </button>
            </div>
        `
        document.getElementById("footer-message").innerHTML = footerEl;
    }


    
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

