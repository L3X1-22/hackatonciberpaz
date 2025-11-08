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
          class="round-img"
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
  grid-auto-rows: minmax(250px, auto);
  gap: 2rem;
  padding: 3rem;
  position: relative;
  z-index: 2;
}

.grid-cell {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Imágenes redondeadas solo aquí */
.round-img .feature-card__image-container {
  border-radius: 50%;
  width: 180px;
  height: 180px;
}

.round-img .feature-card__image {
  border-radius: 50%;
  object-fit: cover;
}

/* Responsivo */
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
    gap: 1.5rem;
    padding: 1.5rem;
  }

  .grid-cell {
    justify-content: center;
  }
}
</style>
