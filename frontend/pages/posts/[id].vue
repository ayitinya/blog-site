<script setup lang="ts">
const { data } = await useFetch(`/api/blogs/${useRoute().params.id}`, { key: `blog-${useRoute().params.id}` })
</script>

<template>
    <div class="h-full">
        <NuxtLayout name="custom">
            <template #left>
                <Icon name="fluent:share-16-filled" size="1.5rem" />
            </template>
            <template #default>
                <div v-if="data" class="p-10 bg-white rounded-t-lg border border-gray-400">
                    <h1>{{ data.title }}</h1>
                    <h2 class="text-slate-500 text-xl">{{ data.subtitle }}</h2>
                    <div id="readme" v-html="data.body" class=""></div>
                </div>
            </template>
            <template #right>
                fdadfad
            </template>
        </NuxtLayout>
    </div>

</template>
