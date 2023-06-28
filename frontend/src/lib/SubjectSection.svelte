<script lang="ts">
	import Subjects from '$lib/Subjects.svelte';
	import { HL_SUBJECTS, SL_SUBJECTS } from '$lib/subjects_list';
</script>

<h1>Subjects we Teach</h1>
<div class="subject-wrapper">
	<Subjects slides={HL_SUBJECTS} />
	<Subjects slides={SL_SUBJECTS} />
</div>

<style>
	h1 {
		display: flex;
		justify-content: center;
		font-weight: 600;
		font-size: 3rem;
		margin-top: 1rem;
	}

	.subject-wrapper {
		display: flex;
		justify-content: center;
		align-items: start;
		margin-top: 1rem;
	}
</style>
