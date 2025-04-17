<template>
  <div class="flex h-[calc(100vh-4rem)]">
    <!-- Sidebar -->
    <div class="w-64 bg-white border-r border-gray-200">
      <div class="p-4">
        <h2 class="text-lg font-semibold text-gray-900">Conversations</h2>
        <div class="mt-4 space-y-2">
          <button 
            v-for="conversation in conversations" 
            :key="conversation.id"
            class="w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-100 rounded-md"
            @click="selectConversation(conversation.id)"
          >
            {{ conversation.title }}
          </button>
        </div>
      </div>
    </div>

    <!-- Chat Area -->
    <div class="flex-1 flex flex-col">
      <!-- Messages -->
      <div class="flex-1 overflow-y-auto p-4 space-y-4">
        <div 
          v-for="message in messages" 
          :key="message.id"
          :class="[
            'flex',
            message.sender === 'user' ? 'justify-end' : 'justify-start'
          ]"
        >
          <div 
            :class="[
              'max-w-lg rounded-lg px-4 py-2',
              message.sender === 'user' 
                ? 'bg-indigo-600 text-white' 
                : 'bg-gray-200 text-gray-900'
            ]"
          >
            {{ message.content }}
          </div>
        </div>
      </div>

      <!-- Input Area -->
      <div class="border-t border-gray-200 p-4">
        <div class="flex space-x-4">
          <input
            v-model="newMessage"
            type="text"
            class="flex-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            placeholder="Type your message..."
            @keyup.enter="sendMessage"
          />
          <button
            @click="sendMessage"
            class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'Chat',
  setup() {
    const store = useStore()
    const newMessage = ref('')
    const conversations = ref([])
    const selectedConversation = ref(null)

    const messages = computed(() => store.getters['chat/messages'])
    const isConnected = computed(() => store.getters['chat/isConnected'])

    onMounted(() => {
      store.dispatch('chat/connect')
      store.dispatch('chat/fetchHistory')
    })

    onUnmounted(() => {
      store.dispatch('chat/disconnect')
    })

    const sendMessage = () => {
      if (newMessage.value.trim() && isConnected.value) {
        store.dispatch('chat/sendMessage', {
          content: newMessage.value,
          sender: 'user'
        })
        newMessage.value = ''
      }
    }

    const selectConversation = (id) => {
      selectedConversation.value = id
      // TODO: Load conversation messages
    }

    return {
      newMessage,
      messages,
      conversations,
      selectedConversation,
      sendMessage,
      selectConversation
    }
  }
}
</script> 