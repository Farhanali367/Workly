/* ================================================================
   SKILL BRIDGE — Recruiter Module JS
   Sidebar control and dashboard analytics for recruiter portal
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

    // Chart.js for Recruiter Activity Dashboard
    const ctx = document.getElementById('recruiterActivityChart');
    if(ctx && typeof SkillBridgeCharts !== 'undefined') {
        SkillBridgeCharts.createDoubleLineChart(
            'recruiterActivityChart',
            'Sourced Candidates', [12, 19, 32, 25, 40, 52],
            'Interviews Conducted', [4, 8, 15, 12, 22, 28],
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        );
    }
});
