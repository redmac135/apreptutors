<script lang="ts">
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
	<button on:click={() => advance(-1)}>&larr;</button>
	{#each slides as slide, i}
		<div class={i === slide_idx ? 'slide active' : 'slide'}>
			<h1 class="title">{slide.title}</h1>
			<p class="description">{slide.desc}</p>
		</div>
	{/each}
	<button on:click={() => advance(1)}>&rarr;</button>
</div>

<style>
	.container {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.slide {
		display: none;
		width: 60%;
		height: 15rem;
		border: 1px solid black;
		border-radius: 0.5rem;
		padding: 1rem;
		overflow: hidden;
	}

	.slide.active {
		display: block;
		position: relative;
	}

	.slide.active::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 6rem;
		background: linear-gradient(transparent, var(--white));
	}

	.title {
		font-size: 2.5rem;
	}

	.description {
		margin-top: 0.5rem;
		font-size: 1.5rem;
	}

	button {
		background: none;
		border: none;
		font-size: 2rem;
		cursor: pointer;
		margin: 0 1rem;
	}
</style>
