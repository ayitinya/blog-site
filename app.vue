<script setup lang="ts">
const { data } = useFetch<string>('/api/posts/7878')

</script>

<template>
  <div v-html="data">
  </div>
</template>
