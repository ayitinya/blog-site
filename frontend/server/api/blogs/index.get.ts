import { Blog } from "~~/composables/types"
import parseBlog from "~/server/utils/parseBlog";

export default defineEventHandler(async event => {
    interface Query {
        count: string
        next: string | null
        previous: string | null
        results: Blog[]
    }

    const query = getQuery(event)
    const data = await $fetch<Query>(`${useRuntimeConfig().public.apiURL}/blogs/`, { query: query })

    data.results.forEach((blog: Blog, index: number) => data.results[index] = parseBlog(blog))

    return data
})
