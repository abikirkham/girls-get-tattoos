$(document).on('click', '.likeButton', function() {
    const button = $(this);
    const productId = button.data('post-id');
    const url = button.data('url');
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    console.log('Product ID:', productId);
    console.log('URL:', url);

    $.ajax({
        url: url,
        type: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        data: {
            'product_id': productId
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
