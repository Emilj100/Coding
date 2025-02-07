// static/charts.js

// Wait until the DOM is fully loaded before executing the code
document.addEventListener("DOMContentLoaded", () => {
  // ========= CALORIES PAGE =========
  // Retrieve the calorie data from the global window object
  const calData = window.calorieData;

  // Proceed only if calorie data exists
  if (calData) {
    // Check if the elements for the charts exist in the DOM
    const calChartEl = document.getElementById('calorieChart');
    const goalChartEl = document.getElementById('goalChart');

    if (calChartEl && goalChartEl) {
      // Create two charts: one for calorie intake and one for calorie goals

      // --- Bar Chart for Calories ---
      // Get the 2D drawing context from the calorie chart element
      const calorieCtx = calChartEl.getContext('2d');
      // Create a new bar chart using the Chart.js library
      new Chart(calorieCtx, {
        type: 'bar', // Set the chart type to bar
        data: {
          // Use the days from the calorie data as the labels on the x-axis
          labels: calData.days,
          datasets: [{
            label: 'Calories (kcal)', // Label for the dataset
            data: calData.calories,     // Calorie values for each day
            backgroundColor: '#007bff'  // Bar color
          }]
        }
      });

      // --- Line Chart for Calorie Goals ---
      // Get the 2D drawing context from the goal chart element
      const goalCtx = goalChartEl.getContext('2d');
      // Create a new line chart using the Chart.js library
      new Chart(goalCtx, {
        type: 'line', // Set the chart type to line
        data: {
          // Use the same days for the x-axis labels
          labels: calData.days,
          datasets: [
            {
              label: 'Actual Intake',    // Label for the actual calorie intake dataset
              data: calData.calories,      // Calorie intake values
              borderColor: '#007bff',      // Line color for actual intake
              backgroundColor: 'rgba(0, 123, 255, 0.2)', // Fill color under the line
              fill: true,                  // Fill the area under the line
              tension: 0.3                 // Curve tension for smoothness
            },
            {
              label: 'Calorie Goal',       // Label for the calorie goal dataset
              // For each day, map the calorie goal value (same goal for each day)
              data: calData.days.map(() => calData.calorieGoal),
              borderColor: '#ff6384',       // Line color for calorie goal
              borderDash: [5, 5],           // Dashed line style
              tension: 0.3                 // Curve tension for smoothness
            }
          ]
        }
      });
    }
  }
});


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
      // Extract data for frequency (samme som før)
      const freqData = trainData.freqData;
      const freqLabels = freqData.map(d => d.week_range);
      const freqSessions = freqData.map(d => d.sessions);

      // Opret bar chart for training frequency
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

      // Extract data for progression (gennemsnitlig vægt per uge)
      const progData = trainData.progressionData;
      const progLabels = progData.map(d => d.week_range);
      const progAvgWeights = progData.map(d => d.avg_weight);

      // Beregn vægtstigning uge for uge (dvs. forskellen fra forrige uge)
      let weightIncreases = [];
      for (let i = 1; i < progAvgWeights.length; i++) {
        // Runder forskellen af til én decimal
        weightIncreases.push(Number((progAvgWeights[i] - progAvgWeights[i - 1]).toFixed(1)));
      }
      // Vi bruger de labels, der svarer til ugerne fra og med den 2. uge
      const diffLabels = progLabels.slice(1);

      // Opret bar chart for average weight increase (progression)
      new Chart(progChartEl.getContext('2d'), {
        type: 'bar',
        data: {
          labels: diffLabels,
          datasets: [{
            label: 'Average Weight Increase (kg)',
            data: weightIncreases,
            backgroundColor: weightIncreases.map(diff => diff >= 0 ? '#28a745' : '#dc3545')
            // Grøn for positive stigninger, rød for negative
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Weight Increase (kg)'
              }
            },
            x: {
              title: {
                display: true,
                text: 'Week Range'
              }
            }
          },
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: function(context) {
                  return context.parsed.y + ' kg';
                }
              }
            }
          }
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
