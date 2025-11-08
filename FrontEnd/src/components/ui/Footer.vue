<template>
  <footer class="footer">
    <div class="footer__content">
      <p class="footer__info">
        Proyecto <strong>IA Consciente</strong> — desarrollado para la
        <a class="highlight" href="https://ciberpaz.gov.co/">Hackatón Ciberpaz 2025</a> del Ministerio TIC de Colombia.
      </p>

      <p class="footer__meta">
        <a href="https://github.com/L3X1-22/IA-consciente" target="_blank" rel="noopener noreferrer">
          Repositorio en GitHub
        </a>
        &nbsp;•&nbsp;
        <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">
          Licencia CC BY-SA 4.0
        </a>
        &nbsp;•&nbsp;
        © {{ currentYear }} — Johan Santiago Camargo Olmos, Miguel Ángel Quintero Puentes,
        Alexia Gutiérrez Niño, Juliana Gutiérrez Rodríguez y Angie Lorena Gonzales Riaño.
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      currentYear: new Date().getFullYear()
    }
  }
}
</script>

<style scoped>
.footer {
  position: relative;
  width: 100%;
  min-height: 10vh;
  max-height: 20vh;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(6px);
  color: rgba(255, 255, 255, 0.9);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 2rem;
  box-sizing: border-box;
}

.footer__content {
  max-width: 1100px;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.footer__info {
  margin: 0;
  font-size: 0.95rem;
}

.footer__meta {
  margin: 0;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.4;
}

.footer__meta a {
  color: var(--blue-ai);
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer__meta a:hover {
  color: var(--yellow-contrast);
}

.highlight {
  color: var(--purple-accent);
  font-weight: 600;
  transition: color 0.6s ease, transform 0.3s ease;
}

.highlight:hover {
  transform: scale(0.96);
  color: var(--pink-support, #ff6bcb);
}

/* Responsivo */
@media (max-width: 640px) {
  .footer {
    padding: 1rem;
  }

  .footer__content {
    gap: 0.6rem;
  }

  .footer__meta {
    font-size: 0.8rem;
  }
}
</style>
