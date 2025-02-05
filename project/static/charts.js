// static/charts.js

document.addEventListener("DOMContentLoaded", () => {
    // ========== CALORIES PAGE ==========
    const calData = window.calorieData;
    if (calData) {
      // Tjek om "calorieChart" findes:
      const calChartEl = document.getElementById('calorieChart');
      const goalChartEl = document.getElementById('goalChart');
      if (calChartEl && goalChartEl) {
        // Opret to charts
        const calorieCtx = calChartEl.getContext('2d');
        new Chart(calorieCtx, {
          type: 'bar',
          data: {
            labels: calData.days,
            datasets: [{
              label: 'Calories (kcal)',
              data: calData.calories,
              backgroundColor: '#007bff'
            }]
          }
        });

        const goalCtx = goalChartEl.getContext('2d');
        new Chart(goalCtx, {
          type: 'line',
          data: {
            labels: calData.days,
            datasets: [
              {
                label: 'Actual Intake',
                data: calData.calories,
                borderColor: '#007bff',
                backgroundColor: 'rgba(0, 123, 255, 0.2)',
                fill: true,
                tension: 0.3
              },
              {
                label: 'Calorie Goal',
                data: calData.days.map(() => calData.calorieGoal),
                borderColor: '#ff6384',
                borderDash: [5, 5],
                tension: 0.3
              }
            ]
          }
        });
      }
    }

    // ========== CHECKIN PAGE ==========
    const chData = window.checkinData;
    if (chData) {
      // Tjek om "energySleepChart" og "checkin-cards" findes
      const chartEl = document.getElementById('energySleepChart');
      const cardsEl = document.getElementById('checkin-cards');
      if (chartEl && cardsEl) {
        // Tag de seneste 6 data
        let recentData = chData.slice(-6).reverse();

        // Rendre checkin-kort
        cardsEl.innerHTML = "";
        recentData.forEach(entry => {
          const cardHTML = `
            <div class="col-md-4">
              <div class="card p-3 mb-3 shadow-sm">
                <h5>${entry.created_at}</h5>
                <p><strong>Weight:</strong> ${entry.weight} kg</p>
                <p><strong>Energy:</strong> ${entry.energy}/10</p>
                <p><strong>Sleep:</strong> ${entry.sleep} hours</p>
              </div>
            </div>`;
          cardsEl.innerHTML += cardHTML;
        });

        // Opret chart
        const dates = recentData.map(d => d.created_at);
        const energyLevels = recentData.map(d => d.energy);
        const sleepHours = recentData.map(d => d.sleep);

        new Chart(chartEl.getContext('2d'), {
          type: 'bar',
          data: {
            labels: dates,
            datasets: [
              {
                label: 'Energy Level',
                data: energyLevels,
                backgroundColor: '#ffca28'
              },
              {
                label: 'Sleep (hrs)',
                data: sleepHours,
                backgroundColor: '#007bff'
              }
            ]
          }
        });
      }
    }
  });



    // ========== DASHBOARD PAGE ==========
  document.addEventListener("DOMContentLoaded", () => {
    const dbData = window.dashboardData;
    if (dbData) {
      // Tjek om elementer findes
      const weightChartEl = document.getElementById('weightChart');
      const calorieChartEl = document.getElementById('calorieChart');

      if (weightChartEl) {
        new Chart(weightChartEl.getContext('2d'), {
          type: 'line',
          data: {
            labels: dbData.weightLabels,
            datasets: [
              {
                label: 'Weight (kg)',
                data: dbData.weightValues,
                borderColor: '#007bff',
                backgroundColor: 'rgba(0, 123, 255, 0.2)',
                fill: true,
                tension: 0.3
              }
            ]
          },
          options: {
            scales: {
              y: { beginAtZero: false }
            }
          }
        });
      }

      if (calorieChartEl) {
        new Chart(calorieChartEl.getContext('2d'), {
          type: 'bar',
          data: {
            labels: dbData.calorieDays,
            datasets: [
              {
                label: 'Calories (kcal)',
                data: dbData.calorieValues,
                backgroundColor: '#007bff'
              },
              {
                label: 'Calorie Goal',
                data: dbData.calorieDays.map(() => dbData.calorieGoal),
                borderColor: '#ff6384',
                borderDash: [5, 5],
                type: 'line',
                fill: false,
                tension: 0.3
              }
            ]
          },
          options: {
            scales: {
              y: { beginAtZero: true }
            }
          }
        });
      }
    }
  });

    // ========== TRAINING PAGE ==========
  document.addEventListener("DOMContentLoaded", () => {
    // Tjek om der er trainingData
    const trainData = window.trainingData;
    if (trainData) {
      // Tjek om disse elementer findes
      const freqChartEl = document.getElementById('trainingFrequencyChart');
      const progChartEl = document.getElementById('progressionChart');

      if (freqChartEl && progChartEl) {
        // Extract data for frequency
        const freqData = trainData.freqData;
        const freqLabels = freqData.map(d => d.week_range);
        const freqSessions = freqData.map(d => d.sessions);

        // Opret bar chart
        new Chart(freqChartEl.getContext('2d'), {
          type: 'bar',
          data: {
            labels: freqLabels,
            datasets: [{
              label: 'Training Sessions',
              data: freqSessions,
              backgroundColor: '#007bff'
            }]
          }
        });

        // Extract data for progression
        const progData = trainData.progressionData;
        const progLabels = progData.map(d => d.week_range);
        const progWeights = progData.map(d => d.avg_weight);

        // Opret line chart
        new Chart(progChartEl.getContext('2d'), {
          type: 'line',
          data: {
            labels: progLabels,
            datasets: [{
              label: 'Avg Weight (kg)',
              data: progWeights,
              borderColor: '#007bff',
              backgroundColor: 'rgba(0, 123, 255, 0.2)',
              fill: true,
              tension: 0.3
            }]
          }
        });
      }
    }
  });


    // ========== WEIGHT PAGE ==========
  document.addEventListener("DOMContentLoaded", () => {
    // Tjek weightData
    const wData = window.weightData;
    if (wData) {
      const weightChartEl = document.getElementById('weightChart');
      if (weightChartEl) {
        const graphData = wData.graphData || [];
        const dates = graphData.map(d => d.created_at);
        const weights = graphData.map(d => d.weight);

        new Chart(weightChartEl.getContext('2d'), {
          type: 'line',
          data: {
            labels: dates,
            datasets: [{
              label: 'Weight (kg)',
              data: weights,
              borderColor: '#007bff',
              backgroundColor: 'rgba(0, 123, 255, 0.2)',
              fill: true,
              tension: 0.3
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: { beginAtZero: false }
            }
          }
        });
      }
    }
  });

    // ========== CALORIETRACKER PAGE ==========
 // Pie chart til calorietracker
 document.addEventListener("DOMContentLoaded", () => {
    let nutritionPieChart;

    // Initialiser pie chart, når fanen aktiveres
    document.querySelector('#nutrition-tab').addEventListener('shown.bs.tab', () => {
        const ctx = document.getElementById('nutritionPieChart').getContext('2d');

        // Hent makronæringsstoffer fra data, der sendes via Jinja
        const macroData = {
            proteins: parseFloat(document.getElementById('macro-proteins').textContent) || 0,
            carbohydrates: parseFloat(document.getElementById('macro-carbohydrates').textContent) || 0,
            fats: parseFloat(document.getElementById('macro-fats').textContent) || 0
        };

        if (!nutritionPieChart) { // Initialiser kun chartet én gang
            const data = {
                labels: ['Proteins', 'Carbohydrates', 'Fats'],
                datasets: [{
                    data: [macroData.proteins, macroData.carbohydrates, macroData.fats],
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
                                    return tooltipItem.label + ': ' + tooltipItem.raw.toFixed(1) + ' g';
                                }
                            }
                        }
                    }
                }
            });
        } else {
            // Opdater data, hvis chartet allerede er initialiseret
            nutritionPieChart.data.datasets[0].data = [
                macroData.proteins,
                macroData.carbohydrates,
                macroData.fats
            ];
            nutritionPieChart.update();
        }
    });
});
