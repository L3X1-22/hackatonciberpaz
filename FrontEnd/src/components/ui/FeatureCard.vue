<template>
  <div 
    class="feature-card"
    :class="{ 'feature-card--clickable': clickable }"
    @click="handleClick"
  >
    <div class="feature-card__image-container">
      <img 
        :src="image" 
        :alt="altText"
        class="feature-card__image"
        loading="lazy"
      />
      <div class="feature-card__overlay"></div>
    </div>
    
    <h3 class="feature-card__title">
      {{ title }}
    </h3>
    
    <p v-if="description" class="feature-card__description">
      {{ description }}
    </p>
    
    <!-- Efecto de glow al hover -->
    <div class="feature-card__glow"></div>
  </div>
</template>

<script>
export default {
  name: 'FeatureCard',
  props: {
    image: {
      type: String,
      required: true,
      default: 'https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg'
    },
    altText: {
      type: String,
      default: 'Imagen descriptiva'
    },
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      default: ''
    },
    clickable: {
      type: Boolean,
      default: true
    },
    to: {
      type: [String, Object],
      default: ''
    }
  },
  emits: ['click'],
  methods: {
    handleClick() {
      if (this.clickable) {
        this.$emit('click')
        
        // Navegación si se proporciona 'to'
        if (this.to && this.$router) {
          if (typeof this.to === 'string') {
            this.$router.push(this.to)
          } else {
            this.$router.push(this.to)
          }
        }
      }
    }
  }
}
</script>

<style scoped>
.feature-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: var(--space-6);
  border-radius: var(--border-radius-lg);
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all var(--transition-normal);
  overflow: hidden;
}

.feature-card--clickable {
  cursor: pointer;
}

.feature-card--clickable:hover {
  transform: translateY(-8px);
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--purple-accent);
  box-shadow: var(--shadow-lg);
}

.feature-card__image-container {
  position: relative;
  width: 120px;
  height: 120px;
  margin-bottom: var(--space-6);
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid transparent;
  background: linear-gradient(135deg, var(--blue-ai), var(--purple-accent));
  padding: 3px;
  transition: all var(--transition-normal);
}

.feature-card--clickable:hover .feature-card__image-container {
  transform: scale(1.05);
  border-color: var(--yellow-contrast);
}

.feature-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  transition: transform var(--transition-slow);
}

.feature-card--clickable:hover .feature-card__image {
  transform: scale(1.1);
}

.feature-card__overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    135deg,
    transparent 0%,
    rgba(155, 81, 224, 0.2) 100%
  );
  border-radius: 50%;
  opacity: 0;
  transition: opacity var(--transition-normal);
}

.feature-card--clickable:hover .feature-card__overlay {
  opacity: 1;
}

.feature-card__title {
  font-family: var(--font-family-heading);
  font-size: var(--text-xl);
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--space-3);
  background: linear-gradient(135deg, var(--text-primary), var(--blue-ai));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.feature-card--clickable:hover .feature-card__title {
  background: linear-gradient(135deg, var(--yellow-contrast), var(--pink-support));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.feature-card__description {
  font-size: var(--text-sm);
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.5;
  max-width: 280px;
}

.feature-card__glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: var(--border-radius-lg);
  background: linear-gradient(135deg, var(--blue-ai), transparent, var(--purple-accent));
  opacity: 0;
  transition: opacity var(--transition-normal);
  z-index: -1;
}

.feature-card--clickable:hover .feature-card__glow {
  opacity: 0.1;
}

/* Responsive */
@media (max-width: 768px) {
  .feature-card {
    padding: var(--space-4);
  }
  
  .feature-card__image-container {
    width: 100px;
    height: 100px;
    margin-bottom: var(--space-4);
  }
  
  .feature-card__title {
    font-size: var(--text-lg);
  }
}
</style>