<template>
  <div class="entorno-academico">
    <div class="background__overlay"></div>

    <div class="grid-layout">
      <!-- Fila 1 -->
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Usa IA para aprender"
          description="Aprende a usar herramientas de IA que potencian tu comprensión en lugar de reemplazar tu pensamiento crítico."
          image="https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=800&q=80"
        />
      </div>
      <div class="grid-cell"></div>
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Crea con propósito"
          description="Usa la inteligencia artificial como un apoyo creativo, no como sustituto de tus ideas."
          image="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80"
        />
      </div>

      <!-- Fila 2 -->
      <div class="grid-cell"></div>
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Apoya tu investigación"
          description="Deja que la IA te ayude a buscar fuentes y estructurar ideas, manteniendo siempre la verificación humana."
          image="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80"
        />
      </div>
      <div class="grid-cell"></div>

      <!-- Fila 3 -->
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Colabora inteligentemente"
          description="Aprovecha la IA para mejorar el trabajo en equipo y la comunicación académica."
          image="https://images.unsplash.com/photo-1581093588401-22dba1e3e5af?auto=format&fit=crop&w=800&q=80"
        />
      </div>
      <div class="grid-cell"></div>
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Desarrolla tu propio estilo"
          description="Usa la IA como inspiración, pero deja que tus palabras y pensamiento sigan siendo tuyos."
          image="https://images.unsplash.com/photo-1529101091764-c3526daf38fe?auto=format&fit=crop&w=800&q=80"
        />
      </div>
    </div>
  </div>
</template>

<script>
import FeatureCard from '@/components/ui/FeatureCard.vue'

export default {
  name: 'EntornoAcademicoView',
  components: { FeatureCard }
}
</script>

<style scoped>
.entorno-academico {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow-y: auto;
  padding-top: 6rem; /* dejar espacio por el nav fijo */
  background: linear-gradient(to bottom right, #0b0b0b, #1a1a1a);
}

.grid-layout {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(250px, auto);
  gap: 2rem;
  padding: 3rem;
  z-index: 2;
}

/* Centrado de celdas */
.grid-cell {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Redondear imágenes SOLO para este view */
.round-img .feature-card__image-container {
  border-radius: 50%;
  width: 180px;
  height: 180px;
}

.round-img .feature-card__image {
  border-radius: 50%;
  object-fit: cover;
}

/* Responsividad */
@media (max-width: 1024px) {
  .grid-layout {
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: minmax(200px, auto);
    padding: 2rem;
  }
}

@media (max-width: 640px) {
  .grid-layout {
    grid-template-columns: 1fr;
    grid-auto-rows: auto;
    gap: 1.5rem;
    padding: 1.5rem;
  }

  .grid-cell {
    justify-content: center;
  }
}
</style>
