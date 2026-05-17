# Carrossel de Depoimentos para Elementor

Este arquivo contém o código HTML/CSS/JS completo, isolado e otimizado para ser copiado e colado diretamente no widget **HTML Code** do Elementor.

## Correções Aplicadas nesta Versão:
1. **Vídeos do YouTube Corrigidos**: Trocado para o domínio principal `youtube.com`, adicionado o parâmetro `playsinline=1`, as permissões completas no `allow` e a política `referrerpolicy="strict-origin-when-cross-origin"` para evitar o erro de bloqueio de reprodução.
2. **Prints 100% Visíveis (Sem Cortes)**: Ajustado o contêiner de imagens para `height: 400px` com `object-fit: contain` e `padding: 16px`. Isso garante que prints longos de WhatsApp ou Instagram apareçam inteiros, sem cortar cabeçalho ou rodapé.

---

```html
<div class="elementor-custom-carousel-wrapper">
  <!-- Container Principal do Carrossel -->
  <div class="carousel-container" id="custom-depo-carousel">
    
    <!-- Track de Slides -->
    <div class="carousel-track" id="depo-track">
      
      <!-- ==================== VÍDEOS ==================== -->
      <!-- Slide 1: Fernanda Folle (Vídeo) -->
      <div class="carousel-slide card-type-video">
        <div class="slide-video-wrapper">
          <iframe 
            src="https://www.youtube.com/embed/K1O_x_HiYIo?rel=0&modestbranding=1&playsinline=1" 
            title="Depoimento Fernanda Folle" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen 
            referrerpolicy="strict-origin-when-cross-origin"
            loading="lazy">
          </iframe>
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Fernanda Folle • Nutri há 12 anos</h4>
          <p class="slide-desc">"Encontrei na Formação um caminho prático para viver de consultório de forma leve e com total segurança nas prescrições."</p>
        </div>
      </div>

      <!-- Slide 2: Adriana Guedes (Vídeo) -->
      <div class="carousel-slide card-type-video">
        <div class="slide-video-wrapper">
          <iframe 
            src="https://www.youtube.com/embed/I3q8K-Shdas?rel=0&modestbranding=1&playsinline=1" 
            title="Depoimento Adriana Guedes" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen 
            referrerpolicy="strict-origin-when-cross-origin"
            loading="lazy">
          </iframe>
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Adriana Guedes • Nutri há 17 anos</h4>
          <p class="slide-desc">"Nenhuma pós-graduação que fiz na vida entrega tudo que a Formação Nutrição Avançada entregou. Incrível."</p>
        </div>
      </div>

      <!-- Slide 3: Melissa Pinesso (Vídeo) -->
      <div class="carousel-slide card-type-video">
        <div class="slide-video-wrapper">
          <iframe 
            src="https://www.youtube.com/embed/Zhi-YzQCIw8?rel=0&modestbranding=1&playsinline=1" 
            title="Depoimento Melissa Pinesso" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen 
            referrerpolicy="strict-origin-when-cross-origin"
            loading="lazy">
          </iframe>
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Melissa Pinesso • Nutri & Aluna</h4>
          <p class="slide-desc">"Nos primeiros atendimentos após o curso pude me notar menos 'calculadora' e mais nutricionista, dando um novo significado e brilho nas minhas consultas."</p>
        </div>
      </div>

      <!-- ==================== CITAÇÕES COM AVATAR CIRCULAR ==================== -->
      <!-- Slide 4: Berty Song -->
      <div class="carousel-slide card-type-quote">
        <div class="avatar-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2023/09/depo-01.png" alt="Berty Song" loading="lazy" />
        </div>
        <h4 class="quote-author-name">BERTY SONG</h4>
        <p class="quote-author-role">Nutricionista recém-formada</p>
        <p class="quote-text">"<b>Antes eu era muito insegura.</b> A Nutrição Avançada mudou a minha vida, hoje em dia eu tenho mais pacientes e tenho mais tempo."</p>
      </div>

      <!-- Slide 5: Nair Cristina -->
      <div class="carousel-slide card-type-quote">
        <div class="avatar-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2023/09/depo-02.png" alt="Nair Cristina" loading="lazy" />
        </div>
        <h4 class="quote-author-name">NAIR CRISTINA</h4>
        <p class="quote-author-role">Nutricionista há 4 anos</p>
        <p class="quote-text">"Me sinto muito mais segura nas abordagens, <b>eu pego um paciente e sei o que fazer com ele em todas as fases com segurança.</b>"</p>
      </div>

      <!-- Slide 6: Nathalia Pantaleão -->
      <div class="carousel-slide card-type-quote">
        <div class="avatar-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2023/09/depo-03.png" alt="Nathalia Pantaleão" loading="lazy" />
        </div>
        <h4 class="quote-author-name">NATHALIA PANTALEÃO</h4>
        <p class="quote-author-role">Nutricionista há 3 anos</p>
        <p class="quote-text">"Tinha uma dificuldade para trabalhar com emagrecimento porque os pacientes não retornavam, eu aplicava tudo que tinha aprendido na faculdade, mas isso não gerava resultados. <b>Hoje meus pacientes indicam meu trabalho.</b>"</p>
      </div>

      <!-- ==================== PRINTS REAIS ==================== -->
      <!-- Slide 7: Curso Nutrição -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/09/curso-nutricao.jpg" alt="Depoimento Curso Nutrição" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Nutricionista Recém-Formada</h4>
          <p class="slide-desc">Formada no final de 2023, eliminou o medo de atender e recuperou o investimento da Formação rapidamente.</p>
        </div>
      </div>

      <!-- Slide 8: Compilado 1 -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/05/compilado-comprimido.jpg" alt="Compilado de Depoimentos" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Resultados de Consultório</h4>
          <p class="slide-desc">Compilado de alunos comemorando resultados reais, alta adesão dos pacientes e faturamento recorde.</p>
        </div>
      </div>

      <!-- Slide 9: Comprimido Site 1 -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/05/comprimido-site-1.jpg" alt="Depoimentos Site" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Segurança nas Prescrições</h4>
          <p class="slide-desc">Nutricionistas relatando a segurança clínica conquistada para conduzir casos difíceis e fidelizar pacientes.</p>
        </div>
      </div>

      <!-- Slide 10: Compilado 2 -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/05/compilado-comprimido-2.jpg" alt="Compilado 2" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Evolução na Prática Clínica</h4>
          <p class="slide-desc">Alunos compartilhando a evolução no consultório e o impacto das prescrições avançadas no dia a dia.</p>
        </div>
      </div>

      <!-- Slide 11: Comprimido Site -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/05/comprimido-site.jpg" alt="Comunidade" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Comunidade Ativa</h4>
          <p class="slide-desc">Grupo exclusivo onde nutricionistas trocam experiências e celebram o crescimento contínuo do consultório.</p>
        </div>
      </div>

      <!-- Slide 12: Dieta na Hora -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/09/curso-dieta-na-hora.jpg" alt="Dieta na Hora" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Plano Alimentar na Hora</h4>
          <p class="slide-desc">Ganhou agilidade e segurança para entregar a dieta na hora, encantando e fidelizando pacientes.</p>
        </div>
      </div>

      <!-- Slide 13: Compilado 3 -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/05/compilado-comprimido-3.jpg" alt="Compilado 3" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Autoridade e Reconhecimento</h4>
          <p class="slide-desc">Mais relatos de alunos que transformaram a insegurança em autoridade e reconhecimento profissional.</p>
        </div>
      </div>

      <!-- Slide 14: Enzo Print -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/05/enzo-print.jpg" alt="Enzo Print" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Domínio das Ferramentas</h4>
          <p class="slide-desc">Enzo comemorando o domínio das ferramentas e a clareza para aplicar a metodologia na prática diária.</p>
        </div>
      </div>

      <!-- Slide 15: Pacote 1k -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2024/09/print-pacote-1k.jpg" alt="Pacote 1k" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">Aluna FNA • Consultório</h4>
          <p class="slide-desc">Fechou seu primeiro pacote de acompanhamento de R$ 1.000,00 aplicando a estrutura de valor da Formação.</p>
        </div>
      </div>

      <!-- Slide 16: João Marcelo -->
      <div class="carousel-slide card-type-print">
        <div class="slide-img-wrapper">
          <img src="https://nutrineyfelipe.com/wp-content/uploads/2025/03/formacao-nutricao-avancada-resultados-depoimentos-joao.2.jpg" alt="João Marcelo" loading="lazy" />
        </div>
        <div class="slide-content">
          <h4 class="slide-title">João Marcelo • Aluno FNA</h4>
          <p class="slide-desc">Superou a insegurança clínica com casos complexos (SOP) e fechou acompanhamento trimestral à vista no Pix.</p>
        </div>
      </div>

    </div>

    <!-- Botões de Navegação Desktop -->
    <button class="carousel-nav nav-prev" id="nav-prev-btn" aria-label="Anterior">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
    </button>
    <button class="carousel-nav nav-next" id="nav-next-btn" aria-label="Próximo">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
    </button>

  </div>

  <!-- Indicadores / Dots -->
  <div class="carousel-dots" id="depo-dots"></div>
</div>

<style>
  /* Isolamento e Container */
  .elementor-custom-carousel-wrapper {
    position: relative;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px 0;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }

  .elementor-custom-carousel-wrapper * {
    box-sizing: border-box;
  }

  .carousel-container {
    position: relative;
    width: 100%;
    overflow: hidden;
    border-radius: 28px;
  }

  /* Track com Scroll Snap nativo (Instagram Style) */
  .carousel-track {
    display: flex;
    gap: 24px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    padding: 20px 16px;
    scrollbar-width: none; /* Firefox */
    cursor: grab;
  }

  .carousel-track::-webkit-scrollbar {
    display: none; /* Chrome/Safari */
  }

  .carousel-track.dragging {
    scroll-snap-type: none;
    scroll-behavior: auto;
    cursor: grabbing;
  }

  /* Estrutura Geral dos Slides */
  .carousel-slide {
    scroll-snap-align: center;
    flex-shrink: 0;
    width: 350px;
    max-width: 85vw;
    border-radius: 24px;
    overflow: hidden;
    background: #06111D;
    box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    transition: transform 0.3s ease, border-color 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .carousel-slide:hover {
    transform: translateY(-6px);
    border-color: rgba(0, 217, 255, 0.4);
    box-shadow: 0 20px 40px -10px rgba(0, 217, 255, 0.2);
  }

  /* =========== TIPO 1: VÍDEOS =========== */
  .slide-video-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #000;
    overflow: hidden;
  }

  .slide-video-wrapper iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
  }

  /* =========== TIPO 2: CITAÇÕES COM AVATAR CIRCULAR =========== */
  .card-type-quote {
    padding: 32px 24px 24px 24px;
    background: linear-gradient(145deg, #06111D 0%, #02070D 100%);
    text-align: center;
    justify-content: flex-start;
  }

  .avatar-wrapper {
    width: 96px;
    height: 96px;
    border-radius: 50%;
    overflow: hidden;
    margin: 0 auto 16px auto;
    border: 2px solid #00D9FF;
    box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
    flex-shrink: 0;
    background: #02070D;
  }

  .avatar-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
    display: block;
  }

  .quote-author-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: #00D9FF;
    margin: 0 0 4px 0;
    letter-spacing: 0.5px;
  }

  .quote-author-role {
    font-size: 0.9rem;
    color: #94A3B8;
    font-style: italic;
    margin: 0 0 20px 0;
  }

  .quote-text {
    font-size: 1.05rem;
    color: #F1F5F9;
    line-height: 1.6;
    margin: 0;
    font-weight: 300;
    text-align: left;
  }

  /* =========== TIPO 3: PRINTS REAIS (SEM CORTES) =========== */
  .slide-img-wrapper {
    width: 100%;
    height: 400px; /* Altura ampliada para prints longos */
    background: #02070D;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
    padding: 16px; /* Respiro interno para o print não tocar nas bordas */
  }

  .slide-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: contain; /* Garante que 100% do print seja visível sem NENHUM corte */
    object-position: center;
    display: block;
    transition: transform 0.5s ease;
    border-radius: 12px;
  }

  .carousel-slide:hover .slide-img-wrapper img {
    transform: scale(1.03);
  }

  .slide-content {
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.02), transparent);
    flex-grow: 1;
    justify-content: space-between;
  }

  .slide-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #00D9FF;
    margin: 0;
    letter-spacing: -0.3px;
  }

  .slide-desc {
    font-size: 0.95rem;
    color: #E2E8F0;
    line-height: 1.5;
    margin: 0;
    font-weight: 400;
  }

  /* Botões de Navegação Desktop */
  .carousel-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: rgba(2, 7, 13, 0.85);
    border: 1px solid rgba(0, 217, 255, 0.4);
    color: #00D9FF;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    transition: all 0.3s ease;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
  }

  .carousel-nav:hover {
    background: #00D9FF;
    color: #02070D;
    transform: translateY(-50%) scale(1.1);
  }

  .nav-prev { left: 16px; }
  .nav-next { right: 16px; }

  /* Indicadores / Dots */
  .carousel-dots {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 24px;
    padding: 0 16px;
  }

  .carousel-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    padding: 0;
  }

  .carousel-dot.active {
    width: 28px;
    border-radius: 100px;
    background: #00D9FF;
    box-shadow: 0 0 12px rgba(0, 217, 255, 0.6);
  }

  /* Oculta setas no Mobile (onde o touch swipe é nativo) */
  @media (max-width: 768px) {
    .carousel-nav { display: none; }
    .carousel-slide { width: 300px; }
    .slide-img-wrapper { height: 320px; }
    .slide-content { padding: 20px; }
  }
</style>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const track = document.getElementById("depo-track");
  const prevBtn = document.getElementById("nav-prev-btn");
  const nextBtn = document.getElementById("nav-next-btn");
  const dotsContainer = document.getElementById("depo-dots");
  const slides = Array.from(track.querySelectorAll(".carousel-slide"));

  if (!track || slides.length === 0) return;

  // Cria os Dots
  slides.forEach((_, index) => {
    const dot = document.createElement("button");
    dot.classList.add("carousel-dot");
    dot.setAttribute("aria-label", `Slide ${index + 1}`);
    if (index === 0) dot.classList.add("active");
    dot.addEventListener("click", () => goToSlide(index));
    dotsContainer.appendChild(dot);
  });

  const dots = Array.from(dotsContainer.querySelectorAll(".carousel-dot"));

  // Navegação para Slide específico
  function goToSlide(index) {
    if (index < 0 || index >= slides.length) return;
    const slide = slides[index];
    const trackRect = track.getBoundingClientRect();
    const slideRect = slide.getBoundingClientRect();
    const scrollPos = slide.offsetLeft - (track.clientWidth / 2) + (slide.clientWidth / 2);
    track.scrollTo({ left: scrollPos, behavior: "smooth" });
  }

  // Atualiza Dot Ativo no Scroll
  track.addEventListener("scroll", () => {
    const scrollCenter = track.scrollLeft + track.clientWidth / 2;
    let closestIndex = 0;
    let minDistance = Infinity;

    slides.forEach((slide, index) => {
      const slideCenter = slide.offsetLeft + slide.clientWidth / 2;
      const distance = Math.abs(scrollCenter - slideCenter);
      if (distance < minDistance) {
        minDistance = distance;
        closestIndex = index;
      }
    });

    dots.forEach((dot, idx) => {
      dot.classList.toggle("active", idx === closestIndex);
    });
  });

  // Botões Prev / Next
  prevBtn.addEventListener("click", () => {
    const slideWidth = slides[0].clientWidth + 24;
    track.scrollBy({ left: -slideWidth, behavior: "smooth" });
  });

  nextBtn.addEventListener("click", () => {
    const slideWidth = slides[0].clientWidth + 24;
    track.scrollBy({ left: slideWidth, behavior: "smooth" });
  });

  // Mouse Drag para Desktop
  let isDown = false;
  let startX;
  let scrollLeft;

  track.addEventListener("mousedown", (e) => {
    isDown = true;
    track.classList.add("dragging");
    startX = e.pageX - track.offsetLeft;
    scrollLeft = track.scrollLeft;
  });

  track.addEventListener("mouseleave", () => {
    isDown = false;
    track.classList.remove("dragging");
  });

  track.addEventListener("mouseup", () => {
    isDown = false;
    track.classList.remove("dragging");
  });

  track.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - track.offsetLeft;
    const walk = (x - startX) * 2; // Velocidade do arrasto
    track.scrollLeft = scrollLeft - walk;
  });
});
</script>
```
