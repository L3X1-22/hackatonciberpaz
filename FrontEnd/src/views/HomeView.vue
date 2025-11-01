<template>
  <div class="home">
    <!-- Hero Section con imagen principal -->
    <section class="hero section-padding">
      <div class="container">
        <div class="hero__content">
          <h1 class="hero__title text-gradient fade-in">
            {{ heroData.title }}
          </h1>
          <p class="hero__description">
            {{ heroData.description }}
          </p>
        </div>
        
        <div class="hero__image">
          <img 
            :src="heroData.mainImage" 
            :alt="heroData.imageAlt"
            class="hero__img"
          />
        </div>
      </div>
    </section>

    <!-- Sección de Features Cards -->
    <section class="features section-padding">
      <div class="container">
        <h2 class="features__title text-center">
          {{ featuresData.sectionTitle }}
        </h2>
        
        <div class="features-grid">
          <FeatureCard
            v-for="feature in featuresData.cards"
            :key="feature.id"
            :image="feature.image"
            :alt-text="feature.altText"
            :title="feature.title"
            :description="feature.description"
            :to="feature.route"
            @click="handleFeatureClick(feature)"
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useStore } from 'vuex'
import FeatureCard from '@/components/ui/FeatureCard.vue'

export default {
  name: 'HomeView',
  components: {
    FeatureCard
  },
  setup() {
    const store = useStore()
    
    const heroData = computed(() => store.state.homePageData.hero || {})
    const featuresData = computed(() => store.state.homePageData.features || {})
    
    const handleFeatureClick = (feature) => {
      console.log('Feature clicked:', feature)
      // Aquí puedes agregar analytics o lógica adicional
    }
    
    onMounted(() => {
      store.dispatch('fetchHomePageData')
    })
    
    return {
      heroData,
      featuresData,
      handleFeatureClick
    }
  }
}
</script>

<style scoped>
.home {
  min-height: 100vh;
}

.hero {
  background: linear-gradient(135deg, var(--bg-primary), #2A1A55);
}

.hero .container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-12);
  align-items: center;
  min-height: 80vh;
}

.hero__title {
  font-size: var(--text-4xl);
  margin-bottom: var(--space-6);
  line-height: 1.2;
}

.hero__description {
  font-size: var(--text-xl);
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: var(--space-8);
  line-height: 1.6;
}

.hero__image {
  position: relative;
}

.hero__img {
  width: 100%;
  height: auto;
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-lg);
  transition: transform var(--transition-slow);
}

.hero__img:hover {
  transform: scale(1.02);
}

.features {
  background: rgba(255, 255, 255, 0.02);
}

.features__title {
  font-size: var(--text-3xl);
  margin-bottom: var(--space-12);
  background: linear-gradient(135deg, var(--blue-ai), var(--purple-accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-8);
  max-width: 1200px;
  margin: 0 auto;
}

/* Responsive */
@media (max-width: 768px) {
  .hero .container {
    grid-template-columns: 1fr;
    gap: var(--space-8);
    text-align: center;
  }
  
  .hero__title {
    font-size: var(--text-3xl);
  }
  
  .hero__description {
    font-size: var(--text-lg);
  }
  
  .features-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-6);
  }
  
  .features__title {
    font-size: var(--text-2xl);
  }
}
</style>