document.addEventListener('DOMContentLoaded', function() {
    const sendButton = document.getElementById('sendButton');
    const messageInput = document.getElementById('messageInput');
    const prefixInput = document.getElementById('prefixInput');
    const delayInput = document.getElementById('delayInput');
    const progressBar = document.getElementById('progressBar');
    const timerLabel = document.getElementById('timerLabel');

    sendButton.addEventListener('click', function() {
        const messages = messageInput.value.split('\n').filter(msg => msg.trim() !== '');
        const prefix = prefixInput.value.trim();
        const delay = parseInt(delayInput.value, 10);

        if (messages.length === 0) {
            alert('Please enter at least one message.');
            return;
        }

        sendMessages(messages, prefix, delay);
    });

    function sendMessages(messages, prefix, delay) {
        let currentIndex = 0;
        progressBar.max = messages.length;
        progressBar.value = 0;
        timerLabel.textContent = 'Tiempo restante: ' + formatTime(delay);

        const interval = setInterval(() => {
            if (currentIndex < messages.length) {
                const message = prefix + messages[currentIndex];
                // Aquí se realizaría la llamada AJAX para enviar el mensaje
                console.log('Enviando mensaje:', message);
                progressBar.value++;
                currentIndex++;
                timerLabel.textContent = 'Tiempo restante: ' + formatTime(delay - (currentIndex * delay));
            } else {
                clearInterval(interval);
                alert('Todos los mensajes han sido enviados.');
            }
        }, delay * 1000);
    }

    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }
});