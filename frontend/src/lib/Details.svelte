<script lang="ts">
	import { getContext } from 'svelte';
    import { detailkeys } from './DetailsContainer.svelte';
	
	export let summary: string;

	const activeDetail = getContext(detailkeys);
</script>

<details open={$activeDetail === summary} on:toggle={({target}) => {$activeDetail = target.open ? summary : $activeDetail}}>
  <summary>{summary}</summary>
	<slot />
</details>