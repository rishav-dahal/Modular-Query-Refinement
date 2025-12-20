export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  modules: ['@nuxtjs/tailwindcss'],
  vite: {
    server: {
      allowedHosts: ['web.risaav.tech']
    }
  },
  runtimeConfig: {
    public: {
      api: {
        baseURL: 'https://api.risaav.tech/',
        trailingSlash: true,
      },
      baseURL: 'https://api.risaav.tech',
    },
  },
});