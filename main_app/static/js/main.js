const $btn = $('#post_edit');
const $cardFormEdit = $('#edit-post');
const $sidebar = $('.city-sidebar')

$btn.on('click', (e) => {  
    if ( $cardFormEdit.hasClass('animate') ) {
        $cardFormEdit.css( { visibility: 'hidden' });
        $cardFormEdit.removeClass('animate'); 
    } else {
        $cardFormEdit.css( { visibility: 'visible' });
        $cardFormEdit.addClass('animate');
    }
});
