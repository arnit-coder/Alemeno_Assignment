async function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files.length) {
        alert('Please select an image file');
        return;
    }
    
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://127.0.0.1:8000/api/upload/', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        document.getElementById('results').textContent = JSON.stringify(result, null, 2);
    } catch (error) {
        document.getElementById('results').textContent = 'Error: ' + error.message;
    }
}
