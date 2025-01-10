// Animationer
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".fade-in-immediate");
    elements.forEach(element => {
        element.style.opacity = "1"; // Sikrer, at effekten fungerer selv uden scrolling
    });
});

document.addEventListener("scroll", () => {
    const sections = document.querySelectorAll(".section");
    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top < window.innerHeight - 100) {
            section.classList.add("visible");
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const slideInElements = document.querySelectorAll(".slide-in-left, .slide-in-right");

    const checkVisibility = () => {
        slideInElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            const windowHeight = window.innerHeight || document.documentElement.clientHeight;

            if (rect.top <= windowHeight - 400) {
                el.classList.add("visible");
            }
        });
    };

    // Kald funktionen ved scrolling og initialt
    window.addEventListener("scroll", checkVisibility);
    checkVisibility();
});

  // Pie chart til calorietracker
  document.addEventListener("DOMContentLoaded", () => {
    let nutritionPieChart;

    // Initialiser pie chart, når fanen aktiveres
    document.querySelector('#nutrition-tab').addEventListener('shown.bs.tab', () => {
        const ctx = document.getElementById('nutritionPieChart').getContext('2d');

        if (!nutritionPieChart) { // Initialiser kun chartet én gang
            const data = {
                labels: ['Proteins', 'Carbohydrates', 'Fats'],
                datasets: [{
                    data: [25, 50, 25],
                    backgroundColor: ['#36A2EB', '#FFCE56', '#FF6384'],
                    hoverOffset: 4
                }]
            };

            nutritionPieChart = new Chart(ctx, {
                type: 'pie',
                data: data,
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            callbacks: {
                                label: function(tooltipItem) {
                                    return tooltipItem.label + ': ' + tooltipItem.raw + '%';
                                }
                            }
                        }
                    }
                }
            });
        } else {
            nutritionPieChart.resize(); // Hvis chartet allerede er initialiseret, tilpas størrelsen
        }
    });
});
