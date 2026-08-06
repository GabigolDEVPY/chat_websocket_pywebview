

let ws = null;



function OpenSocket (room) {
    if (ws) {
        ws.close()
    }

    const protocol = window.location.protocol === "https:" ? "wss" : "ws";

    ws = new WebSocket(
        `${protocol}://${window.location.host}/ws/chat/${room}/`
    );

    ws.onopen = async () => {
        console.log("tentando limpar")
        document.getElementById("messages").innerHTML = "";
    }



    ws.onmessage = function(e) {

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
                   <div class="bg-light rounded p-2 mb-1">${message.user}: ${message.text}</div>`
                   document.getElementById("messages").appendChild(messageEL);                
               }
            }
        }
        
        else if (data.type === "message") {
            const messageEL = document.createElement("div");
            messageEL.innerHTML = `
                <div class="bg-light rounded p-2 mb-1">${data.username}: ${data.message}</div>
            `
            document.getElementById("messages").appendChild(messageEL);
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

