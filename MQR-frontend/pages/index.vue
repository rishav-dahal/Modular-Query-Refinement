<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'

const query = ref('')
// const response = ref(' g97ftvhmr update /pages/index.vue, /assets/css/main.css, /assets/css/main.css?direct, /pages/index.vue?macro=true, /@id/virtual:nuxt:%2Fhome%2Fsandhya%2FDesktop%2FModular-Query-Refinement%2FMQR-frontend%2F.nuxt%2Froutes.mjs (x19)uoihb')
const response = ref("")
const textareaRef = ref<HTMLTextAreaElement | null>(null)
const isSubmitting = ref(false)

const resizeTextarea = () => {
    if (textareaRef.value) {
        textareaRef.value.style.height = 'auto'
        textareaRef.value.style.height = textareaRef.value.scrollHeight + 'px'
    }
}

watch(query, resizeTextarea)
onMounted(resizeTextarea)

function submitQuery() {
    if (!query.value.trim()) return

    isSubmitting.value = true
    setTimeout(() => {
        isSubmitting.value = false
    }, 1000)
}
</script>

<template>
    <div class="min-h-screen w-full bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
            <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-gray-600 rounded-full blur-3xl"></div>
            <div class="absolute bottom-1/4 right-1/4 w-80 h-80 bg-gray-500 rounded-full blur-3xl"></div>
        </div>

        <div class="relative z-10 min-h-screen flex flex-col">
            <header class="w-full px-4 sm:px-6 lg:px-8 pt-2 sm:pt-16">
                <div class="text-center">
                    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-2 sm:mb-4 tracking-tight">
                        Query<span
                            class="text-gradient bg-gradient-to-r from-gray-400 to-gray-300 bg-clip-text text-transparent">Processor</span>
                    </h1>
                    <p class="text-gray-300 text-lg sm:text-xl lg:text-2xl font-light max-w-2xl mx-auto">
                        Advanced query processing with intelligent responses
                    </p>
                </div>
            </header>

            <main class="flex-1 flex items-center justify-center px-4 sm:px-6 lg:px-8 py-8">
                <div class="w-full max-w-6xl">
                    <div
                        class="bg-white/5 backdrop-blur-xl rounded-3xl border border-white/10 shadow-2xl mb-8 overflow-hidden">
                        <div class="p-6 sm:p-8 lg:p-12">

                            <div class="relative mb-8">
                                <textarea ref="textareaRef" v-model="query"
                                    placeholder="Enter your query here..." class="w-full min-h-[120px] sm:min-h-[150px] p-6 sm:p-8 bg-gray-800/50 backdrop-blur-sm border-2 border-gray-600/30 
                                           rounded-2xl text-white text-lg sm:text-xl leading-relaxed placeholder-gray-400
                                           focus:outline-none focus:border-gray-500 focus:ring-4 focus:ring-gray-500/20 
                                           resize-none transition-all duration-300 hover:border-gray-500/50"
                                    @keyup.enter="submitQuery" rows="4"></textarea>

                                <!-- Character Counter -->
                                <div class="absolute bottom-4 right-6 flex items-center gap-3">
                                    <span class="text-gray-400 text-sm font-medium">{{ query.length }} chars</span>
                                    <div class="w-2 h-2 bg-gray-500 rounded-full animate-pulse"></div>
                                </div>
                            </div>

                            <!-- Submit Button -->
                            <div class="flex justify-center">
                                <button @click="submitQuery" :disabled="!query.trim() || isSubmitting" class="group relative px-8 sm:px-12 py-4 sm:py-5 bg-gradient-to-r from-gray-600 to-gray-700 
                                           text-white text-lg sm:text-xl font-bold rounded-2xl shadow-2xl 
                                           hover:shadow-gray-500/25 transform transition-all duration-300 
                                           hover:scale-105 hover:from-gray-500 hover:to-gray-600 
                                           focus:outline-none focus:ring-4 focus:ring-gray-500/30 
                                           disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none
                                           min-w-[200px] sm:min-w-[250px]">
                                    <span v-if="!isSubmitting" class="flex items-center justify-center gap-3">
                                        <svg class="w-5 h-5 sm:w-6 sm:h-6 group-hover:translate-x-1 transition-transform duration-300"
                                            fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
                                        </svg>
                                        Submit Query
                                    </span>
                                    <span v-else class="flex items-center justify-center gap-3">
                                        <svg class="animate-spin w-5 h-5 sm:w-6 sm:h-6" fill="none"
                                            stroke="currentColor" viewBox="0 0 24 24">
                                            <circle cx="12" cy="12" r="10" stroke-width="2" stroke-dasharray="31.416"
                                                stroke-dashoffset="31.416">
                                                <animate attributeName="stroke-dasharray" dur="2s"
                                                    values="0 31.416;15.708 15.708;0 31.416" repeatCount="indefinite" />
                                                <animate attributeName="stroke-dashoffset" dur="2s"
                                                    values="0;-15.708;-31.416" repeatCount="indefinite" />
                                            </circle>
                                        </svg>
                                        Processing...
                                    </span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div v-if="response" class="animate-slide-up">
                        <div
                            class="bg-white/5 backdrop-blur-xl rounded-3xl border border-white/10 shadow-2xl overflow-hidden">
                            <div
                                class="bg-gradient-to-r from-gray-700/50 to-gray-600/50 px-6 sm:px-8 py-4 sm:py-6 border-b border-white/10">
                                <div class="flex items-center gap-4">
                                    <div class="flex gap-2">
                                        <div class="w-3 h-3 bg-gray-400 rounded-full animate-pulse"></div>
                                        <div class="w-3 h-3 bg-gray-500 rounded-full animate-pulse"
                                            style="animation-delay: 0.2s"></div>
                                        <div class="w-3 h-3 bg-gray-600 rounded-full animate-pulse"
                                            style="animation-delay: 0.4s"></div>
                                    </div>
                                    <h2 class="text-xl sm:text-2xl font-bold text-white flex-1">Response Generated</h2>
                                </div>
                            </div>

                            <div class="p-6 sm:p-8 lg:p-12">
                                <div
                                    class="bg-gray-800/30 backdrop-blur-sm rounded-2xl border border-gray-600/20 overflow-hidden">
                                    <div class="p-6 sm:p-8">
                                        <pre
                                            class="text-gray-200 leading-relaxed text-sm sm:text-base font-mono whitespace-pre-wrap break-words">{{ response }}</pre>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>

<style scoped>
@keyframes slide-up {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-slide-up {
    animation: slide-up 0.6s ease-out;
}

.text-gradient {
    background: linear-gradient(135deg, #9CA3AF, #D1D5DB);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

textarea::-webkit-scrollbar {
    width: 8px;
}

textarea::-webkit-scrollbar-track {
    background: rgba(75, 85, 99, 0.3);
    border-radius: 4px;
}

textarea::-webkit-scrollbar-thumb {
    background: rgba(156, 163, 175, 0.5);
    border-radius: 4px;
    transition: background 0.3s ease;
}

textarea::-webkit-scrollbar-thumb:hover {
    background: rgba(156, 163, 175, 0.7);
}

/* Responsive adjustments */
@media (max-width: 640px) {
    .min-h-[120px] {
        min-height: 100px;
    }
}

@media (max-width: 480px) {
    .rounded-3xl {
        border-radius: 1.5rem;
    }

    .rounded-2xl {
        border-radius: 1rem;
    }
}
</style>