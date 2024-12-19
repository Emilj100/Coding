const slider = document.querySelector('.slider');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

let currentIndex = 0;

function updateSliderPosition() {
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : 0;
    updateSliderPosition();
});

nextBtn.addEventListener('click', () => {
    const totalCards = slider.children.length;
    currentIndex = (currentIndex < totalCards - 1) ? currentIndex + 1 : totalCards - 1;
    updateSliderPosition();
});
