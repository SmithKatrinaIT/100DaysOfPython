// Ensure the entire script waits for the HTML elements to exist
document.addEventListener("DOMContentLoaded", () => {

    // --- 1. MOBILE NAVIGATION CONTROL ---
    (() => {
        const toggle = document.querySelector('.nav-toggle');
        const menu = document.getElementById('nav-menu');

        // If this page doesn't have a navbar, safely exit THIS function only
        if (!toggle || !menu) return;

        toggle.addEventListener('click', function () {
            const expanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', String(!expanded));
            menu.classList.toggle('nav-links--open');
        });

        document.addEventListener('click', function (e) {
            if (!toggle.contains(e.target) && !menu.contains(e.target)) {
                toggle.setAttribute('aria-expanded', 'false');
                menu.classList.remove('nav-links--open');
            }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                toggle.setAttribute('aria-expanded', 'false');
                menu.classList.remove('nav-links--open');
                toggle.focus();
            }
        });
    })();


    // --- 2. REVEAL ON SCROLL ANIMATION ---
    (() => {
        if (!window.IntersectionObserver) return;

        const els = document.querySelectorAll('.reveal');

        // If this page doesn't have any scroll-reveal elements, exit safely
        if (els.length === 0) return;

        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target); //
                }
            });
        }, { threshold: 0.1 }); //

        els.forEach(function (el) { observer.observe(el); });
    })();

});

