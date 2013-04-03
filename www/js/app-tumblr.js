function trimMessages(){
    $("body.index-page .post .message").each(function(i,v){
        var message = $(v);
        message.text(message.text().substring(0,80) + "...");
    });
}

$(document).ready(function(){
    $b = $('body');
    $form = $('#project-form');
    $modal_bg = $('.modal-bg');
    $modal_btn = $('#modal-btn');
    $project_hdr = $form.find('.hdr');
    $project_wrap = $form.find('.project-iframe-wrapper');
    $project_iframe = $form.find('iframe');
    
    function toggle_header() {
        $b.toggleClass('modal-open');
    }
    
    $modal_btn.click(function() {
        toggle_header();
    });
    $project_hdr.click(function() {
        toggle_header();
    });
    $modal_bg.click(function() {
        toggle_header();
    });
    
    trimMessages();
    
    function resize_window() {
        var new_height = $form.height() - $project_hdr.height();
        $project_wrap.height(new_height);
    }
    $(window).resize(resize_window);
    resize_window();
});