import {Blog} from "~/composables/types";

export default function (blog: Blog) {

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
            } else
                blog.image = ""
        }
    }

    summary()
    image()

    return blog
}