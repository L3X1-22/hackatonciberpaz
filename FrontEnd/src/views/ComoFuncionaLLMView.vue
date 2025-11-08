<template>
  <div class="llm-view">
    <div class="grid-llm">
      <!-- 🔹 Texto izquierdo -->
      <div class="llm-text left">
        <SimpleTextBlock
          title="Procesamiento del lenguaje"
          text="Los LLM analizan el texto descomponiéndolo en unidades llamadas tokens. Cada token representa una palabra o fragmento de palabra, lo que permite entender estructuras y contextos."
        />
      </div>

      <!-- 🔹 Imagen central -->
      <div class="llm-image">
        <img
          src="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1920&q=80"
          alt="Red neuronal representando un modelo de lenguaje"
        />
      </div>

      <!-- 🔹 Texto derecho -->
      <div class="llm-text right">
        <SimpleTextBlock
          title="Predicción y contexto"
          text="A partir del contexto previo, el modelo predice la siguiente palabra más probable. Este proceso ocurre miles de veces por segundo, generando respuestas coherentes y fluidas."
        />
      </div>

      <!-- 🔹 Texto inferior -->
      <div class="llm-text bottom">
        <SimpleTextBlock
          title="Aprendizaje continuo"
          text="Los LLM mejoran con grandes volúmenes de datos, ajustando internamente millones de parámetros que determinan cómo se relacionan las palabras y los conceptos."
        />
      </div>
    </div>
  </div>
</template>

<script>
import SimpleTextBlock from '@/components/ui/SimpleTextBlock.vue'

export default {
  name: 'ComoFuncionaLLMView',
  components: {
    SimpleTextBlock
  }
}
</script>

<style scoped>
.llm-view {
  width: 100%;
  min-height: 100vh;
  padding-top: 90px; /* espacio para el nav fijo */
  background: radial-gradient(circle at center, #0d0d0d 0%, #121212 100%);
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.grid-llm {
  display: grid;
  grid-template-columns: 1fr 1.2fr 1fr;
  grid-template-rows: auto auto;
  gap: 2rem;
  max-width: 1400px;
  width: 100%;
  padding: 2rem;
  align-items: center;
}

/* 🔹 Imagen central grande */
.llm-image {
  grid-column: 2 / span 1;
  grid-row: 1 / span 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.llm-image img {
  width: 100%;
  max-width: 600px;
  height: auto;
  border-radius: 1rem;
  object-fit: cover;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.4);
  transition: transform 0.4s ease;
}

.llm-image img:hover {
  transform: scale(1.03);
}

/* 🔹 Posiciones */
.llm-text.left {
  grid-column: 1;
  grid-row: 1;
}

.llm-text.right {
  grid-column: 3;
  grid-row: 1;
}

.llm-text.bottom {
  grid-column: 1 / span 3;
  grid-row: 2;
  display: flex;
  justify-content: center;
}

/* 🔹 Responsivo - tablet */
@media (max-width: 1024px) {
  .grid-llm {
    grid-template-columns: 1fr 1fr;
  }

  .llm-text.left {
    grid-column: 1;
    grid-row: 1;
  }

  .llm-image {
    grid-column: 2;
    grid-row: 1;
  }

  .llm-text.right {
    grid-column: 1 / span 2;
    grid-row: 2;
  }

  .llm-text.bottom {
    grid-column: 1 / span 2;
    grid-row: 3;
  }
}

/* 🔹 Responsivo - móvil */
@media (max-width: 768px) {
  .grid-llm {
    grid-template-columns: 1fr;
  }

  .llm-text.left,
  .llm-text.right,
  .llm-text.bottom,
  .llm-image {
    grid-column: 1;
  }

  .llm-text.left {
    grid-row: 1;
  }

  .llm-image {
    grid-row: 2;
  }

  .llm-text.right {
    grid-row: 3;
  }

  .llm-text.bottom {
    grid-row: 4;
  }

  .llm-image img {
    max-width: 100%;
  }
}
</style>
