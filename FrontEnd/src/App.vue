<template>
  <nav class="navbar">
    <div class="navbar__logo">
      <img src="https://placekitten.com/50/50" alt="Logo gatito" />
    </div>

    <div class="navbar__links">
      <router-link to="/">Inicio</router-link>
      <router-link to="/que-es-ia">Entiende la IA</router-link>
      <router-link to="/como-funciona-un-llm">Explora un LLM</router-link>
      <router-link to="/entorno-academico">Aplícalo al estudio</router-link>
      <router-link to="/pensamiento-critico">Piensa por ti</router-link>
    </div>

  </nav>

  <router-view />
</template>

<script>
export default {
  name: "App",
};
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;

  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 1rem 2rem;
  background: rgba(10, 10, 20, 0.85);
  backdrop-filter: blur(10px);

  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

/* Logo */
.navbar__logo img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  transition: transform 0.3s ease;
}

.navbar__logo img:hover {
  transform: scale(1.1) rotate(-6deg);
}

/* Contenedor de links */
.navbar__links {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  gap: 2rem;
  margin-left: auto;
}

/* Links */
.navbar__links a {
  color: var(--text-primary, #fff);
  text-decoration: none;
  font-weight: 500;
  position: relative;
  transition: color 0.3s ease;
  font-family: var(--font-family-heading, 'Poppins', sans-serif);
}

/* Subrayado animado */
.navbar__links a::after {
  content: "";
  position: absolute;
  bottom: -4px;
  left: 50%;
  width: 0;
  height: 2px;
  background: var(--purple-accent, #9b51e0);
  transition: width 0.3s ease, left 0.3s ease;
}

.navbar__links a:hover {
  color: var(--purple-accent, #9b51e0);
}

.navbar__links a:hover::after {
  width: 100%;
  left: 0;
}

/* Efecto de click */
.navbar__links a:active {
  transform: scale(0.96);
  color: var(--pink-support, #ff6bcb);
}

/* Responsive */
@media (max-width: 768px) {
  .navbar {
    padding: 0.75rem 1rem;
  }

  .navbar__logo img {
    width: 34px;
    height: 34px;
  }

  .navbar__links {
    gap: 1rem;
  }
}
</style>
