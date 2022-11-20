<script setup lang="ts">
const searchBox = ref<HTMLElement | null>(null)

const focusOnSearchBox = () => {
  searchBox.value?.focus()
}
</script>

<template>
  <nav class="flex h-20 bg-black text-white items-center justify-center w-full">
    <NuxtLink to="/">
      <span>LOGO</span>
    </NuxtLink>
    <!-- <div class="col-start-1 col-end-2 pl-4">
      <NuxtLink to="/">
        <span>LOGO</span>
      </NuxtLink>
    </div> -->
    <!-- <div class="flex ml-auto pr-4">
      <div class="flex items-center relative">
        <input ref="searchBox" class="ml-auto border border-gray-200 h-10 w-28 focus-within:w-full px-5 rounded-lg focus-within:outline-none transition-all duration-500" placeholder="Search">
        <Icon name="fluent:search-16-regular" size="1.4rem" class="absolute right-0 text-gray-400 mr-4" @click="focusOnSearchBox" />
      </div>
    </div> -->
  </nav>
</template>