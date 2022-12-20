<script setup lang="ts">
const query = reactive(
    {
        limit: 10,
        offset: 0,
    }
)
const { data, refresh, pending } = await useFetch('/api/blogs/', { key: 'blogs', query: query });

watch(query, () => refresh())
</script>

<template>
    <div class="h-full">
        <NuxtLayout>
            <template #default>
                <div class="py-8 md:p-8">
                    <div class="flex items-center py-4">
                        <span class="text-2xl font-semibold min-w-fit pr-4 pl-5 md:pl-0">Latest Posts</span>
                        <hr class="w-full">
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3  gap-5">
                        <div v-for="blog in data!.results" :key="blog.id">
                            <BlogCard :blog="blog" :display-author="true" />
                        </div>
                    </div>
                    <div class="flex justify-center">
                        <LoadMoreBtn :pending="pending" v-if="data!.next" @click="query.limit += 10"/>
                    </div>
                </div>
            </template>
        </NuxtLayout>
    </div>
</template>
