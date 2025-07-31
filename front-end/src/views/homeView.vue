<script setup>
// No data needed for this simple landing page
</script>

<template>
  <div class="bg-gray-900 min-h-screen text-white">
    <section class="container mx-auto px-4 py-12">
      <!-- Hero Section -->
      <div class="text-center mb-10">
        <h1 class="text-4xl font-bold mb-4">Your AI Calendar Assistant</h1>
        <p class="text-xl text-gray-300 max-w-2xl mx-auto">
          Get smart summaries of your day using a local LLM model
        </p>
      </div>

      <!-- Two Key Features -->
      <div class="grid md:grid-cols-2 gap-8 mb-12 max-w-4xl mx-auto">
        <div class="bg-gray-800 p-6 rounded-lg">
          <h3 class="text-xl font-semibold mb-3">Daily Summary</h3>
          <p class="text-gray-400 mb-4">
            Ask "What's on my schedule today?" and get a concise, 
            intelligent summary of your meetings and appointments.
          </p>
          <div class="bg-gray-700 p-3 rounded">
            <p class="text-sm italic text-gray-300">
              "You have 3 meetings today, starting with a team standup at 9 AM. 
              Your afternoon is mostly clear after 2 PM."
            </p>
          </div>
        </div>

        <div class="bg-gray-800 p-6 rounded-lg">
          <h3 class="text-xl font-semibold mb-3">Local LLM Chat</h3>
          <p class="text-gray-400 mb-4">
            Chat with a powerful AI running directly on your system.
            No data sent to external servers.
          </p>
          <div class="bg-gray-700 p-3 rounded">
            <p class="text-sm italic text-gray-300">
              "All processing happens locally for maximum privacy and security."
            </p>
          </div>
        </div>
      </div>

      <!-- How It Works -->
      <div class="max-w-2xl mx-auto">
        <h2 class="text-2xl font-bold text-center mb-6">How It Works</h2>
        <div class="space-y-4">
          <div class="flex items-center">
            <span class="bg-indigo-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-4">1</span>
            <p>Sign in with Google to connect your calendar</p>
          </div>
          <div class="flex items-center">
            <span class="bg-indigo-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-4">2</span>
            <p>Ask about your schedule or chat with the AI</p>
          </div>
          <div class="flex items-center">
            <span class="bg-indigo-600 text-white rounded-full w-8 h-8 flex items-center justify-center mr-4">3</span>
            <p>Get instant, private responses powered by local LLM</p>
          </div>
        </div>
      </div>
    </section>     
  </div>
</template>