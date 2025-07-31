<script setup>
import { ref } from 'vue';

const isMobileMenuOpen = ref(false);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};
</script>

<template>
  <header class="bg-gray-800 shadow-md">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center py-4">
        <!-- Logo and Navigation in one group -->
        <div class="flex items-center space-x-8">
          <!-- Logo -->
          <span class="text-xl font-bold text-white">OllamaApp</span>
          
          <!-- Desktop Navigation moved next to logo -->
          <nav class="hidden md:flex space-x-8">
            <router-link to="/" class="text-gray-300 hover:text-white transition duration-200">
              Home
            </router-link>
            <router-link to="/chat" class="text-gray-300 hover:text-white transition duration-200">
              Chat
            </router-link>
          </nav>
        </div>

        <!-- Login Button (Desktop) -->
        <div class="hidden md:block">
          <a
            href="http://localhost:8000/accounts/google/login"
            class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-md transition duration-200"
          >
            Login
          </a>
        </div>

        <!-- Mobile Menu Button -->
        <button @click="toggleMobileMenu" class="md:hidden text-gray-300 hover:text-white">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              v-if="!isMobileMenuOpen"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
            <path
              v-else
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <div v-show="isMobileMenuOpen" class="md:hidden pb-4">
        <div class="flex flex-col space-y-4">
          <router-link
            to="/"
            class="text-gray-300 hover:text-white transition duration-200"
            @click="isMobileMenuOpen = false"
          >
            Home
          </router-link>
          <router-link
            to="/chat"
            class="text-gray-300 hover:text-white transition duration-200"
            @click="isMobileMenuOpen = false"
          >
            Chat
          </router-link>
          <a
            href="http://localhost:8000/accounts/google/login"
            class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-md transition duration-200 text-center"
          >
            Login
          </a>
        </div>
      </div>
    </div>
  </header>
</template>