<script setup lang="ts">
const query = reactive({
  limit: 4,
  offset: 0,
})


const { data, refresh, pending } = await useFetch(
  `/api/users/${useRoute().params.id}`,
  { key: `user-${useRoute().params.id}-blogs`, query: query }
)

watch(query, () => refresh())

</script>

<template>
  <div class="h-full">
    <NuxtLayout>
      <div class="p-5 md:p-10">
        <div class="flex flex-col items-center md:items-start md:flex-row">
          <div class="flex flex-col w-full h-full flex justify-center">
            <img :src="data!.user.image" alt="User profile image">
            <div class="mt-2">
              <span class="font-bold">Contact</span>
              <div class="flex">
                <NuxtLink v-for="link in data!.user.social_links" :to="link.url" :external="true">
                  <Icon :name="`mdi:${link.name.toLocaleLowerCase()}`" class="mr-2" size="1.5rem" />
                </NuxtLink>
              </div>
            </div>

          </div>
          <div class="md:pl-5 prose max-w-none">
            <h1 class="text-2xl font-bold">{{ data!.user.first_name }} {{ data!.user.last_name }}</h1>
            <p class="">
              {{ data!.user.bio }}
            </p>
          </div>
        </div>
        <div class="flex items-center py-8">
          <h1 class="text-xl min-w-fit pr-4">Articles by {{ data!.user.first_name }} {{ data!.user.last_name }}</h1>
          <hr class="w-full">
        </div>
        <div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div v-for="blog in data!.blogs.results" :key="blog.id">
              <BlogCard :blog="blog" :display-author="false" />
            </div>
          </div>
          <div class="flex justify-center">
            <LoadMoreBtn v-if="data!.blogs.next" @click="query.limit += 10" :pending="pending" />
          </div>
        </div>
      </div>
    </NuxtLayout>
  </div>
</template>