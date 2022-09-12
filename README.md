# Streamlit Component template in Vue.js

Vue 3 template to build a Streamlit component. Uses Vue.js scoped slot to send parameters from Streamlit Python script into `args` props of your component.

## Differences from the upstream

Built with [Vite](https://vitejs.dev/), Vue3 and Typescript to be light and fast.

## Setup


- Ensure you have [Python 3.8+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) and (optionally) [yarn](https://yarnpkg.com/getting-started/install)  installed.
- Generate template from this repo by using `Use this template` button on the repo's Github page.
- Create a new Python virtual environment for the template using your preferred method.
- Install Streamlit:

```
$ pip install streamlit
```

- Initialize and run the component template frontend:

```
$ cd my_component/frontend
$ yarn install    # Install the dependencies
$ yarn run dev  # Start the dev server
```

- From a separate terminal, run the template's Streamlit app:

```
$ streamlit run my_component/__init__.py
```

- If all goes well, you should see something like this:
  ![Quickstart Success](quickstart.png)
- Modify the frontend code at `my_component/frontend/src/Component.vue`.
  - Parameters passed by Python script are made available in `args` props.
- Modify the Python code at `my_component/__init__.py`.
- Feel free to rename the `my_component` folder, `Component.vue` file with its import in `app.vue`, and package name in `setup.py` and `package.json`.

## Resources

- [Higher Order Components in Vue.js](https://medium.com/bethink-pl/higher-order-components-in-vue-js-a79951ac9176)
- [Do we need Higher Order Components in Vue.js?](https://medium.com/bethink-pl/do-we-need-higher-order-components-in-vue-js-87c0aa608f48)
- [Build better higher-order components with Vue 3](https://blog.logrocket.com/build-better-higher-order-components-with-vue-3/)
- [Scoped slots](https://v3.vuejs.org/guide/component-slots.html#scoped-slots)
- [Using Slots in Vue.js](https://www.smashingmagazine.com/2019/07/using-slots-vue-js/)
- [Single File Components](https://v3.vuejs.org/guide/single-file-component.html)
- [SFC Spec](https://vue-loader.vuejs.org/spec.html)
