// Use Chart.js to create charts based on your data
// Example usage:
var topInterestsData = {
    labels: ["Interest 1", "Interest 2", "Interest 3", "Interest 4", "Interest 5"],
    datasets: [{
        label: 'Top Interests',
        data: [10, 8, 6, 4, 2],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

var topInterestsOptions = {
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

var topInterestsChart = new Chart(document.getElementById('topInterestsChart'), {
    type: 'bar',
    data: topInterestsData,
    options: topInterestsOptions
});

// Add more charts as needed
