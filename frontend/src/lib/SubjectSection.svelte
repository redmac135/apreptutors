<script lang="ts">
	import Subjects from '$lib/Subjects.svelte';
	import { HL_SUBJECTS, SL_SUBJECTS } from '$lib/subjects_list';
</script>

<div class="container">
	<h1>Diversity in Subjects</h1>
	<p>
		In the IB Programme, there are HL and SL subjects, which stands for Higher Level and Standard
		Level. HL subjects require a more extensive and in-depth study compared to SL subjects. While
		both HL and SL subjects are rigorous and challenging, HL subjects provide students with a deeper
		understanding and preparation for higher education, while SL subjects offer a solid foundation
		in the subject area.
	</p>
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
		line-height: 1.5;
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

		p {
			max-width: 75%;
			margin: 1rem auto;
		}
	}
</style>
