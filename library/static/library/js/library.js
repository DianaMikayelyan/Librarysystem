document.addEventListener('DOMContentLoaded', function() {
    // References to elements
    const bookIdInput = document.getElementById('book-id');
    const modal = document.getElementById('borrow-form-model');
    const form = document.getElementById('borrow-form');

    // Functions for borrow form
    window.openBorrowForm = function(bookId) {
        bookIdInput.value = bookId;
        modal.style.display = 'block';
    }

    window.closeBorrowForm = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch(`/borrow/${bookIdInput.value}/`, {  // Ensure this URL matches your actual endpoint
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Book borrowed successfully!');
                closeBorrowForm();
            } else {
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error: Unable to borrow book.');
        });
    });
});