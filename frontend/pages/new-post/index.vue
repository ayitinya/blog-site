<script setup lang="ts">
import { baseURL } from '~~/server/utils/services';


const title = ref("");
const subtitle = ref("");
const body = ref("");
const summary = ref("");

const post = () => {
    useFetch(`${baseURL}/blogs/`, {
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
        console.log(res)
    })
}
</script>

<template>
    <div>
        <NuxtLayout name="custom">
            <div class="h-[calc(100vh_-_10rem)] overflow-y-auto bg-white rounded-lg border border-gray-400">
                <TextEditor v-model:body="body" v-model:title="title" v-model:subtitle="subtitle"
                    v-model:summary="summary" />
            </div>
            <div class="py-4 flex">
                <button @click="" type="button" class="border border-gray-500 px-2 py-1 rounded">Save Draft</button>
                <button @click="" type="button" class="border border-gray-500 px-2 py-1 ml-2 rounded">Preview</button>
                <button @click="post" type="button"
                    class="ml-auto border border-gray-500 px-2 py-1 rounded">Publish</button>
            </div>
        </NuxtLayout>
    </div>
</template>