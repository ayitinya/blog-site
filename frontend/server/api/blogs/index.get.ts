import { Blog } from "~~/composables/types"
import { baseURL } from "~~/server/utils/services"
import parseBlog from "~/server/utils/parseBlog";

export default defineEventHandler(async event => {
    interface Query {
        count: string
        next: string | null
        previous: string | null
        results: Blog[]
    }

    const query = getQuery(event)
    const data = await $fetch<Query>(`${baseURL}/blogs/`, { query: query })

    data.results.forEach((blog: Blog, index: number) => data.results[index] = parseBlog(blog))

    return data
})
