<script lang="ts">
	import { fly } from 'svelte/transition';
	let state: number = 0;

	function cycleText() {
		state = (state + 1) % 3;
	}

	function sloganLoop() {
		setTimeout(function () {
			cycleText();
			sloganLoop();
		}, 2000);
	}

	sloganLoop();
</script>

<div class="section slogan-container">
	<h1 class="slogan">
		{#if state === 0}
			<span
				class="rolling-text"
				id="txt2"
				in:fly={{ duration: 200, y: -100 }}
				out:fly={{ duration: 200, y: 100 }}>By</span
			>
		{:else if state === 1}
			<span
				class="rolling-text"
				id="txt1"
				in:fly={{ duration: 200, y: -100 }}
				out:fly={{ duration: 200, y: 100 }}>For</span
			>
		{/if}
		<span>&nbsp;IB students</span>
	</h1>
	<!-- TODO ANCHORs -->
	<button><a href="/#">Learn More</a></button>
</div>

<style>
	.section {
		margin: 10rem auto;
		max-width: 75%;
		overflow: hidden;
	}

	.slogan-container {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.slogan {
		position: relative;
		font-size: 6rem;
	}

	.rolling-text {
		font-style: italic;
		position: absolute;
		left: 0;
	}

	.rolling-text#txt1 {
		transform: translateX(-11rem);
	}

	.rolling-text#txt2 {
		transform: translateX(-8.5rem);
	}

	.slogan span {
		font-size: 6rem;
		font-family: 'sans-serif';
		padding-left: 8rem;
	}

	button {
		background-color: var(--dark-blue);
		border: none;
		border-radius: 0.3rem;
		padding: 1rem 2rem;
		margin: 2rem 0;
		cursor: pointer;
		transition: all 0.2s ease-in-out;
	}

	button:hover {
		background-color: var(--light-blue);
	}

	button a {
		color: var(--white);
		text-decoration: none;
		font-size: 1rem;
	}
</style>
