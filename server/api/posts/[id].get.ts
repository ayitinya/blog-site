import { storageBucket, parseMarkdown, Storage } from "~~/server/utils";

export default defineEventHandler(async _event => {
    const storage = new Storage()
    const data = await storage.bucket(storageBucket.name).file('README.md').download()
    
    return parseMarkdown(data.toString())
})