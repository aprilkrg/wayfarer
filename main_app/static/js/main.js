const $btn = $('#post_edit');
const $cardFormEdit = $('#edit-post');

$btn.on('click', (e) => {
    $cardFormEdit.css( { visibility: 'visible' });
    $cardFormEdit.addClass('animate');
});
