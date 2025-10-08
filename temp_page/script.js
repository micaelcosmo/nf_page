document.addEventListener('DOMContentLoaded', () => {

    // 1. CÓDIGO DO INTERSECTION OBSERVER (EFEITO FADE-IN AO ROLAR)
    // Esta parte do código continua funcionando perfeitamente, pois busca
    // por elementos com a classe '.fade-element', que mantivemos no novo HTML.
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
    // Esta funcionalidade também é ideal para a página da escola de dança,
    // criando um ambiente imersivo. O código inicia a música assim que o
    // usuário interage com a página (clique, toque ou rolagem).
    const music = document.getElementById('background-music');
    let audioStarted = false; // Flag para garantir que o áudio só inicie uma vez

    if (music) {
        // Tenta dar play no modo mudo no início, por segurança e compatibilidade inicial.
        music.muted = true;
        music.play().catch(error => {
            // Se falhar (o que é comum em mobile), não há problema. Esperamos a interação.
        });

        // Função para iniciar o áudio (com som) no primeiro toque/interação
        function startAudio() {
            if (!audioStarted) {
                music.muted = false; // Tenta desmutar
                music.play().then(() => {
                    // Sucesso: Áudio iniciou com som. Remove os listeners.
                    audioStarted = true;
                    document.removeEventListener('click', startAudio);
                    document.removeEventListener('touchstart', startAudio);
                    document.removeEventListener('scroll', startAudio);
                }).catch(error => {
                    // Se o navegador ainda bloquear o som, garante que a música toque no mudo.
                    music.muted = true;
                    music.play();
                    audioStarted = true;
                    document.removeEventListener('click', startAudio);
                    document.removeEventListener('touchstart', startAudio);
                    document.removeEventListener('scroll', startAudio);
                });
            }
        }

        // Adiciona os listeners de eventos de interação mais comuns:
        document.addEventListener('click', startAudio);      // Clique (desktop)
        document.addEventListener('touchstart', startAudio); // Toque na tela (mobile)
        document.addEventListener('scroll', startAudio);     // Rolagem
    }
});