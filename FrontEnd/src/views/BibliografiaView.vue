<template>
  <div class="bibliografia-view">
    <h1>Bibliografía</h1>

    <div v-if="loading" class="loading">Cargando bibliografía...</div>
    <div v-else-if="error" class="error">
      Error al cargar los datos: {{ error }}
    </div>

    <div v-else class="bibliografia-grid">
      <a
        v-for="item in bibliografia"
        :key="item.id"
        class="bibliografia-card"
        :href="item.source_url"
        target="_blank"
        rel="noopener noreferrer"
      >
        <p class="campo"><strong>Título:</strong> {{ item.title }}</p>
        <p class="campo"><strong>Autor:</strong> {{ item.author }}</p>
        <p class="campo"><strong>Referencia:</strong> {{ item.reference_text }}</p>
        <p class="campo"><strong>Año:</strong> {{ item.year }}</p>
      </a>
    </div>
  </div>
</template>

<script>
import api from '@/services/api.js'

export default {
  name: 'BibliografiaView',
  data() {
    return {
      bibliografia: [],
      loading: true,
      error: null
    }
  },
  async mounted() {
    try {
      const response = await api.get('bibliography/')
      this.bibliografia = Array.isArray(response.data)
        ? response.data
        : [response.data]
    } catch (err) {
      this.error = err.message || 'Error desconocido'
    } finally {
      this.loading = false
    }
  }
}
</script>

<style scoped>
.bibliografia-view {
  padding-top: 120px;
  padding-bottom: var(--space-8);
  background: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
  animation: fadeIn 0.6s ease-out;
}

h1 {
  text-align: center;
  margin-bottom: var(--space-10);
  background: linear-gradient(135deg, var(--blue-ai), var(--purple-accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: var(--text-4xl);
}

.loading,
.error {
  text-align: center;
  font-size: var(--text-lg);
  color: var(--text-primary);
  opacity: 0.8;
}

.error {
  color: var(--pink-support);
}

.bibliografia-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-6);
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 var(--space-6);
}

/* --- TARJETA --- */
.bibliografia-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: var(--bg-primary-light);
  border: 1px solid var(--purple-accent-light);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  padding: var(--space-6);
  text-decoration: none;
  color: inherit;
  transition: transform var(--transition-normal),
              box-shadow var(--transition-normal),
              border-color var(--transition-fast);
  min-height: 220px; /* mantiene altura uniforme */
}

.bibliografia-card:hover {
  transform: translateY(-4px);
  border-color: var(--purple-accent);
  box-shadow: 0 0 10px var(--purple-accent-light);
}

.campo {
  margin-bottom: var(--space-3);
  font-size: var(--text-sm);
  line-height: 1.5;
  color: var(--text-primary);
}

.campo strong {
  color: var(--purple-accent);
  font-weight: 600;
}
</style>
