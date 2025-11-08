<template>
  <div class="feature-card" :class="{ 'reverse': reverse }">
    <div class="feature-card__image-container">
      <img 
        :src="image" 
        :alt="altText" 
        class="feature-card__image"
        loading="lazy"
      />
    </div>

    <div class="feature-card__text">
      <h3 class="feature-card__title">{{ title }}</h3>
      <p v-if="description" class="feature-card__description">{{ description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeatureCard',
  props: {
    image: {
      type: String,
      required: true
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
    reverse: {
      type: Boolean,
      default: false // 🔹 true = texto a la derecha, imagen a la izquierda
    }
  }
}
</script>

<style scoped>
.feature-card {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
  border-radius: 1rem;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
}

.feature-card.reverse {
  flex-direction: row-reverse; /* 🔁 texto a la izquierda */
}

.feature-card__image-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.feature-card__image {
  width: 100%;
  max-width: 400px;
  border-radius: 1rem;
  object-fit: cover;
}

.feature-card__text {
  flex: 1;
  color: white;
  text-align: left;
}

.feature-card__title {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.feature-card__description {
  font-size: 1rem;
  line-height: 1.6;
  opacity: 0.9;
}

/* Hover suave */
.feature-card:hover {
  transform: translateY(-4px);
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.25);
}

/* Responsivo */
@media (max-width: 1024px) {
  .feature-card {
    flex-direction: column;
    text-align: center;
  }

  .feature-card.reverse {
    flex-direction: column; /* 🔹 En móvil siempre imagen arriba */
  }

  .feature-card__image {
    max-width: 80%;
  }

  .feature-card__text {
    text-align: center;
  }
}
</style>