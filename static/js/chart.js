const chart = document.getElementById('chart')

// obtaining colors from DOM (legend panel)
const legendColors = document.getElementsByClassName('legend-color')
const colors = Array.from(legendColors).map(legend => {
  return legend.style.backgroundColor
})

// obtaining each percentage
const percentageHeaders = document.getElementsByClassName('percentage')
const percentages = Array.from(percentageHeaders).map(percentage => {
  return percentage.innerHTML
})


if (chart) {
    const ctx = chart.getContext('2d')

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
              data: percentages,
              backgroundColor: colors
            }]
        }
    })
}