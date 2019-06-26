(function ($) {
    'use strict';

    $(document).ready(function() {

        var $modal = $('#reviewsModal');
        $modal.find('form').on('submit', function(e) {
            e.preventDefault();
            var $form = $(this);
            $.ajax({
                type: $form.attr('method'),
                url: $form.attr('action'),
                data: $form.serialize()
            }).done(function(response){
                $modal.find('h5').text(response.title);
                $form.replaceWith("<p>" + response.message + "</p>");
            });
        });

    })

}(jQuery));
