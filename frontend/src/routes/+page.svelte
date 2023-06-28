<script lang="ts">
	import PricingSection from '$lib/PricingSection.svelte';

	import Subjects from '$lib/Subjects.svelte';
	import { HL_SUBJECTS, SL_SUBJECTS } from '$lib/subjects_list';
	import Slogan from '$lib/Slogan.svelte';

	import AboutSection from '$lib/AboutSection.svelte';
	import BackgroundSection from '$lib/BackgroundSection.svelte';
</script>

<main>
	<Slogan />

	<AboutSection />

	<BackgroundSection />

	<Subjects slides={HL_SUBJECTS} />
	<Subjects slides={SL_SUBJECTS} />

	<PricingSection />
</main>
