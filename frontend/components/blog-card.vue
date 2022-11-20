<script setup lang="ts">
import { Blog } from "~/composables/types";


const props = withDefaults(
  defineProps<{
    blog: Blog,
    displayAuthor?: boolean
  }>(), {
  displayAuthor: true
}
)

</script>

<template>
  <NuxtLink :to="`/posts/${props.blog.id}`">
    <div class="border h-96 lg:h-52 flex flex-col lg:flex-row">
      <div class="h-52 lg:w-52 lg:grow-0 lg:shrink-0 flex">
        <img :src="props.blog.image.length ? props.blog.image : `https://via.placeholder.com/200`" alt="Blog image"
          class="w-full lg:h-full object-cover">
      </div>
      <div class="p-5 overflow-y-auto lg:grow-0 flex flex-col h-full">

        <h1 class="text-xl font-bold line-clamp-2">{{ props.blog.title }}</h1>
        <p class="line-clamp-2 lg:line-clamp-3 lg:h-auto">
          {{ props.blog.summary }}
        </p>
        <div class="mt-auto font-thin text-gray-500 text-sm">
          <div>
            <span v-for="tag of props.blog.tags" class="text-sm font-thin bg-gray-100 px-2 rounded">
              {{ tag.name }}
            </span>
          </div>
          <ClientOnly v-if="props.displayAuthor">
            <NuxtLink :to="`/authors/${props.blog.author}`">
              <span>by {{ props.blog.first_name }} {{ props.blog.last_name }}</span>
            </NuxtLink>

            <template #fallback>
              <span class="">by {{ props.blog.first_name }} {{ props.blog.last_name }}</span>
            </template>
          </ClientOnly>
          <span class="mx-2" v-if="props.displayAuthor">•</span>
          <span class="">
            {{ useDateFormat(props.blog.created_at, 'MMM D', { locales: 'en-us' }).value }}
          </span>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>


<style scoped>

</style>