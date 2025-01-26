$(document).ready(function() {
    $('.likeButton').click(function() {
        var product_id = $(this).data('product-id');
        var button = $(this);
        $.ajax({
            type: 'POST',
            url: '/like/',
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            dataType: 'json',
            success: function(response) {
                if (response.liked) {
                    button.text('Liked');
                }
            },
            error: function(response) {
                console.log('Error:', response);
            }
        });
    });
});
