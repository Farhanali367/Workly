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

    // Chart.js Instance for Company Admin Funnel
    const ctx = document.getElementById('funnelChart');
    if(ctx) {
        new Chart(ctx, {
            type: 'bar', // Visualized as bar imitating a funnel for simplicity
            data: {
                labels: ['Applied', 'Reviewed', 'Shortlisted', 'Interviewed', 'Offered', 'Hired'],
                datasets: [{
                    label: 'Candidates',
                    data: [1245, 800, 300, 150, 40, 14],
                    backgroundColor: [
                        '#93C5FD',
                        '#60A5FA',
                        '#3B82F6',
                        '#2563EB',
                        '#1D4ED8',
                        '#10B981' // Green for hired
                    ],
                    borderWidth: 0,
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        backgroundColor: '#1E293B',
                        padding: 10
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
