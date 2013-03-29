$(document).ready(function(){
    $project_header = $('#project-form .hdr');
    $project_frame = $('.project-iframe-wrapper');
    $project_header.click(function() {
        $project_frame.slideToggle();
    });
    if ($('body').hasClass('index-page')) {
        $project_header.trigger('click');
    }
});
