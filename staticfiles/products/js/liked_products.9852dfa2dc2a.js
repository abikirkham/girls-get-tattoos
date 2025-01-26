$(document).on('click', '.likeButton', function() {
        const button = $(this);
        const productId = button.data('post-id');

        $.ajax({
            url: "{% url 'like_view' %}",
            type: 'POST',
            data: {
                'product_id': productId,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(response) {
                alert(response.message);
                button.toggleClass('liked');
            },
            error: function(response) {
                alert(response.responseJSON.error || 'Something went wrong!');
            }
        });
    });
