const $btn = $('#post_edit');
const $cardFormEdit = $('#edit-post');

$btn.on('click', (e) => {
    console.log(e.target.id)
    $cardFormEdit.css( { visibility: 'visible' });
    $cardFormEdit.addClass('animate');
});
