document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function (event) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                event.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    const scene = document.querySelector('.space-scene');
    if (scene) {
        for (let i = 0; i < 10; i += 1) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.width = `${4 + Math.random() * 8}px`;
            star.style.height = star.style.width;
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.animationDelay = `${Math.random() * 2}s`;
            star.style.opacity = `${0.4 + Math.random() * 0.6}`;
            scene.appendChild(star);
        }
    }
});
