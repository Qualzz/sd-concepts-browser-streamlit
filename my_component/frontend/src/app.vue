<!--
  We bootstrap our Component to Streamlit with our scoped slot in the top-level App.
  This is where scoped slot passes Streamlit `args` data from itself to children MyComponent.
  You should not have to edit this, but are free to do so :)
-->
<template>
  <WithStreamlitConnection v-slot="{ args }">
    <Component :args="args" />
  </WithStreamlitConnection>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Component from './Component.vue'

// "withStreamlitConnection" is a scoped slot. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

export default defineComponent({
  name: 'App',
  components: {
    Component,
    WithStreamlitConnection,
  },
})
</script>

<style>
body, html {
  margin: 0;
}
</style>
