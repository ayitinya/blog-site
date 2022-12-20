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
    <div class="border h-96 flex flex-col ">
      <div class="h-52  flex">
        <img :src="props.blog.image.length ? props.blog.image : `https://via.placeholder.com/200`" :alt="props.blog.title"
          class="w-full object-cover">
      </div>
      <div class="p-5 overflow-y-auto  flex flex-col h-full">
        <div>
            <span v-for="tag of props.blog.tags" class="text-sm font-thin">
              {{ tag.name }}
            </span>
          </div>
        <span class="text-xl font-bold line-clamp-2">{{ props.blog.title }}</span>
        <p class="line-clamp-2">
          {{ props.blog.summary }}
        </p>
        <div class="mt-auto font-thin text-gray-500 text-sm">
          
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