/* ================================================================
   SKILL BRIDGE — Shared Chart.js Config
   Universal configurations, color systems, and responsiveness settings for dashboard graphs
   ================================================================ */

// Global Chart configurations
if (typeof Chart !== 'undefined') {
    // Set global font defaults
    Chart.defaults.font.family = "'Inter', sans-serif";
    Chart.defaults.font.size = 11;
    Chart.defaults.plugins.tooltip.padding = 10;
    Chart.defaults.plugins.tooltip.cornerRadius = 8;
    Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(15, 23, 42, 0.9)';
    Chart.defaults.plugins.tooltip.titleFont = { weight: 'bold', size: 12 };
    Chart.defaults.plugins.tooltip.bodyFont = { size: 12 };
}

const ChartThemes = {
    colors: {
        primary: '#0A66C2',
        primaryLight: 'rgba(10, 102, 194, 0.1)',
        success: '#059669',
        successLight: 'rgba(5, 150, 105, 0.1)',
        accent: '#7C3AED',
        accentLight: 'rgba(124, 58, 237, 0.1)',
        warning: '#D97706',
        warningLight: 'rgba(217, 119, 6, 0.1)',
        danger: '#DC2626',
        info: '#0891B2'
    },

    getGridColor() {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        return isDark ? '#334155' : '#E2E8F0';
    },

    getTextColor() {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        return isDark ? '#94A3B8' : '#666666';
    }
};

// Expose universal chart generator helpers
const SkillBridgeCharts = {
    // Generate a standard double-dataset line chart
    createDoubleLineChart(elementId, label1, data1, label2, data2, labels) {
        const ctx = document.getElementById(elementId);
        if (!ctx) return null;

        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: label1,
                    data: data1,
                    borderColor: ChartThemes.colors.primary,
                    backgroundColor: ChartThemes.colors.primaryLight,
                    borderWidth: 2.5,
                    fill: true,
                    tension: 0.4
                },
                {
                    label: label2,
                    data: data2,
                    borderColor: ChartThemes.colors.success,
                    backgroundColor: 'transparent',
                    borderWidth: 2,
                    borderDash: [6, 6],
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: ChartThemes.getTextColor(),
                            boxWidth: 12,
                            padding: 15
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: ChartThemes.getTextColor() },
                        grid: { color: ChartThemes.getGridColor() }
                    },
                    x: {
                        ticks: { color: ChartThemes.getTextColor() },
                        grid: { display: false }
                    }
                }
            }
        });
    },

    // Generate a standard bar chart
    createBarChart(elementId, datasetLabel, data, labels, barColor = 'primary') {
        const ctx = document.getElementById(elementId);
        if (!ctx) return null;

        const colorHex = ChartThemes.colors[barColor] || ChartThemes.colors.primary;

        return new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: datasetLabel,
                    data: data,
                    backgroundColor: colorHex,
                    borderRadius: 6,
                    borderWidth: 0,
                    barThickness: 16
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: ChartThemes.getTextColor() },
                        grid: { color: ChartThemes.getGridColor() }
                    },
                    x: {
                        ticks: { color: ChartThemes.getTextColor() },
                        grid: { display: false }
                    }
                }
            }
        });
    },

    // Generate a standard donut chart for distributions
    createDonutChart(elementId, labels, data) {
        const ctx = document.getElementById(elementId);
        if (!ctx) return null;

        return new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: [
                        ChartThemes.colors.primary,
                        ChartThemes.colors.success,
                        ChartThemes.colors.accent,
                        ChartThemes.colors.warning
                    ],
                    borderWidth: 2,
                    borderColor: document.documentElement.getAttribute('data-theme') === 'dark' ? '#1E293B' : '#FFFFFF'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: ChartThemes.getTextColor(),
                            boxWidth: 10,
                            padding: 12
                        }
                    }
                },
                cutout: '70%'
            }
        });
    }
};

// Monitor theme changes to redraw chart styles dynamically
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    // Charts need to be manually updated if redraw is required
});
document.addEventListener('click', (e) => {
    if (e.target.closest('.theme-toggle')) {
        // Delay slightly to wait for DOM update
        setTimeout(() => {
            // Re-render chart configs if instances exist (handled by pages or global redraw)
        }, 100);
    }
});
