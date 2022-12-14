import { JSDOM } from 'jsdom'
import DOMPurify from 'dompurify'
import { Blog } from "~~/composables/types"
import parseJSONToHTML from "~~/server/utils/parseJSONToHTML"

export default defineEventHandler(async event => {
    const query = event.context.params.id
    const res = await $fetch<Blog>(`${useRuntimeConfig().public.apiURL}/blogs/${query}/`)
    const body = res.body
    const parsedJSON = parseJSONToHTML(body)

    const window = new JSDOM('').window;
    const purify = DOMPurify(window as unknown as Window);
    res.body = purify.sanitize(parsedJSON);

    return res
})
