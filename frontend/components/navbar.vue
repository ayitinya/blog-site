<script setup lang="ts">
const mobileNavExpanded = ref(false)
</script>

<template>
  <header class="w-screen sticky top-0 bg-white/90 backdrop-blur-lg drop-shadow px-4">
    <nav class="container flex h-20 items-center justify-between mx-auto  z-50">
      <div class="">
        <NuxtLink to="/">
          <span>LOGO</span>
        </NuxtLink>
      </div>

      <ul class="lg:flex hidden items-center justify-center gap-4 h-16">
        <li
          class="flex items-center justify-center h-10 px-3 py-2 bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
          <Icon name="heroicons:home" class="w-6 h-6 text-gray-600" />
          <span class="ml-2">Home</span>
        </li>
        <li
          class="flex items-center justify-center h-10 px-3 py-2 bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
          <Icon name="heroicons:hashtag" class="w-6 h-6 text-gray-600" />
          <span class="ml-2">Tags</span>
        </li>
        <li
          class="flex items-center justify-center h-10 px-3 py-2 bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
          <Icon name="heroicons:bookmark" class="w-6 h-6 text-gray-600" />
          <span class="ml-2">Bookmarks</span>
        </li>
        <li
          class="flex items-center justify-center h-10 px-3 py-2 bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
          <Icon name="heroicons:bell" class="w-6 h-6 text-gray-600" />
          <span class="ml-2">Notifications</span>
        </li>
      </ul>

      <span @click="mobileNavExpanded = !mobileNavExpanded"
        class="flex lg:hidden items-center justify-center w-10 h-10 rounded-full bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
        <svg class="w-6 h-6 text-gray-600" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          viewBox="0 0 24 24" stroke="currentColor">
          <!-- x icon path -->
          <path v-if="mobileNavExpanded" d="M6 18L18 6M6 6l12 12"></path>
          <!-- hamburger icon path -->
          <path v-else d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </span>
      <div class="lg:flex hidden items-center ml-4 gap-4">
        <!-- search btn -->
        <div
          class="flex items-center justify-center w-10 h-10 rounded-full bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
          <Icon name="heroicons:magnifying-glass-solid" class="w-6 h-6 text-gray-600" />
        </div>
        <NuxtLink to="/new-post">
          <button
            class="flex items-center justify-center h-10 ml-4 px-3 py-2 bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <svg class="w-6 h-6 text-gray-600" fill="none" stroke-linecap="round" stroke-linejoin="round"
              stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
            Post
          </button>
        </NuxtLink>
        <div class="flex items-center gap-4">
          <div
            class="flex items-center justify-center w-10 h-10 rounded-full bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <Icon name="heroicons:user" class="w-6 h-6 text-gray-600" />
          </div>
          <div class="flex flex-col">
            <span class="text-gray-600">Username</span>
            <span class="text-gray-400 text-xs">Admin</span>
          </div>
        </div>
      </div>
    </nav>
    <!-- mobile nav -->
    <div class="lg:hidden bg-white/90 drop-shadow-sm backdrop-blur-lg w-screen absolute left-0 z-50 transition-all ease-in-out duration-500 py-4" :class="{ 'hidden': !mobileNavExpanded }">
      <div class="container mx-auto">
        <ul class="grid grid-cols-1 sm:grid-cols-2  gap-4 ">
          <li
            class="flex items-center justify-center h-10 px-3 py-2  hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <Icon name="heroicons:home" class="w-6 h-6 text-gray-600" />
            <span class="ml-2">Home</span>
          </li>
          <li
            class="flex items-center justify-center h-10 px-3 py-2  hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <Icon name="heroicons:hashtag" class="w-6 h-6 text-gray-600" />
            <span class="ml-2">Tags</span>
          </li>
          <li
            class="flex items-center justify-center h-10 px-3 py-2  hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <Icon name="heroicons:bookmark" class="w-6 h-6 text-gray-600" />
            <span class="ml-2">Bookmarks</span>
          </li>
          <li
            class="flex items-center justify-center h-10 px-3 py-2  hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <Icon name="heroicons:bell" class="w-6 h-6 text-gray-600" />
            <span class="ml-2">Notifications</span>
          </li>
          <li class="flex items-center justify-center h-10 px-3 py-2  hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <Icon name="heroicons:magnifying-glass-solid" class="w-6 h-6 text-gray-600" />
            <span class="ml-2">Search</span>
          </li>
          <li class="flex items-center justify-center h-10 px-3 py-2  hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50">
            <svg class="w-6 h-6 text-gray-600" fill="none" stroke-linecap="round" stroke-linejoin="round"
              stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
            </svg>
            <span class="ml-2">Post</span>
          </li>
        </ul>
      </div>
    </div>

  </header>
</template>