$(document).ready(function(){
    $form = $('#project-form');
    $modal_btn = $('#modal-btn');
    $project_hdr = $form.find('.hdr');

    $modal_btn.click(function() {
        $form.show();
    });

    $project_hdr.click(function() {
        $form.hide();
    });

});