<script setup lang="ts">
const { data } = await useFetch(`/api/blogs/${useRoute().params.id}`, { key: `blog-${useRoute().params.id}` })
</script>

<template>
    <div class="h-full">
        <NuxtLayout name="custom">
            <template #left>
            </template>
            <template #default>
                <div v-if="data" class="p-10 bg-white rounded-lg border">
                    <h1>{{ data.title }}</h1>
                    <h2 class="text-slate-500 text-xl">{{ data.subtitle }}</h2>
                    <div id="readme" v-html="data.body" class=""></div>
                </div>
            </template>
            <template #right>
            </template>
        </NuxtLayout>
    </div>

</template>
