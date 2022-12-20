<script setup lang="ts">
</script>

<template>
    <div class="flex flex-col items-center min-h-screen">
        <Navbar class="" />
        <div class="w-full xl:w-9/12 max-w-5xl">
            <slot />
        </div>
        <Footer class="mt-auto w-full shrink-0 grow-0" />
    </div>
</template>

<style lang="scss" scoped>

</style>