// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    modules: ['@nuxtjs/tailwindcss', 'nuxt-icon', '@vueuse/nuxt',],
    tailwindcss: {},
    runtimeConfig: {
        public: {
            apiURL: process.env.API_URL || 'http://localhost:8000/api',
        }
    }
})

