<script lang="ts">
	import Details from '$lib/Details.svelte';
	import DetailsContainer from '$lib/DetailsContainer.svelte';

	type Slide = {
		title: string;
		desc: string;
	};
	export let slides: Array<Slide>;
</script>

<div class="container">
	<DetailsContainer>
		{#each slides as slide}
			<Details summary={slide.title} content={slide.desc} />
		{/each}
	</DetailsContainer>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		overflow-x: hidden;
	}
</style>
