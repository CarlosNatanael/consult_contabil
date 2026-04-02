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

    // ==========================================
    // MENU MOBILE (Hambúrguer)
    // ==========================================
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    if (hamburger && navLinks) {
        // Abre e fecha o menu ao clicar no ícone
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // Fecha o menu automaticamente quando o cliente clica em algum link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }

    // ==========================================
    // MODAL DE SERVIÇOS E DADOS
    // ==========================================
    const modal = document.getElementById('servicoModal');
    const fecharModal = document.getElementById('fecharModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalText = document.getElementById('modalText');
    const modalIcon = document.getElementById('modalIcon');

    // O nosso "Banco de Dados" local com os resumos
    const dadosServicos = {
        "Abertura de Empresas": {
            icon: "<i class='bi bi-building'></i>",
            texto: "Cuidamos de toda a burocracia para que possa começar o seu negócio com o pé direito. Realizamos a elaboração do contrato social, registo nos órgãos competentes, emissão de NIF/CNPJ e alvarás. Garantimos que a sua empresa nasça 100% regularizada e enquadrada no melhor regime tributário para pagar apenas os impostos devidos por lei."
        },
        "Regularização de MEI": {
            icon: "<i class='bi bi-card-checklist'></i>",
            texto: "Está com declarações atrasadas ou guias pendentes? Nós resolvemos. Fazemos o levantamento completo da sua situação, estruturamos planos de pagamento e regularizamos o seu perfil junto da Autoridade Tributária. Evite multas, perda de benefícios ou o cancelamento da sua atividade."
        },
        "Declaração IRPF MEI": {
            icon: "<i class='bi bi-file-earmark-bar-graph'></i>",
            texto: "A confusão entre finanças pessoais e empresariais é um grande risco. Realizamos os cálculos exatos da sua parcela isenta e tributável, elaborando a sua Declaração de Rendimentos com total segurança. Evite cair na 'malha fina' ou pagar impostos desnecessários através de um planeamento cuidado."
        },
        "Plano de Carreira": {
            icon: "<i class='bi bi-graph-up-arrow'></i>",
            texto: "Reter os melhores talentos é essencial para o crescimento sustentável. Estruturamos planos de carreira claros e objetivos para a sua equipa, definindo critérios de progressão, faixas salariais e benefícios. Isto aumenta a motivação dos colaboradores e traz segurança jurídica contra eventuais litígios laborais."
        },
        "Descrição de Cargos": {
            icon: "<i class='bi bi-people'></i>",
            texto: "Mapeamos e documentamos detalhadamente as responsabilidades, requisitos e competências de cada função dentro da sua empresa. Uma descrição bem feita organiza a rotina, facilita processos de contratação e é a peça fundamental para garantir a equidade interna e o cumprimento rigoroso da legislação do trabalho."
        },
        "Consultoria Fiscal": {
            icon: "<i class='bi bi-calculator'></i>",
            texto: "Uma análise profunda da operação da sua empresa para identificar oportunidades de poupança (Elisão Fiscal). Revisamos a tributação atual, recuperamos valores pagos a mais e desenvolvemos um planeamento estratégico focado em aumentar a sua margem de lucro de forma totalmente legal e segura."
        }
    };

    // Abre o modal APENAS ao clicar na setinha "Saiba mais ->"
    document.querySelectorAll('.service-arrow').forEach(botao => {
        botao.addEventListener('click', (evento) => {
            // Garante que o clique não ativa outras coisas acidentalmente
            evento.stopPropagation();
            
            // Procura o cartão (pai) a que esta setinha pertence para ler o título
            const card = botao.closest('.service-card');
            const titulo = card.querySelector('.service-title').innerText;
            const dados = dadosServicos[titulo];
            
            if (dados) {
                modalTitle.innerText = titulo;
                modalText.innerText = dados.texto;
                modalIcon.innerHTML = dados.icon;
                modal.classList.add('active');
            }
        });
    });

    // Fecha o modal ao clicar no X
    if (fecharModal) {
        fecharModal.addEventListener('click', () => {
            modal.classList.remove('active');
        });
    }

    // Fecha o modal se clicar fora da caixa (na parte escura)
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    }
});