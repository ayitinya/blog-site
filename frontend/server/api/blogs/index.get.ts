import {Blog} from "~~/composables/types"
import {baseURL} from "~~/server/utils/services"
import parseBlog from "~/server/utils/parseBlog";

export default defineEventHandler(async event => {
    const data = await $fetch<Blog[]>(`${baseURL}/blogs/`)

    data.forEach((blog: Blog, index: number) => data[index] = parseBlog(blog))

    return data
})
