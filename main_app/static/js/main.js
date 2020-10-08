let modalId = window.location.pathname;
console.log(window.location)
modalId = modalId.split('/').join('')
console.log(modalId)

const $btn = $('.btn-primary');
const $modal = $('.modal-dialog');
const $modalTitle = $('.modal-title');

$modal.attr("id", `${modalId}`)

console.log($btn);

// $('nav').on('click', (e) => {
//     // window.location.href = window.location.href + e.target.id
//     // $btn.attr("data-target", "#" + modalId );
//     $modalTitle.text(modalId)
//     console.log(e.target);
// })
