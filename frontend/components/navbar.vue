<script setup lang="ts">
const searchBox = ref<HTMLElement | null>(null)

const focusOnSearchBox = () => {
  searchBox.value?.focus()
}
</script>

<template>
  <nav class="flex h-20 bg-black text-white items-center">
    <div class="col-start-1 col-end-2 pl-4">
      <NuxtLink to="/">
        <span>LOGO</span>
      </NuxtLink>
    </div>
    <div class="flex ml-auto pr-4">
      <div class="flex items-center relative">
        <input ref="searchBox" class="ml-auto border border-gray-200 h-10 w-28 focus-within:w-full px-5 rounded-lg focus-within:outline-none transition-all duration-500" placeholder="Search">
        <Icon name="fluent:search-16-regular" size="1.4rem" class="absolute right-0 text-gray-400 mr-4" @click="focusOnSearchBox" />
      </div>
      <!-- <button @click="$router.push('/new-post')"
        class="border border-red-500 font-semibold py-2 px-4 rounded mx-1 hover:bg-red-500 hover:text-white transition-all duration-500">
        New Post
      </button>
      <button class="mx-1">
        <Icon name="fluent:alert-28-regular" size="1.5rem" />
      </button>
      <button class="mx-1">
        <Icon name="fluent:person-16-regular" size="1.5rem" />
      </button> -->
    </div>
  </nav>
</template>