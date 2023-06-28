<script lang="ts">
	import { getContext } from 'svelte';
	import { detailkeys } from './DetailsContainer.svelte';
	import type { Writable } from 'svelte/store';

	export let summary: string;

	const activeFaq: Writable<string> = getContext(detailkeys);
</script>

<details
	open={$activeFaq === summary}
	on:toggle={({ target }) => {
		// @ts-ignore
		$activeFaq = target.open ? summary : $activeFaq;
	}}
>
	<summary>{summary}</summary>
	<slot />
</details>
