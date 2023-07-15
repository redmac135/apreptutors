<script lang="ts">
	import { fly } from 'svelte/transition';
	let state: number = 0;

	function cycleText() {
		state = (state + 1) % 2;
	}

	function sloganLoop() {
		setTimeout(function () {
			cycleText();
			sloganLoop();
		}, 2000);
	}

	sloganLoop();
</script>

<section>
	<div class="section container">
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
		<a href="/#aboutus"><button>Learn More</button></a>
	</div>
</section>

<style>
	section {
		background-image: url('/images/sloganbackground.webp');
		background-position: center;
		background-size: cover;
		background-attachment: fixed;
		height: 70vh;
	}

	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 10rem;
		margin: auto;
		max-width: 75%;
	}

	.rolling-text {
		font-style: italic;
		position: absolute;
		text-align: center;
		width: 100%;
		margin-left: auto;
		margin-right: auto;
		top: -3rem;
	}

	.slogan span {
		font-family: 'sans-serif';
	}

	button {
		background-color: var(--dark-blue);
		border: none;
		border-radius: 0.3rem;
		padding: 1rem 2rem;
		margin: 2rem 0;
		cursor: pointer;
		transition: all 0.2s ease-in-out;
		color: var(--white);
		text-decoration: none;
		font-size: 1rem;
	}

	button:hover {
		background-color: var(--light-blue);
	}

	.slogan {
		position: relative;
		font-size: 3rem;
	}

	@media (min-width: 400px) {
		.container {
			overflow-y: hidden;
		}

		.rolling-text {
			left: 0;
			top: 0;
			margin: 0;
			width: auto;
		}

		.slogan span {
			padding-left: 4rem;
		}

		.rolling-text#txt1 {
			transform: translateX(-5rem);
		}

		.rolling-text#txt2 {
			transform: translateX(-3.75rem);
		}
	}

	@media (min-width: 850px) {
		.slogan {
			font-size: 6rem;
		}

		.slogan span {
			padding-left: 8rem;
		}

		.rolling-text#txt1 {
			transform: translateX(-10rem);
		}

		.rolling-text#txt2 {
			transform: translateX(-7.5rem);
		}
	}
</style>
