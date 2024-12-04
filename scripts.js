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
