document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/login/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();  // Ensure the response is parsed as JSON
        })
        .then(data => {
            if (data.success) {
                window.location.href = '/user/';  // Redirect to user profile
            } else {
                alert('Login failed: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error logging in. Please try again.');
        });
    });
});
