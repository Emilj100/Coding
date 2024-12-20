document.addEventListener('DOMContentLoaded', function() {
    let div = document.querySelector('#div-project');
    let less = document.querySelector('#show-less');
    let more = document.querySelector('#show-more');

    more.addEventListener('click', function() {
        div.style.display = 'block';
        less.style.display = 'inline-block';
        more.style.display = 'none';
    });

    // Når man klikker på "Show Less"
    less.addEventListener('click', function() {
        div.style.display = 'none';
        less.style.display = 'none';
        more.style.display = 'inline-block'; 
    });
});
