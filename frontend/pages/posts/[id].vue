<script setup lang="ts">
const { data } = await useFetch(`/api/blogs/${useRoute().params.id}`, { key: `blog-${useRoute().params.id}` })
</script>

<template>
    <div class="h-full ">
        <NuxtLayout>
            <div v-if="data" class="p-5">
                <h1 class="text-5xl font-bold">{{ data.title }}</h1>
                <h2 class="font-light text-xl">{{ data.subtitle }}</h2>
                <div class="flex text-gray-500 my-1">
                    <span>by {{ data.first_name }} {{ data.last_name }}</span>
                    <span class="mx-2">•</span>
                    <span class="">
                        {{ useDateFormat(data.created_at, 'MMM D', { locales: 'en-us' }).value }}
                    </span>
                </div>
                <div class="my-4 flex justify-center lg:justify-between">
                    <div id="readme" v-html="data.body"
                        class="w-full lg:w-3/4 prose max-w-none md:prose-lg lg:prose-xl">
                    </div>
                    <aside class="hidden lg:block w-1/4">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus asperiores est adipisci ipsam
                        dolore? Veniam, sed, illo iste saepe exercitationem accusantium nulla omnis iusto nihil
                        accusamus officia earum, quasi eos?
                    </aside>
                </div>
            </div>
        </NuxtLayout>
    </div>

</template>
