document.addEventListener('DOMContentLoaded', function() {
    let div = document.querySelector('#div-project');
    let less = document.querySelector('#show-less');
    let more = document.querySelector('#show-more');
    document.querySelector('#show-more').addEventListener('click', function() {
        div.style.visibility = 'visible';
        less.style.visibility = 'visible';
        more.style.visibilty = 'hidden';
    document.querySelector('#show-less').addEventListener('click', function() {
        div.style.visibility = 'hidden';
        less.style.visibilty = 'hidden';
        more.style.visibility = 'visible';

    });

    });
});


