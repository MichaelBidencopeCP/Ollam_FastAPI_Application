<script setup>
import { ref, onMounted } from 'vue';

// Sample chat messages for demonstration
const messages = ref([
]);

const newMessage = ref('');
const chatContainer = ref(null);

// Websocket connection
onMounted


const sendMessage = () => {
  if (newMessage.value.trim() === '') return;
  
  // Add user message
  messages.value.push({
    id: messages.value.length + 1,
    sender: 'user',
    content: newMessage.value
  });
  
  // Clear input
  const userMessage = newMessage.value;
  newMessage.value = '';
  

    
  // Scroll to bottom after adding new messages
  scrollToBottom();
  
};

const scrollToBottom = () => {
  setTimeout(() => {
    if (chatContainer.value) {
      chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
    }
  }, 50);
};

onMounted(() => {
  scrollToBottom();
});
</script>

<template>
  <div class="bg-gray-900 min-h-screen text-white pt-4 pb-8 px-4">
    <div class="max-w-3xl mx-auto flex flex-col h-[80vh]">
      <h1 class="text-2xl font-bold mb-4">Chat with Your Calendar Assistant</h1>
      
      <!-- Chat Messages Container -->
      <div 
        ref="chatContainer"
        class="flex-grow bg-gray-800 rounded-t-lg p-4 overflow-y-auto"
      >
        <div v-for="message in messages" :key="message.id" class="mb-4">
          <!-- User Message -->
          <div v-if="message.sender === 'user'" class="flex justify-end">
            <div class="bg-indigo-600 text-white p-3 rounded-lg max-w-[80%]">
              {{ message.content }}
            </div>
          </div>
          
          <!-- AI Message -->
          <div v-else class="flex justify-start">
            <div class="bg-gray-700 text-white p-3 rounded-lg max-w-[80%]">
              {{ message.content }}
            </div>
          </div>
        </div>
      </div>
      
      <!-- Message Input -->
      <div class="bg-gray-800 rounded-b-lg p-4 border-t border-gray-700">
        <form @submit.prevent="sendMessage" class="flex">
          <input
            v-model="newMessage"
            type="text"
            placeholder="Type your message..."
            class="flex-grow bg-gray-700 text-white p-2 rounded-l-md focus:outline-none"
          />
          <button
            type="submit"
            class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-r-md transition duration-200"
          >
            Send
          </button>
        </form>
      </div>
    </div>
  </div>
</template>