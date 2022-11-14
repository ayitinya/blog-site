<script setup lang="ts">
import { Blog } from '~~/composables/types';

const { data } = await useFetch<Blog[]>('/api/blogs/')
</script>

<template>
    <div class="h-full">
        <NuxtLayout>
            <template #default>
                <div class="p-8">
                    <div class="py-4" v-for="post of data">
                        <div class="flex md:flex-row flex-col">
                            <div v-if="post.image?.length" class="md:pr-4">
                                <NuxtLink :to="`/posts/${post.id}`">
                                    <img :src="post.image" class="md:w-32 md:h-32" />
                                </NuxtLink>
                            </div>
                            <div class="">
                                <NuxtLink :to="`/posts/${post.id}`">
                                    <h1 class="text-2xl font-bold">{{ post.title }}</h1>
                                    <h2 class="text-xl font-light">{{ post.subtitle }}</h2>
                                </NuxtLink>
                                <div class="font-thin text-gray-500 text-sm">
                                    <span class="">by {{ post.first_name }} {{ post.last_name }}</span>
                                    <span class="mx-2">•</span>
                                    <span class="">
                                        {{ useDateFormat(post.created_at, 'MMM D', { locales: 'en-us' }).value }}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </NuxtLayout>
    </div>
</template>
