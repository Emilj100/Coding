document.addEventListener('DOMContentLoaded', function() {
    let div = document.querySelector('#div-project');
    let less = document.querySelector('#show-less');
    let more = document.querySelector('#show-more');
    document.querySelector('#show-more').addEventListener('click', function() {
        div.style.display = 'block';
        less.style.display = 'inline-block';
        more.style.display = 'none';
    });

    document.querySelector('#show-less').addEventListener('click', function() {
        div.style.display = 'none';
        less.style.displayy = 'none';
        more.style.display = 'inline-block';

    });
});


