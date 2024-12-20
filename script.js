document.addEventListener('DOMContentLoaded', function() {
    let div = document.querySelector('#div-project');
    let less = document.querySelector('#show-less');
    let more = document.querySelector('#show-more');
    document.querySelector('#show-more').addEventListener('click', function() {
        div.style.visibility = 'visible';
        less.style.visibility = 'visible';
        more.style.visibility = 'hidden';
    });

    document.querySelector('#show-less').addEventListener('click', function() {
        div.style.visibility = 'hidden';
        less.style.visibility = 'hidden';
        more.style.visibility = 'visible';

    });
});

document.addEventListener('DOMContentLoaded', function() {
    question1 = document.getElementById('question1');
    buttons = question1.querySelectorAll('button');
    buttons.forEach((button) => {
        button.addEventListener('click', function () {
            if (this.dataset.correct === "true") {
                this.style.backgroundColor = 'green';
                buttons.forEach(btn => btn.disabled = true);
            } else {
                this.style.backgroundColor = 'red';
            }
        });
    });
    question2 = document.getElementById('question2');
    buttons = question2.querySelectorAll('button');
    buttons.forEach((button) => {
        button.addEventListener('click', function () {
            if (this.dataset.correct === "true") {
                this.style.backgroundColor = 'green';
                buttons.forEach(btn => btn.disabled = true);
            } else {
                this.style.backgroundColor = 'red';
            }

        });
    });
    question3 = document.getElementById('question3');
    buttons = question3.querySelectorAll('button');
    buttons.forEach((button) => {
        button.addEventListener('click', function () {
            if (this.dataset.correct === "true") {
                this.style.backgroundColor = 'green';
                buttons.forEach(btn => btn.disabled = true);
            } else {
                this.style.backgroundColor = 'red';
            }

        });
    });
    question4 = document.getElementById('question4');
    buttons = question4.querySelectorAll('button');
    buttons.forEach((button) => {
        button.addEventListener('click', function () {
            if (this.dataset.correct === "true") {
                this.style.backgroundColor = 'green';
                buttons.forEach(btn => btn.disabled = true);
            } else {
                this.style.backgroundColor = 'red';
            }

        });
    });
});

