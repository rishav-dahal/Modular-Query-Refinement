export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  modules: ['@nuxtjs/tailwindcss'],
  runtimeConfig: {
    public: {
      api: {
        baseURL: 'http://127.0.0.1:8000/',
        trailingSlash: true,
      },
      baseURL: 'http://127.0.0.1:8000',
    },
  },
});