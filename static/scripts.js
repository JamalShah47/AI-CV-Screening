document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const outputDiv = document.getElementById('output');
    const submitBtn = document.querySelector('button[type="submit"]');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const cvFile = formData.get('cv');
        const jobDescriptionFile = formData.get('jobDescription');

        if (!cvFile || !jobDescriptionFile) {
            alert('Please upload both CV and Job Description files.');
            return;
        }

        // Disable submit button and show loading spinner
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';

        const response = await processFiles(formData);
        displayOutput(response);

        // Re-enable submit button and reset text
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Submit';
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

        // Set color based on score
        let color = '';
        if (score >= 7) {
            color = 'green'; // Green for scores >= 7
        } else {
            color = 'red'; // Red for scores < 7
        }

        // Update output with colored score
        outputDiv.innerHTML = `<p>Score: <span style="color: ${color};">${score}</span></p><p>Explanation: ${explanation}</p>`;
    }
});
