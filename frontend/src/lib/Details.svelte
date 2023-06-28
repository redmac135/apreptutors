<script lang="ts">
	import { getContext } from 'svelte';
	import { detailkeys } from './DetailsContainer.svelte';
	import type { Writable } from 'svelte/store';

	export let summary: string;
	export let content: string;

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
	<p class="content">{content}</p>
</details>

<style>
	details {
		background-color: var(--light-blue);
		color: black;
		margin-bottom: 0.5rem;
		cursor: pointer;
		width: 25rem;
		padding: 1rem;
		border: 2px solid var(--dark-blue);
		border-radius: 0.5rem;
	}

	summary {
		border: none;
		text-align: left;
		outline: none;
		font-weight: 500;
		font-size: 1.2rem;
	}

	.content {
		border-top: 2px solid var(--dark-blue);
		margin-top: 1rem;
		padding-top: 1rem;
	}
</style>
