<template>
  <div>
    <p>Hello, {{ args.name }}! &nbsp;</p>
    <button @click="onClicked">Click Me!</button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { Streamlit, Theme } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"

interface IProps {
  args: any;
  disabled: boolean;
  theme: Theme;
}

useStreamlit(); // lifecycle hooks for automatic Streamlit resize
const props = defineProps<IProps>();

const numClicks = ref(0)
const onClicked = () => {
  numClicks.value++
  Streamlit.setComponentValue(numClicks.value)
}
</script>
<style scoped>
  p { margin-block: 0 20px;}
</style>