$(document).on('click', '.likeButton', function() {
    const button = $(this);
    const productId = button.data('post-id');
    const url = button.data('url');
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    $.ajax({
        url: url,
        type: 'POST',
        data: {
            'product_id': productId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        headers: {
            'X-CSRFToken': csrfToken // Pass CSRF token in the headers
        },
        success: function(response) {
            alert('Product liked successfully!');
            button.find('i').toggleClass('far fas');
        },
        error: function(response) {
            console.log(response.responseText);
            alert('Failed to like the product.');
        }
    });
});
