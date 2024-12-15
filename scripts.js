document.getElementById('chat-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const query = document.getElementById('query').value;
    const chatBox = document.getElementById('chat-box');

    // Add user message to chat box
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user-message';
    userMessageDiv.textContent = query;
    chatBox.appendChild(userMessageDiv);

    // Clear input field
    document.getElementById('query').value = '';

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;

    // Add loading indicator
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message bot-message loading';
    loadingDiv.innerHTML = '<span>Loading...</span>';
    chatBox.appendChild(loadingDiv);

    try {
        const response = await fetch('https://api.cohere.ai/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Your API KEY`
            },
            body: JSON.stringify({ message: query })
        });

        const data = await response.json();
        const botMessage = data.chat_history[data.chat_history.length - 1].message;

        // Remove loading indicator
        chatBox.removeChild(loadingDiv);

        // Add bot message to chat box
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'message bot-message';
        botMessageDiv.innerHTML = formatResponse(botMessage);
        chatBox.appendChild(botMessageDiv);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        // Remove loading indicator
        chatBox.removeChild(loadingDiv);

        const errorMessageDiv = document.createElement('div');
        errorMessageDiv.className = 'message bot-message';
        errorMessageDiv.textContent = 'Error: ' + error.message;
        chatBox.appendChild(errorMessageDiv);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});

function formatResponse(response) {
    // Split the response into separate points
    const points = response.split(/(\d+\.\s)/).filter(Boolean);
    let formattedResponse = '';

    points.forEach((point, index) => {
        if (index % 2 === 0) {
            formattedResponse += `<strong>${point}</strong>`;
        } else {
            formattedResponse += `<p>${point}</p>`;
        }
    });

    return formattedResponse;
}
