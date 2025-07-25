import { defineNuxtPlugin } from '#app'
import Toast, { POSITION } from 'vue-toastification'
import 'vue-toastification/dist/index.css'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(Toast, {
    position: POSITION.TOP_RIGHT,
    timeout: 3000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: false,
    closeButton: "button",
    icon: true,
    rtl: false,
    toastDefaults: {
      success: {
        timeout: 3000,
        hideProgressBar: false,
      },
      error: {
        timeout: 5000,
        hideProgressBar: false,
      },
      info: {
        timeout: 3000,
        hideProgressBar: false,
      },
      warning: {
        timeout: 4000,
        hideProgressBar: false,
      }
    }
  })
})
