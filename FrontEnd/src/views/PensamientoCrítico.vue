<template>
  <div class="pensamiento-critico">
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
  </div>
</template>

<script>
import FeatureCard from '@/components/ui/FeatureCard.vue'
import api from '@/services/api.js'

export default {
  name: 'PensamientoCriticoView',
  components: { FeatureCard },
  data() {
    return {
      contentBlocks: [],
      loading: true,
      error: null
    }
  },
  computed: {
    filteredBlocks() {
      return this.contentBlocks.filter(
        block => block.section === 'pensamiento-critico'
      )
    }
  },
  async mounted() {
    try {
      const response = await api.get('content-blocks/?section=pensamiento-critico')
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
.pensamiento-critico {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow-y: auto;
  padding-top: 6rem;
  background: linear-gradient(to bottom right, #0b0b0b, #141414);
}

.grid-layout {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  padding: 3rem;
  position: relative;
  z-index: 2;
}

.grid-cell {
  display: flex;
  justify-content: center;
  align-items: stretch; /* Cambiado para que las tarjetas se estiren */
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
  min-height: 350px; /* Altura mínima consistente */
  display: flex;
  flex-direction: column;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card-wrapper ::v-deep .feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
}

.feature-card-wrapper ::v-deep .feature-card__image-container {
  width: 100%;
  height: 180px;
  border-radius: 50%;
  margin: 0 auto;
  margin-top: 1.5rem;
  overflow: hidden;
  flex-shrink: 0; /* Evita que se reduzca */
}

.feature-card-wrapper ::v-deep .feature-card__image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
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

/* Responsivo */
@media (max-width: 1024px) {
  .grid-layout {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 2rem;
  }
  
  .feature-card-wrapper ::v-deep .feature-card {
    min-height: 320px;
  }
  
  .feature-card-wrapper ::v-deep .feature-card__image-container {
    height: 160px;
    width: 160px;
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
    min-height: 300px;
  }
  
  .feature-card-wrapper ::v-deep .feature-card__image-container {
    height: 140px;
    width: 140px;
  }
}
</style>