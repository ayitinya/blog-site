<script setup lang="ts">
import { Blog } from '~~/composables/types';

const { data } = await useFetch<Blog[]>('/api/blogs/')
</script>

<template>
    <div class="h-full">
        <NuxtLayout name="custom">
            <template #left>
            </template>
            <template #default>
                <div class="p-8 bg-white rounded-lg border border-gray-200">

                    <div class="py-4" v-for="post of data">
                        <div class="flex">
                            <span class="">
                                <Icon name="fluent:person-12-filled" size="2.5rem" />
                            </span>
                            <div class="flex flex-col">
                                <span>{{ post.first_name }} {{ post.last_name }}</span>
                                <span class="font-thin text-gray-500 text-sm">
                                    {{ useDateFormat(post.created_at, 'MMM D', { locales: 'en-us' }).value }}
                                </span>
                            </div>
                        </div>
                        <NuxtLink :to="`/posts/${post.id}`">
                            <div class="pl-10 mt-3">
                                <h2>{{ post.title }}</h2>
                            </div>
                        </NuxtLink>
                        <div class="pl-10 mt-5">
                            <span class="text-sm font-thin bg-gray-200 px-1 rounded mr-2">#Read more</span>
                            <span class="text-sm font-thin bg-gray-200 px-1 rounded mr-2">#Read more</span>
                            <span class="text-sm font-thin bg-gray-200 px-1 rounded mr-2">#Read more</span>
                        </div>
                        <div class="pl-10 mt-3 flex text-gray-600 text-sm">
                            <div class="flex font-thin ">
                                <button type="button"
                                    class="mr-3 p-1 rounded hover:text-zinc-900 hover:bg-gray-200 transition-all">
                                    <Icon name="fluent:like-16-regular" size="1.25rem" /> 2 Reactions
                                </button>
                                <button type="button"
                                    class="mr-3 p-1 rounded hover:text-zinc-900 hover:bg-gray-200 transition-all">
                                    <Icon name="fluent:comment-multiple-16-regular" size="1.25rem" /> 5 Comments
                                </button>
                            </div>
                            <div class="ml-auto">
                                <button type="button"
                                    class="p-1 rounded hover:text-zinc-900 hover:bg-gray-200 transition-all">
                                    <Icon name="fluent:bookmark-16-regular" size="1.25rem" />
                                </button>
                            </div>
                        </div>

                    </div>
                </div>

            </template>
            <template #right>
            </template>
        </NuxtLayout>
    </div>

</template>
