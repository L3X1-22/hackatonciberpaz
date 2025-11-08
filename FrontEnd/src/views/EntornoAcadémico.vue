<template>
  <div class="entorno-academico">
    <div class="background__overlay"></div>

    <div class="grid-layout" v-if="!loading && !error">
      <div
        v-for="(item, index) in filteredBlocks"
        :key="item.id"
        class="grid-cell"
      >
        <FeatureCard
          class="feature-card-wrapper"
          :title="item.title"
          :description="item.description"
          :image="item.image_url"
          :alt-text="item.image_alt"
        />
      </div>
    </div>

    <div v-else-if="loading" class="loading">Cargando contenido...</div>
    <div v-else-if="error" class="error">Error: {{ error }}</div>
  </div>
</template>

<script>
import FeatureCard from '@/components/ui/FeatureCard.vue'
import api from '@/services/api.js'

export default {
  name: 'EntornoAcademicoView',
  components: { FeatureCard },
  data() {
    return {
      contentBlocks: [],
      loading: true,
      error: null
    }
  },
  computed: {
    // 🔹 Solo los bloques de esta sección
    filteredBlocks() {
      return this.contentBlocks.filter(
        block => block.section === 'entorno-academico'
      )
    }
  },
  async mounted() {
    try {
      const response = await api.get('content-blocks/?section=entorno-academico')
      this.contentBlocks = response.data
    } catch (err) {
      this.error = err.message || 'Error al cargar el contenido'
    } finally {
      this.loading = false
    }
  }
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
  gap: 2rem;
  padding: 3rem;
  z-index: 2;
}

/* Centrado de celdas */
.grid-cell {
  display: flex;
  justify-content: center;
  align-items: stretch; /* Cambiado para estirar las tarjetas */
}

.feature-card-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
}

/* Estilos para garantizar tamaño consistente */
.feature-card-wrapper ::v-deep .feature-card {
  width: 100%;
  height: 100%;
  min-height: 380px; /* Altura mínima consistente */
  display: flex;
  flex-direction: column;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: rgba(30, 30, 30, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.feature-card-wrapper ::v-deep .feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
  border-color: rgba(255, 255, 255, 0.2);
}

/* Imágenes redondeadas SOLO para este view */
.feature-card-wrapper ::v-deep .feature-card__image-container {
  border-radius: 50%;
  width: 180px;
  height: 180px;
  margin: 0 auto;
  margin-top: 1.5rem;
  overflow: hidden;
  flex-shrink: 0; /* Evita que se reduzca */
  border: 3px solid rgba(255, 255, 255, 0.1);
}

.feature-card-wrapper ::v-deep .feature-card__image {
  border-radius: 50%;
  object-fit: cover;
  width: 100%;
  height: 100%;
  transition: transform 0.3s ease;
}

.feature-card-wrapper ::v-deep .feature-card:hover .feature-card__image {
  transform: scale(1.05);
}

.feature-card-wrapper ::v-deep .feature-card__content {
  flex: 1;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.feature-card-wrapper ::v-deep .feature-card__title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: #ffffff;
  text-align: center;
}

.feature-card-wrapper ::v-deep .feature-card__description {
  font-size: 0.95rem;
  line-height: 1.5;
  color: #cccccc;
  text-align: center;
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Estados */
.loading,
.error {
  text-align: center;
  margin-top: var(--space-12);
  font-size: var(--text-lg);
  color: var(--text-primary);
  opacity: 0.8;
}

.error {
  color: var(--pink-support);
}

/* Responsividad */
@media (max-width: 1024px) {
  .grid-layout {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 2rem;
  }
  
  .feature-card-wrapper ::v-deep .feature-card {
    min-height: 360px;
  }
  
  .feature-card-wrapper ::v-deep .feature-card__image-container {
    width: 160px;
    height: 160px;
  }
}

@media (max-width: 640px) {
  .grid-layout {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 1.5rem;
    max-width: 400px;
    margin: 0 auto;
  }
  
  .feature-card-wrapper ::v-deep .feature-card {
    min-height: 340px;
  }
  
  .feature-card-wrapper ::v-deep .feature-card__image-container {
    width: 140px;
    height: 140px;
  }
  
  .grid-cell {
    justify-content: center;
  }
}
</style>