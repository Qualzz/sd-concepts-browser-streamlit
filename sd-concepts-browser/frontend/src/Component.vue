<template>
  <div class="bootstrap-wrapper pt-4">

    <div class="concept-gallery row">
      <div v-for="concept in args.concepts"
           :key="concept.name"
           class="col-12 col-sm-6 col-md-4 col-lg-4 col-xl-3">

        <div class="concept-card p-4">
          <div class="card-header row no-gutters">
            <div class="col">
              <h1 class="concept-title pl-1"><span class="token-char pr-0">&lt;</span>{{ concept.name }}<span class="pl-0 token-char">&gt;</span></h1>
            </div>

            <!-- <div class="col-auto card-favorite">
              <img width="24"
                   height="24"
                   class="icon-star"
                   src="./icons/star.svg" />
            </div> -->
          </div>

          <div class="concept-img-wrapper container-fluid p-0 row no-gutters">
            <div class="col-6 p-0"
                 v-for="(img, img_index) in concept.images"
                 :key="'concept_img'+img_index">
              <img class="concept-img p-1"
                   :src="'data:image/png;base64,'+img" />
            </div>
          </div>

          <div class="concept-card-footer row no-gutters pt-2">
            <div class="col pl-1">
              <div v-if="concept.type"
                   :class="{

                    'concept-type-tag': true,
                    'concept-type-style': concept.type.toLowerCase() === 'style',
                    'concept-type-object': concept.type.toLowerCase() === 'object'
                  }
                   ">
                {{ concept.type.toUpperCase() }}
              </div>
            </div>
            <div class="col-auto">
              <!-- Copy to clipboard button -->
              <button class="button"
                      @click="copyToClipboard(concept.token)">
                <!-- <img width="18"
                     height="18"
                     class="mr-2"
                     src="./icons/clipboard-solid.svg" /> -->
                Copy to clipboard
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
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

const copyToClipboard = (text: string) => {
  console.log("sending copy to clipboard event", text)
  Streamlit.setComponentValue("text")
}

// const enable_favorites = ref(false)
// const enable_copy_to_clipboard = ref(false)


</script>
<style>

.concept-card {
  background-color: var(--secondary-background-color);
  border-radius: 5px;
  margin-bottom: 20px;
}

.concept-title {
  margin-top: 0px;
  margin-bottom: 24px;
  font-size: 1em;
  color: var(--text-color);
}

.concept-img-wrapper {}

.card-favorite {
  text-align: end;
}

.concept-img {
  width: 100%;
  height: 160px;
  border-radius: 8px;
  max-height: 180px;
  object-fit: cover;
}

.icon-star {
  cursor: pointer;
  position: relative;
  top: -3px;
}

.token-char {
  color: #939393;
  font-weight: 700;
  position: relative;
  top: 1px;
}

.concept-card-footer {
  align-items: center;
}

.concept-type-tag {
  background-color: #898989;
  border-radius: 16px;
  padding: 5px 16px;
  font-size: 0.7em;
  color: #fff;
  display: inline-block;
  font-weight: bold;
}

.concept-type-style {
  background-color: #0095ff;
}

.concept-type-object {
  background-color: #ff9031;
}

.button {

  display: inline-flex;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  font-weight: 400;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  margin: 0px;
  line-height: 1.6;
  color: inherit;
  width: auto;
  user-select: none;
  background-color: var(--background-color);
  border: 1px solid rgba(128, 128, 128, 0.8);
}

.button:hover {
  color: var(--primary-color);
  border-color: var(--primary-color);
}

/* .button:focus {
  box-shadow: rgb(var(--primary-color) / 50%) 0px 0px 0px 0.2rem;
  outline: none;
}

.button:focus:not(:active) {
    border-color: var(--primary-color);
    color: var(--primary-color);
} */
</style>