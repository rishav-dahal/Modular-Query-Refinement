<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'

const query = ref('')
const response = ref('')

const textareaRef = ref<HTMLTextAreaElement | null>(null)
const resizeTextarea = () => {
    if (textareaRef.value) {
        textareaRef.value.style.height = 'auto'
        textareaRef.value.style.height = textareaRef.value.scrollHeight + 'px'
    }
}

watch(query, resizeTextarea)
onMounted(resizeTextarea)

function submitQuery() {
    
}
</script>
<template>
    <div class="flex flex-col gap-6 items-center justify-center min-h-screen text-center bg-gray-200">
        <div class="bg-gray-100 p-8 rounded-lg shadow-lg w-2xl flex flex-col gap-7 items-center">
            <h1 class="text-4xl font-semibold mb-4 text-gray-600">Enter your Query</h1>
            <textarea ref="textareaRef" v-model="query" placeholder="Type your query here..."
                class="p-2 border border-gray-300 text-stone-600 rounded-lg focus:outline-none focus:ring-2 w-2/3 focus:ring-gray-500 resize-none overflow-hidden"
                @keyup.enter="submitQuery" rows="2"></textarea>
            <button @click="submitQuery"
                class="mt-4 px-6 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500">Submit</button>
            <div v-if="response" class="mt-6 p-4 bg-white shadow-md rounded-lg w-1/2">
                <h2 class="text-xl font-semibold mb-2">Response:</h2>
                <p class="text-gray-700">{{ response }}</p>
            </div>
        </div>
    </div>
</template>