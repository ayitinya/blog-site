<template>
    <div class="grid grid-cols-[minmax(auto,_20%)_minmax(min-content,_768px)_auto] grid-rows-[auto_1fr_auto] h-full">
        <Navbar class="col-span-full mb-4 sticky top-0"/>
        <div class="col-start-1 col-end-2 pl-4">
            <slot name="left" />
        </div>
        <main class="col-start-2 col-end-3 max-w-3xl bg-white rounded-lg border border-gray-200">
            <slot />
        </main>
        <aside class="col-start-3 col-end-4 pr-4">
            <slot name="right" />
        </aside>
    </div>
</template>