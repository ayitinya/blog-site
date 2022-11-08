<script setup lang="ts">
import { useEditor, EditorContent, BubbleMenu, FloatingMenu } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import Link from '@tiptap/extension-link'
import Underline from '@tiptap/extension-underline'
import Image from '@tiptap/extension-image'
import Typography from '@tiptap/extension-typography'

const props = defineProps<{
  title: string,
  subtitle: string,
  body: string,
  summary: string,
}>()

const emit = defineEmits<{
  (event: 'update:title', val: string): void
  (event: 'update:subtitle', val: string): void
  (event: 'update:body', val: string): void
  (event: 'update:summary', val: string): void
}>()

const editor = useEditor({
  content: props.body,
  extensions: [
    StarterKit,
    Underline,
    Link,
    Image,
    Typography,
  ],
  onUpdate: ({ editor }) => {
    emit('update:body', JSON.stringify(editor.getJSON()))
  },
})

function addImage() {
  const url = window.prompt('URL')

  if (url) {
    editor.value!.chain().focus().setImage({ src: url }).run()
  }
}

function setLink() {
  const previousUrl = editor.value!.getAttributes('link').href
  const url = window.prompt('URL', previousUrl)

  // cancelled
  if (url === null) {
    return
  }

  // empty
  if (url === '') {
    editor.value!
      .chain()
      .focus()
      .extendMarkRange('link')
      .unsetLink()
      .run()

    return
  }

  // update link
  editor.value!
    .chain()
    .focus()
    .extendMarkRange('link')
    .setLink({ href: url })
    .run()
}
</script>

<template>
  <div class="mb-5 px-10 pt-10">
    <input class="focus-visible:outline-none text-5xl font-bold" type="text" placeholder="Post title"
      :value="props.title" @input="$emit('update:title', ($event.target as HTMLInputElement).value)" />
    <input class="focus-visible:outline-none text-4xl font-semibold" type="text" name="" id="" placeholder="Subtitle"
      :value="props.subtitle" @input="$emit('update:subtitle', ($event.target as HTMLInputElement).value)">
  </div>

  <div class="bg-[#F3F3F3] mb-5 px-10 py-2 flex items-center fixed-menu sticky top-0 z-50" v-if="editor">
    <button @click="editor!.chain().focus().toggleHeading({ level: 2 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }" class="mx-2">
      <Icon name="ri:h-2" size="1.5rem" />
    </button>
    <button @click="editor!.chain().focus().toggleHeading({ level: 3 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }" class="mx-2">
      <Icon name="ri:h-3" size="1.5rem" />
    </button>
    <button @click="editor!.chain().focus().toggleHeading({ level: 4 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 4 }) }" class="mx-2">
      <Icon name="ri:h-4" size="1.5rem" />
    </button>

    <button @click="editor!.chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }"
      class="mx-2">
      <Icon name="fluent:text-bold-16-filled" size="1.5rem" />
    </button>
    <button @click="editor!.chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }"
      class="mx-2">
      <Icon name="fluent:text-italic-16-filled" size="1.5rem" />
    </button>
    <button @click="editor!.chain().focus().toggleUnderline().run()"
      :class="{ 'is-active': editor.isActive('underline') }" class="mx-2">
      <Icon name="fluent:text-underline-16-regular" size="1.5rem" />
    </button>
    <button @click="editor!.chain().focus().toggleStrike().run()" :class="{ 'is-active': editor.isActive('strike') }"
      class="mx-2">
      <Icon name="fluent:text-strikethrough-16-regular" size="1.5rem" />
    </button>
    <button @click="setLink" :class="{ 'is-active': editor.isActive('link') }" class="mx-2">
      <Icon name="fluent:link-12-filled" size="1.5rem" />
    </button>
    <button @click="addImage" class="mx-2">
      <Icon name="fluent:image-16-regular" size="1.5rem" />
    </button>
    <button @click="editor!.chain().focus().toggleCodeBlock().run()"
      :class="{ 'is-active': editor.isActive('codeBlock') }">
      <Icon name="fluent:code-16-filled" size="1.5rem" />
    </button>

    <button @click="editor!.chain().focus().toggleBulletList().run()"
      :class="{ 'is-active': editor.isActive('bulletList') }" class="mx-2">
      <Icon name="fluent:text-bullet-list-tree-16-filled" size="1.5rem" />
    </button>
    <button @click="editor!.chain().focus().toggleOrderedList().run()"
      :class="{ 'is-active': editor.isActive('orderedList') }" class="mx-2">
      <Icon name="fluent:text-number-list-ltr-16-filled" size="1.5rem" />
    </button>
  </div>

  <div v-if="editor">
    <BubbleMenu class="bubble-menu" :tippy-options="{ duration: 100 }" :editor="editor">
      <button @click="editor!.chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }">
        Bold
      </button>
      <button @click="editor!.chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }">
        Italic
      </button>
      <button @click="editor!.chain().focus().toggleStrike().run()" :class="{ 'is-active': editor.isActive('strike') }">
        Strike
      </button>
    </BubbleMenu>

    <FloatingMenu class="floating-menu" :tippy-options="{ duration: 100 }" :editor="editor">
      <button @click="editor!.chain().focus().toggleHeading({ level: 2 }).run()"
        :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
        H2
      </button>
      <button @click="editor!.chain().focus().toggleHeading({ level: 3 }).run()"
        :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }">
        H3
      </button>
      <button @click="editor!.chain().focus().toggleHeading({ level: 4 }).run()"
        :class="{ 'is-active': editor.isActive('heading', { level: 4 }) }">
        H4
      </button>
      <button @click="editor!.chain().focus().toggleBulletList().run()"
        :class="{ 'is-active': editor.isActive('bulletList') }">
        Bullet List
      </button>
    </FloatingMenu>
  </div>

  <EditorContent :editor="editor" class="mb-5 px-10" />

</template>

<style lang="scss">
/* Basic editor styles */
.ProseMirror {
  >*+* {
    margin-top: 0.75em;
  }

  ul,
  ol {
    padding: 0 1rem;
  }

  blockquote {
    padding-left: 1rem;
    border-left: 2px solid rgba(#0D0D0D, 0.1);
  }


}

.ProseMirror:focus-visible {
  outline: none;
  border: none;
}

.fixed-menu {
  button {
    opacity: 0.4;

    &:hover,
    &.is-active {
      opacity: 1;
    }
  }

}

.bubble-menu {
  display: flex;
  background-color: #0D0D0D;
  padding: 0.2rem;
  border-radius: 0.5rem;

  button {
    border: none;
    background: none;
    color: #FFF;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0 0.2rem;
    opacity: 0.6;

    &:hover,
    &.is-active {
      opacity: 1;
    }
  }
}

.floating-menu {
  display: flex;
  background-color: #0D0D0D10;
  padding: 0.2rem;
  border-radius: 0.5rem;

  button {
    border: none;
    background: none;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0 0.2rem;
    opacity: 0.6;

    &:hover,
    &.is-active {
      opacity: 1;
    }
  }
}

code {
  background-color: #0D0D0D10;
  padding: 0.2rem;
  border-radius: 0.5rem;
}
</style>