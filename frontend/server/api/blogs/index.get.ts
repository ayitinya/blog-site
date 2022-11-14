import { Blog } from "~~/composables/types"
import { baseURL } from "~~/server/utils/services"

export default defineEventHandler(async event => {
    const data = await $fetch<Blog[]>(`${baseURL}/blogs/`)

    data.forEach((blog, index) => {
        const body = JSON.parse(blog.body).content
        const summary = () => {
            for (let index = 0; index < body.length; index++) {
                const element = body[index];
                if (element.type === "paragraph") {
                    blog.summary = element.content[0].text
                    break
                }

            }
        }

        const image = () => {
            for (let index = 0; index < body.length; index++) {
                const element = body[index];
                if (element.type === "image") {
                    blog.image = element.attrs.src
                    break
                }
                else
                    blog.image = ""
            }
        }

        summary()
        image()
    })
    return data
})
