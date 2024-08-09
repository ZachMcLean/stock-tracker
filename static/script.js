document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('stockChart').getContext('2d');
    var labels = [];
    var dataOpen = [];
    var dataClose = [];

    {% if stock_data %}
    {% for date, data in stock_data.items() %}
    labels.push("{{ date }}");
    dataOpen.push({{ data['1. open'] }});
    dataClose.push({{ data['4. close'] }});
    {% endfor %}
    {% endif %}

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Open Price',
                    data: dataOpen,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                },
                {
                    label: 'Close Price',
                    data: dataClose,
                    borderColor: 'rgba(153, 102, 255, 1)',
                    backgroundColor: 'rgba(153, 102, 255, 0.2)',
                }
            ]
        },
        options: {
            scales: {
                x: {
                    beginAtZero: true
                },
                y: {
                    beginAtZero: false
                }
            }
        }
    });
});

