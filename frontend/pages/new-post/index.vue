<script setup lang="ts">
import { Blog } from '~~/composables/types';

const title = ref("");
const subtitle = ref("");
const body = ref("");
const summary = ref("");

const post = () => {
    useFetch<Blog>(`${useRuntimeConfig().public.apiURL}/blogs/`, {
        method: 'POST',
        key: body.value,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title.value,
            subtitle: subtitle.value,
            body: body.value,
            summary: summary.value,
            author: 1,
        })
    }).then((res) => {
        if (res.data.value)
            useRouter().replace(`/posts/${res.data.value.id}`)
    })
}
</script>

<template>
        <NuxtLayout name="custom">
            <div class="h-[calc(100vh_-_11rem)] overflow-y-auto overflow-x-hidden bg-white rounded-lg">
                <TextEditor v-model:body="body" v-model:title="title" v-model:subtitle="subtitle"
                    v-model:summary="summary" />
            </div>
            <div class="py-4 flex gap-4 prose md:prose-lg lg:prose-xl mx-auto">
                <button @click="" type="button" class="border border-gray-500 px-2 py-1 rounded" disabled>Save Draft</button>
                <button @click="" type="button" class="border border-gray-500 px-2 py-1 rounded" disabled>Preview</button>
                <button @click="post" type="button"
                    class="ml-auto border border-gray-500 px-2 py-1 rounded">Publish</button>
            </div>
        </NuxtLayout>
</template>