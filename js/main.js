// NEXUS ALPHA - JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll para links internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Contador para o preço (efeito de digitação)
    const priceElement = document.querySelector('.price');
    if(priceElement) {
        const originalPrice = priceElement.textContent;
        priceElement.textContent = '';
        let i = 0;
        function typePrice() {
            if(i < originalPrice.length) {
                priceElement.textContent += originalPrice.charAt(i);
                i++;
                setTimeout(typePrice, 50);
            }
        }
        setTimeout(typePrice, 1000);
    }
    
    // Animação para cards de benefícios
    const benefitCards = document.querySelectorAll('.benefit-card');
    benefitCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
    
    // Atualizar ano no footer
    const yearElement = document.querySelector('#current-year');
    if(yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
    
    // Log de clique nos botões
    document.querySelectorAll('.btn-main, .btn-nav').forEach(btn => {
        btn.addEventListener('click', function() {
            console.log('Botão clicado:', this.textContent);
            // Aqui você pode adicionar Google Analytics ou outros trackers
        });
    });
});
