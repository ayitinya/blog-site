import {baseURL} from "~/server/utils/services";
import {Author, Blog} from "~/composables/types";
import parseBlog from "~/server/utils/parseBlog";


export default defineEventHandler(async ({context}) => {
    const blogs = async () => await $fetch<Blog[]>(`${baseURL}/users/${context.params.id}/blogs`);
    const user = async () => await $fetch<Author>(`${baseURL}/users/${context.params.id}`);
    return await Promise
        .all([blogs(), user()])
        .then(
            (values) => {
                return ({
                    "blogs": values[0].map(parseBlog),
                    "user": values[1]
                });
            }
        )
        .catch((error) => {
                console.error(error);
                return {
                    "blogs": [],
                    "user": {}
                };
            }
        );
})