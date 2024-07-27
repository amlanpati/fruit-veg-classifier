const form = document.getElementById('upload-form');
const imageInput = document.getElementById('image-input');
const uploadButton = document.getElementById('upload-button');
const resultDiv = document.getElementById('result');

uploadButton.addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', imageInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerText = `Result: ${data.result}`;
    })
    .catch(error => {
        console.error(error);
    });
});