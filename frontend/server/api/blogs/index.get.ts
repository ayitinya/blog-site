import { baseURL } from "~~/server/utils/services"

export default defineEventHandler(async event => {
    return await $fetch(`${baseURL}/blogs/`)
})
