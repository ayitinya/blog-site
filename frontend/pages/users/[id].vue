<script setup lang="ts">
const {data: {value: {blogs, user}}} = await useFetch(
  `/api/users/${useRoute().params.id}`,
  {key: `user-${useRoute().params.id}-blogs`}
)
</script>

<template>
  <div class="h-full">
    <NuxtLayout>
      <div class="p-5 md:p-10">
        <div class="flex flex-col items-center md:items-start md:flex-row">
          <div class="flex flex-col w-full h-full flex justify-center">
            <img src="https://via.placeholder.com/200" alt="User profile image">
            <div class="mt-2">
              <span class="font-bold">Contact</span>
              <div class="flex">
                <Icon name="mdi:twitter" class="mr-2" size="1.5rem"/>
                <Icon name="mdi:linkedin" class="mr-2" size="1.5rem"/>
                <Icon name="ic:round-email" class="mr-2" size="1.5rem"/>
              </div>
            </div>

          </div>
          <div class="md:pl-5 prose max-w-none">
            <h1 class="text-2xl font-bold">{{ user.first_name }} {{ user.last_name }}</h1>
            <p class="">
              Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nam ullam deleniti cumque
              consequatur non beatae, amet expedita doloremque iste omnis aspernatur voluptates vel
              sapiente labore iure architecto tenetur autem velit molestias! Omnis quasi sed facere.
              Necessitatibus deserunt sapiente, voluptates sunt pariatur fugiat quos nulla, officia
              cupiditate ipsa iste eos optio.
            </p>
          </div>
        </div>
        <div class="flex items-center pt-10">
          <h1 class="text-xl min-w-fit pr-4">Articles by {{ user.first_name }} {{ user.last_name }}</h1>
          <hr class="w-full">
        </div>
        <div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            <div v-for="blog in blogs" :key="blog.id">
              <BlogCard :blog="blog" :display-author="false"/>
            </div>
          </div>
        </div>
      </div>
    </NuxtLayout>
  </div>
</template>