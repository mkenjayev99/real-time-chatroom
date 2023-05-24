const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/<room_name>/'); // Replace <room_name> with the actual room name

chatSocket.onmessage = function (e) {
    const message = JSON.parse(e.data);
    const messageContainer = document.getElementById('message-container');
    const messageElement = document.createElement('div');
    messageElement.innerText = message.content;
    messageContainer.appendChild(messageElement);
};

document.getElementById('message-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const messageInput = document.getElementById('message-input');
    const messageContent = messageInput.value;
    chatSocket.send(JSON.stringify({
        'content': messageContent
    }));
    messageInput.value = '';
});