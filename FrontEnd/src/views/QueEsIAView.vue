<template>
  <div class="que-es-ia-view">
    <div class="content-grid">
      <!-- 🔹 Fila superior -->
      <div class="feature-top">
        <FeatureCard
          title="¿Qué es la Inteligencia Artificial?"
          description="La inteligencia artificial (IA) busca crear sistemas capaces de realizar tareas que normalmente requieren inteligencia humana, desde reconocer patrones hasta tomar decisiones complejas."
          image="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1920&q=80"
        />
      </div>

      <div class="text-top">
        <SimpleTextBlock
          title="Más que una herramienta"
          text="La IA no es solo tecnología; es una extensión de nuestra forma de pensar, crear y resolver problemas. Su evolución redefine lo que significa ser humano en la era digital."
        />
      </div>

      <!-- 🔹 Fila inferior -->
      <div class="text-bottom">
        <SimpleTextBlock
          title="IA débil, fuerte y general"
          text="Mientras la IA débil está diseñada para tareas específicas, la IA fuerte o general aspira a reproducir la adaptabilidad y el razonamiento humano."
        />
      </div>

      <div class="feature-bottom">
        <FeatureCard
          title="Aprendizaje continuo"
          description="Los modelos de IA aprenden de la experiencia, refinando sus resultados mediante datos y retroalimentación. Este proceso impulsa avances en múltiples disciplinas."
          image="https://images.unsplash.com/photo-1508385082359-f38ae991e8f2?auto=format&fit=crop&w=1920&q=80"
          :reverse="true"
        />
      </div>
    </div>
  </div>
</template>

<script>
import FeatureCard from '@/components/ui/FeatureCard.vue'
import SimpleTextBlock from '@/components/ui/SimpleTextBlock.vue'

export default {
  name: 'QueEsIAView',
  components: {
    FeatureCard,
    SimpleTextBlock
  }
}
</script>

<style scoped>
.que-es-ia-view {
  width: 100%;
  min-height: 100vh;
  padding-top: 90px; /* espacio para el nav fijo */
  background: linear-gradient(180deg, #0a0a0a 0%, #151515 100%);
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  justify-content: center;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 2rem;
  max-width: 1400px;
  width: 100%;
  padding: 2rem;
}

/* 🔹 Posicionamiento en desktop (3 columnas) */
.feature-top {
  grid-column: 1 / span 2;
  grid-row: 1;
}

.text-top {
  grid-column: 3 / span 1;
  grid-row: 1;
}

.text-bottom {
  grid-column: 1 / span 1;
  grid-row: 2;
}

.feature-bottom {
  grid-column: 2 / span 2;
  grid-row: 2;
}

/* 🔹 Alineación general */
.feature-top,
.feature-bottom,
.text-top,
.text-bottom {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 🔹 Responsivo - tablets */
/* @media (max-width: 1024px) {
  .content-grid {
    grid-template-columns: 1fr 1fr;
  }

  .feature-top {
    grid-column: 1 / span 2;
    grid-row: 1;
  }

  .text-top {
    grid-column: 1 / span 2;
    grid-row: 2;
  }

  .text-bottom {
    grid-column: 1 / span 2;
    grid-row: 3;
  }

  .feature-bottom {
    grid-column: 1 / span 2;
    grid-row: 4;
  }
} */

/* 🔹 Responsivo - móviles */
@media (max-width: 768px) {
  .content-grid {
    grid-template-columns: 1fr;
  }

  .feature-top {
    grid-column: 1;
    grid-row: 1;
  }

  .text-top {
    grid-column: 1;
    grid-row: 2;
  }

  .text-bottom {
    grid-column: 1;
    grid-row: 3;
  }

  .feature-bottom {
    grid-column: 1;
    grid-row: 4;
  }
}
</style>
