<script context="module">
    export const detailkeys = {};
  </script>
  
  <script>
      import { setContext } from 'svelte';
      import { writable } from 'svelte/store';
      setContext(detailkeys, writable(""))
  </script>
  
  <slot />