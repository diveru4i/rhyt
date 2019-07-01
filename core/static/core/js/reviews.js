(function ($) {
    'use strict';

    $(document).ready(function() {

        var $modal = $('#reviewsModal');
        var $response = $modal.find('.response');
        var $form = $modal.find('form');
        $form.on('submit', function(e) {
            e.preventDefault();
            var $form = $(this);
            $.ajax({
                type: $form.attr('method'),
                url: $form.attr('action'),
                data: $form.serialize()
            }).done(function(response){
                $response.find('h5').text(response.title);
                $response.find('p').text(response.message);
                $response.show();
                $form.hide();
            });
        });
        $modal.on('hide.bs.modal', function(){
            $response.hide();
            $form.show();
        });

    })

}(jQuery));
