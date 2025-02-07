async function sendMessage() {
    const userInput = document.getElementById('user_input').value;
    const fileInput = document.getElementById('file_input').files[0];

    let fileData = null;
    let fileName = null;

    if (fileInput) {
        fileName = fileInput.name;
        fileData = await fileInput.text();
    }

    const response = await fetch('https://YOUR_API_GATEWAY_URL', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_input: userInput,
            file_data: fileData,
            file_name: fileName
        })
    });

    const data = await response.json();
    document.getElementById('response_text').innerText = data.assistant_response;

    if (data.file_url) {
        document.getElementById('response_text').innerText += `\nFile uploaded: ${data.file_url}`;
    }
}
