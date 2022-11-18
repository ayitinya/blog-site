<script setup lang="ts">
import {Blog} from "~/composables/types";


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
    <div class="border h-72">
      <div class="h-48">
        <img :src="props.blog.image.length ? props.blog.image : `https://via.placeholder.com/200`" alt="Blog image"
             class="w-full h-full object-cover">
      </div>
      <div class="p-5 overflow-y-auto">
        <h1 class="text-xl font-bold line-clamp-2">{{ props.blog.title }}</h1>
        <div class="font-thin text-gray-500 text-sm">
          <span class="" v-if="props.displayAuthor">by {{ props.blog.first_name }} {{ props.blog.last_name }}</span>
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