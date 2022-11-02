import { marked } from "marked";
import DOMPurify from 'dompurify';
import { JSDOM } from 'jsdom';


export default function parseMarkdown(markdown: string): string {
    const data = marked(markdown, {})
    const window = new JSDOM('').window;
    const purify = DOMPurify(window as unknown as Window);
    const clean = purify.sanitize(data);
    return clean
}
