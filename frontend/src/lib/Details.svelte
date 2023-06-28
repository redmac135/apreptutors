<script>
	import { getContext } from 'svelte';
    import { detailkeys } from './DetailsContainer.svelte';
	
	export let summary;

	const activeFaq = getContext(detailkeys);
</script>

<details open={$activeFaq === summary} on:toggle={({target}) => {$activeFaq = target.open ? summary : $activeFaq}}>
  <summary>{summary}</summary>
	<slot />
</details>