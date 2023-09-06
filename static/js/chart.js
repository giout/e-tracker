const chart = document.getElementById('chart')

if (chart) {
    const ctx = chart.getContext('2d')

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
              data: [300, 50, 100],
              backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
              ],
            }]
        }
    })
}