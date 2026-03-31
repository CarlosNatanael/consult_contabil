// Aguarda todo o HTML ser carregado antes de rodar o JS
document.addEventListener('DOMContentLoaded', () => {

    // ==========================================
    // 1. CURSOR PERSONALIZADO
    // ==========================================
    const cursor = document.getElementById('cursor');
    const ring = document.getElementById('cursorRing');
    
    // Só executa se o cursor existir no HTML
    if (cursor && ring) {
        let mx = 0, my = 0, rx = 0, ry = 0;
        
        document.addEventListener('mousemove', e => { 
            mx = e.clientX; 
            my = e.clientY; 
        });
        
        function animCursor() {
            cursor.style.left = mx + 'px';
            cursor.style.top = my + 'px';
            rx += (mx - rx) * 0.12;
            ry += (my - ry) * 0.12;
            ring.style.left = rx + 'px';
            ring.style.top = ry + 'px';
            requestAnimationFrame(animCursor);
        }
        animCursor();
        
        document.querySelectorAll('a, button, .service-card, .pillar, .testimonial-card, .process-step').forEach(el => {
            el.addEventListener('mouseenter', () => { 
                ring.style.transform = 'translate(-50%,-50%) scale(1.8)'; 
                ring.style.opacity = '0.3'; 
            });
            el.addEventListener('mouseleave', () => { 
                ring.style.transform = 'translate(-50%,-50%) scale(1)'; 
                ring.style.opacity = '0.6'; 
            });
        });
    }

    // ==========================================
    // 2. NAV SCROLL (Menu muda de cor ao rolar)
    // ==========================================
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        });
    }

    // ==========================================
    // 3. REVEAL ON SCROLL (Animações de entrada)
    // ==========================================
    const observer = new IntersectionObserver(entries => {
        entries.forEach(e => { 
            if (e.isIntersecting) {
                e.target.classList.add('visible'); 
            }
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    
    document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => observer.observe(el));

    // ==========================================
    // 4. SMOOTH SCROLL (Rolagem suave dos links)
    // ==========================================
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            const targetAttr = a.getAttribute('href');
            // Ignora se for apenas um "#" vazio
            if(targetAttr !== '#') {
                e.preventDefault();
                const targetElement = document.querySelector(targetAttr);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // ==========================================
    // 5. COUNTER ANIMATION (Animação de números)
    // ==========================================
    function animateCount(el, target, suffix = '') {
        let current = 0;
        const step = target / 60;
        const timer = setInterval(() => {
            current = Math.min(current + step, target);
            el.textContent = Math.floor(current) + suffix;
            if (current >= target) clearInterval(timer);
        }, 16);
    }
    
    const statsObs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                document.querySelectorAll('.hero-stat-num').forEach(el => {
                    const t = el.textContent;
                    if (t.includes('+')) animateCount(el, parseInt(t), '+');
                    else if (t.includes('%')) animateCount(el, parseInt(t), '%');
                });
                statsObs.disconnect();
            }
        });
    }, { threshold: 0.5 });
    
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        statsObs.observe(heroStats);
    }
});