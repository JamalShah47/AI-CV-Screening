document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const outputDiv = document.getElementById('output');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const cvFile = formData.get('cv');
        const jobDescriptionFile = formData.get('jobDescription');

        if (!cvFile || !jobDescriptionFile) {
            alert('Please upload both CV and Job Description files.');
            return;
        }

        const response = await processFiles(formData);
        displayOutput(response);
    });

    async function processFiles(formData) {
        try {
            const response = await fetch('/process-files', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error processing files:', error);
            return { error: 'An error occurred while processing files.' };
        }
    }

    function displayOutput(response) {
        if (response.error) {
            outputDiv.innerHTML = `<p>Error: ${response.error}</p>`;
            return;
        }

        const { score, explanation } = response;
        outputDiv.innerHTML = `<p>Score: ${score}</p><p>Explanation: ${explanation}</p>`;
    }
});