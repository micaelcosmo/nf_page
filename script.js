document.addEventListener('DOMContentLoaded', () => {

    // 1. CÓDIGO DO INTERSECTION OBSERVER (EFEITO FADE-IN AO ROLAR)
    const fadeElements = document.querySelectorAll('.fade-element');
    const options = {
        root: null, 
        rootMargin: '5px',
        threshold: 0.3
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, options);

    fadeElements.forEach(element => {
        observer.observe(element);
    });

    // -------------------------------------------
    // 2. CONTROLE DE ÁUDIO DE FUNDO (SOLUÇÃO MOBILE ROBUSTA)
    // -------------------------------------------
    const music = document.getElementById('background-music');
    let audioStarted = false;

    if (music) {
        music.muted = true;
        music.play().catch(error => {
            // Se falhar (o que é comum em mobile), não há problema. Esperamos a interação.
        });

        function startAudio() {
            if (!audioStarted) {
                music.muted = false;
                music.play().then(() => {
                    audioStarted = true;
                    document.removeEventListener('click', startAudio);
                    document.removeEventListener('touchstart', startAudio);
                    document.removeEventListener('scroll', startAudio);
                }).catch(error => {
                    music.muted = true;
                    music.play();
                    audioStarted = true;
                    document.removeEventListener('click', startAudio);
                    document.removeEventListener('touchstart', startAudio);
                    document.removeEventListener('scroll', startAudio);
                });
            }
        }

        document.addEventListener('click', startAudio);
        document.addEventListener('touchstart', startAudio);
        document.addEventListener('scroll', startAudio);
    }

    // -------------------------------------------
    // 3. LÓGICA DO BOTÃO WHATSAPP (NOVO)
    // -------------------------------------------
    const whatsappButton = document.getElementById('assinatura-final');

    if (whatsappButton) {
        const phoneNumber = '5561982907143';
        const message = 'Olá, gostaria de agendar uma aula experimental.';
        
        // Codifica a mensagem para ser usada em uma URL de forma segura
        const encodedMessage = encodeURIComponent(message);
        
        const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedMessage}`;

        // Opcional, mas recomendado: define o href para que o usuário veja o link
        whatsappButton.href = whatsappUrl;

        whatsappButton.addEventListener('click', (event) => {
            // Previne o comportamento padrão do link, se houver um href="#"
            event.preventDefault(); 
            
            // Abre a URL do WhatsApp em uma nova aba
            window.open(whatsappUrl, '_blank');
        });
    }
});