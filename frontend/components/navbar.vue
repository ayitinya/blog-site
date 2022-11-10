<template>
  <nav class="grid grid-cols-[minmax(auto,_20%)_minmax(min-content,_768px)_auto] h-14 bg-white items-center">
    <div class="col-start-1 col-end-2 pl-4">
      <NuxtLink to="/">
        <span>LOGO</span>
      </NuxtLink>
    </div>
    <div class="col-start-2 col-end-3">
      <input class="border border-gray-200 h-10 w-full px-5 rounded-lg focus-within:outline-none" placeholder="Search">
    </div>
    <div class="col-start-3 col-end-4 ml-auto pr-4">
      <button @click="$router.push('/new-post')"
        class="border border-red-500 font-semibold py-2 px-4 rounded mx-1 hover:bg-red-500 hover:text-white transition-all duration-500">
        New Post
      </button>
      <button class="mx-1">
        <Icon name="fluent:alert-28-regular" size="1.5rem" />
      </button>
      <button class="mx-1">
        <Icon name="fluent:person-16-regular" size="1.5rem" />
      </button>
    </div>
  </nav>
</template>