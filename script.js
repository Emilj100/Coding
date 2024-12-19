let input = document.querySelector('input');
document.querySelector('#button5').addEventListener('click', function() {
    if (input.value == 'Denmark')
    {
        text6.style.visibility = 'visible';
        input.style.backgroundColor = 'green';
    }
    else
    {
        text5.style.visibility = 'visible';
        input.style.backgroundColor = 'red';
    }
