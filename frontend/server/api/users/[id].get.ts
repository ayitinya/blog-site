import { Author, Blog } from "~/composables/types";
import parseBlog from "~/server/utils/parseBlog";

interface Query {
    count: string
    next: boolean
    results: Blog[]
}

export default defineEventHandler(async (event): Promise<{
    blogs: Query,
    user: Author
}> => {
    const query = getQuery(event)

    const blogs = async () => await $fetch<Query>(`${useRuntimeConfig().public.apiURL}/users/${event.context.params.id}/blogs/`, { query: query });
    const user = async () => await $fetch<Author>(`${useRuntimeConfig().public.apiURL}/users/${event.context.params.id}/`);
    return await Promise
        .all([blogs(), user()])
        .then(
            (values) => {
                return ({
                    "blogs": {
                        "count": values[0].count,
                        "next": values[0].next,
                        "results": values[0].results.map((blog: Blog) => parseBlog(blog))
                    },
                    "user": values[1]
                });
            }

        )
})