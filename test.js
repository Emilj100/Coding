document.addEventListener('DOMContentLoaded', function () {
    // Part 1: Multiple Choice
    const buttons = document.querySelectorAll('.options button');
    const result1 = document.getElementById('result1');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            if (this.dataset.correct === "true") {
                this.style.backgroundColor = 'green';
                result1.textContent = "Correct!";
                result1.className = "result correct";
            } else {
                this.style.backgroundColor = 'red';
                result1.textContent = "Incorrect";
                result1.className = "result incorrect";
            }

            // Deaktiver alle knapper efter et valg
            buttons.forEach(btn => btn.disabled = true);
        });
    });

    // Part 2: Free Response
    const input = document.getElementById('answerInput');
    const checkButton = document.getElementById('checkAnswer');
    const result2 = document.getElementById('result2');

    checkButton.addEventListener('click', function () {
        const answer = input.value.trim().toLowerCase();

        if (answer === "denmark") {
            input.style.backgroundColor = 'green';
            result2.textContent = "Correct!";
            result2.className = "result correct";
        } else {
            input.style.backgroundColor = 'red';
            result2.textContent = "Incorrect";
            result2.className = "result incorrect";
        }
    });
});


