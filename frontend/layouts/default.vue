<script setup lang="ts">
</script>

<template>
    <div class="flex flex-col items-center">
        <Navbar class="col-span-full w-full mb-4 sticky top-0" />
        <div class="w-full xl:w-9/12 max-w-5xl">
            <slot />
        </div>
    </div>
</template>

<style lang="scss" scoped>

</style>