<script lang="ts">
	import Slogan from '../lib/Slogan.svelte';

	import AboutComponent from '../lib/AboutSection.svelte';
	import BackgroundSection from '../lib/BackgroundSection.svelte';
</script>

<main>
	<Slogan />

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

	.title-text {
		font: x-large;
		margin: 1rem 0;
		font-weight: 400;
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
</style>
