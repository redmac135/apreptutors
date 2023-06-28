<script lang="ts">
	import PricingSection from '$lib/PricingSection.svelte';

	import Slogan from '$lib/Slogan.svelte';

	import AboutSection from '$lib/AboutSection.svelte';
	import BackgroundSection from '$lib/BackgroundSection.svelte';
</script>

<main>
	<Slogan />

	<AboutSection />

	<BackgroundSection />

	<div class="section">
		<h1 class="title-text">What we offer</h1>
		<p>HL SUBJECT, HL SUBJECT, HL SUBJECT, HL SUBJECT, HL SUBJECT</p>
		<p>SL SUBJECT, SL SUBJECT, SL SUBJECT, SL SUBJECT, SL SUBJECT</p>
	</div>

	<PricingSection />
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
</style>
