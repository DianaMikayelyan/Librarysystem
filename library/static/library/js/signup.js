document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('signup-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('http://127.0.0.1:8000/library/signup/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (response.headers.get('content-type').includes('application/json')) {
                return response.json();  // Parse response as JSON
            } else {
                throw new Error('Response is not JSON');
            }
        })
        .then(data => {
            if (data.success) {
                window.location.href = '/library/login/';  // Redirect to login
            } else {
                alert('Sign up failed: ' + JSON.stringify(data.errors));
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error signing up. Please try again.');
        });
    });
});
