<script setup>
// No data needed for this simple page
</script>

<template>
  <div class="bg-gray-900 min-h-screen text-white flex flex-col items-center justify-center px-4 py-12">
    <div class="max-w-md w-full text-center">
      <span class="text-2xl text-indigo-400 font-semibold mb-4">
        What are you doing here?
      </span>
      <img class="w-24 h-24 m-auto" src="https://i.pinimg.com/736x/60/53/da/6053da0bb734ba028ea016b63c6fee33.jpg" />
      
    </div>
    <div class="text-center mt-8">
      <h1 class="text-5xl font-bold mb-4">404</h1>
      <h2 class="text-2xl font-bold mb-6">Page Not Found</h2>
      
      <div class="space-y-4">        
        <router-link 
          to="/" 
          class="inline-block bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-md transition duration-200"
        >
          Take Me Home
        </router-link>
      </div>
    </div>
  </div>
</template>