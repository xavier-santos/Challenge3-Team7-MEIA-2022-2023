<script setup>
import ChatPage from './components/chatpage/ChatPage.vue'
</script>

<template>
  <header>MEIA - Team 7 - Movie Recommendantion System</header>
  <main class="main">
    <ChatPage />
  </main>
</template>

<style scoped>
header {
  border-top: #193f6e 1px solid;
  border-bottom: #193f6e 1px solid;
  padding: 20px;
  text-align: center;
  font-size: large;
  font-weight: 400;
  background-color: #e1ebec;
  line-height: 1.5;
}

.main {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  overflow: hidden;
  justify-content: space-between;
}
</style>
