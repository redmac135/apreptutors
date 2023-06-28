<script lang="ts">
	import Subjects from '$lib/Subjects.svelte';
	import { HL_SUBJECTS, SL_SUBJECTS } from '$lib/subjects_list';
</script>

<div class="container">
	<h1>Diversity in subjects</h1>
	<p>some text explaining the difference between hl and sl</p>
	<div class="subject-wrapper">
		<div class="subject-list">
			<h2>Higher level</h2>
			<Subjects slides={HL_SUBJECTS} />
		</div>
		<div class="subject-list">
			<h2>Standard level</h2>
			<Subjects slides={SL_SUBJECTS} />
		</div>
	</div>
</div>

<style>
	.container {
		margin: 6rem 0;
	}

	h1 {
		font-weight: 600;
		font-size: 3rem;
		margin-top: 1rem;
		text-align: center;
	}

	p {
		text-align: center;
		font-size: 1.5rem;
		margin: 1rem;
		margin-bottom: 0;
	}

	.subject-wrapper {
		display: flex;
		justify-content: center;
		align-items: start;
		flex-wrap: wrap;
	}

	.subject-list {
		margin: 1rem;
	}

	h2 {
		font-size: 2rem;
		margin-bottom: 1rem;
		font-weight: normal;
		text-align: center;
	}

	@media (min-width: 800px) {
		.subject-wrapper {
			margin-top: 4rem;
		}
	}
</style>
