import { generateHTML } from '@tiptap/html'
import { Link } from '@tiptap/extension-link'
import { Underline } from '@tiptap/extension-underline'
import { StarterKit } from '@tiptap/starter-kit'
import { Image } from '@tiptap/extension-image'
import { Typography } from '@tiptap/extension-typography'

export default function parseJSONToHTML(json: string) {
  return generateHTML(JSON.parse(json), [StarterKit, Link, Underline, Image, Typography])
}