<script lang="ts">
	import Details from '$lib/Details.svelte';
	import DetailsContainer from '$lib/DetailsContainer.svelte';

	type Slide = {
		title: string;
		desc: string;
	};
	export let slides: Array<Slide>;

	let slide_idx = 0;
	function advance(n: number) {
		slide_idx += n;
		if (slide_idx < 0) slide_idx = slides.length - 1;
		else if (slide_idx >= slides.length) slide_idx = 0;
	}
</script>

<div class="container">
	<DetailsContainer>
		{#each slides as slide}
			<div class="summary">
				<Details summary={slide.title}>
					<p>{slide.desc}</p>
				</Details>
			</div>
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
		margin-left: 1.5rem;
		margin-right: 1.5rem;
	}

	.summary {
		background-color: #eee;
		color: #444;
		cursor: pointer;
		padding: 18px;
		width: 25rem;
		border: none;
		text-align: left;
		outline: none;
		font-size: 15px;
	}
</style>
