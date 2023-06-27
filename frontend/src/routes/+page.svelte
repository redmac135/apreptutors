<script>
	import AboutComponent from './AboutComponent.svelte';

	import BackgroundSection from './BackgroundSection.svelte';
</script>

<main>
	<div class="section slogan-container">
		<h1 class="slogan">SLOGAN</h1>
		<!-- TODO ANCHORs -->
		<button><a href="/#">Learn More</a></button>
	</div>

	<AboutComponent />

	<BackgroundSection />

	<div class="section">
		<h1 class="title-text">What we offer</h1>
		<p>HL SUBJECT, HL SUBJECT, HL SUBJECT, HL SUBJECT, HL SUBJECT</p>
		<p>SL SUBJECT, SL SUBJECT, SL SUBJECT, SL SUBJECT, SL SUBJECT</p>
	</div>

	<div class="section">
		<h1 class="title-text">Pricing</h1>
		<div class="packages">
			<div class="pricing-package">
				<h2>Package 1</h2>
				<p>
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text
				</p>
			</div>
			<div class="pricing-package">
				<h2>Package 2</h2>
				<p>
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text
				</p>
			</div>
			<div class="pricing-package">
				<h2>Package 3</h2>
				<p>
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text
				</p>
			</div>
		</div>
	</div>
</main>

<style>
	.section {
		margin: 10rem auto;
		max-width: 75%;
	}

	.slogan-container {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.slogan {
		font-size: 6rem;
		font-family: 'sans-serif';
	}

	.flex-container {
		display: flex;
		justify-content: space-between;
	}

	.left-side {
		width: 50%;
	}

	.title-text {
		font: x-large;
		margin: 1rem 0;
		font-weight: 400;
	}

	.description-text {
		margin: 1rem 0;
	}

	.right-side {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 30%;
	}

	.packages {
		display: flex;
		justify-content: space-between;
	}

	.pricing-package {
		padding: 1rem;
		border: 1px solid black;
		margin: 0 0.5rem;
	}

	.pricing-package > h2 {
		text-align: center;
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
