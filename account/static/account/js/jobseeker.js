document.addEventListener('DOMContentLoaded', () => {
    
    // Sidebar Mobile Toggle
    const sidebar = document.getElementById('sidebar');
    const openBtn = document.getElementById('openSidebar');
    const closeBtn = document.getElementById('closeSidebar');

    if(sidebar && openBtn && closeBtn) {
        openBtn.addEventListener('click', () => {
            sidebar.classList.add('show');
        });
        closeBtn.addEventListener('click', () => {
            sidebar.classList.remove('show');
        });
    }

    // Chart.js Instance for Job Seeker Dashboard
    const ctx = document.getElementById('applicationChart');
    if(ctx) {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Applications Sent',
                    data: [2, 5, 8, 3, 12, 7],
                    borderColor: '#0A66C2',
                    backgroundColor: 'rgba(10, 102, 194, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.4
                },
                {
                    label: 'Profile Views',
                    data: [10, 25, 18, 45, 80, 60],
                    borderColor: '#10B981',
                    borderDash: [5, 5],
                    backgroundColor: 'transparent',
                    borderWidth: 2,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0,0,0,0.05)'
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
    }

});
