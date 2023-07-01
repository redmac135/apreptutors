<script>
	import InstructorProfile from './InstructorProfile.svelte';

	import { FOUNDERS } from './founders';
</script>

<div class="container">
	<div class="story">
		<h1>Our Story</h1>
		<p>
			Having finished the IB exams in 2023, a small group of passionate students came together with
			the goal of assisting future students and helping them excel at academically rigorous
			programs, such as the internationally recognized International Baccalaureate Programme.
		</p>
		<p>
			Our mission is to inspire, encourage, and motivate high school students by providing both
			quality tutoring support for learners of various academic streams and inviting them into a
			network of previous IB alumni.
		</p>
	</div>

	<div class="founders">
		<h1>Our Founders</h1>
		<div class="profiles">
			{#each FOUNDERS as { name, position, specialties, university, photo }}
				<div class="instructor">
					<InstructorProfile {name} {position} {specialties} {university} {photo} />
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.story {
		display: flex;
		flex-direction: column;
		padding: 1rem 2rem;
		margin: 1rem;
		text-align: center;
	}

	.story h1 {
		font-size: 2.5rem;
	}

	.story p {
		font-size: 1.1rem;
		margin-top: 1rem;
	}

	.founders {
		display: flex;
		flex-direction: column;
		margin: 1rem;
	}

	.founders h1 {
		font-size: 2.5rem;
		text-align: center;
		margin-bottom: 1rem;
	}

	.profiles {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}

	.instructor {
		margin: 0.5rem 1rem;
	}

	@media (min-width: 768px) {
		.story {
			padding: 1rem 12rem;
		}

		.founders {
			padding: 2rem;
		}
	}
</style>
