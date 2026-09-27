/* ================================================================
   SKILL BRIDGE — Super Admin Module JS
   Sidebar, theme adjustments, and administrative analytics
   ================================================================ */

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

    // Chart.js for Admin Registration Growth
    const growthCtx = document.getElementById('adminGrowthChart');
    if(growthCtx && typeof SkillBridgeCharts !== 'undefined') {
        SkillBridgeCharts.createDoubleLineChart(
            'adminGrowthChart',
            'Job Seekers Added', [200, 350, 480, 600, 850, 1100],
            'Companies Registered', [10, 25, 38, 52, 70, 95],
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        );
    }

    // Chart.js for Admin Revenue Distribution
    const revCtx = document.getElementById('adminRevenueChart');
    if(revCtx && typeof SkillBridgeCharts !== 'undefined') {
        SkillBridgeCharts.createDonutChart(
            'adminRevenueChart',
            ['Enterprise Plan', 'Professional Plan', 'Recruiter Postings', 'Ads & Featured'],
            [55, 25, 12, 8]
        );
    }
});
