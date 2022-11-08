import { baseURL } from "~~/server/utils/services"
import { JSDOM } from 'jsdom'
import DOMPurify from 'dompurify'
import { Blog } from "~~/composables/types"
import parseJSONToHTML from "~~/server/utils/parseJSONToHTML"

export default defineEventHandler(async event => {
    const query = event.context.params.id
    const res = await $fetch<Blog>(`${baseURL}/blogs/${query}`)
    const body = res.body
    const parsedJSON = parseJSONToHTML(body)

    const window = new JSDOM('').window;
    const purify = DOMPurify(window as unknown as Window);
    const cleanedHTML = purify.sanitize(parsedJSON);

    res.body = cleanedHTML

    return res
})
