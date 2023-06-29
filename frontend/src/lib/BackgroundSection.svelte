<div class="section">
	<div class="container">
		<h1 class="title">Taught by Experienced Graduates</h1>
		<p class="description">
			Our tutors are recent graduates of the IB program, scoring top marks in their respective
			subjects. They will be attending top competitive programs in Canada, such as Waterloo CS,
			McMaster Health Sciences and Western Ivey. With their fresh academic insight and first-hand
			experience, they will mentor young students and give them the resources to succeed in high
			school.
		</p>
		<div class="uni-logo-container">
			<img src="images/western.png" alt="western university logo" class="western-logo" />
			<img src="images/waterloo.png" alt="waterloo university logo" class="waterloo-logo" />
			<img src="images/mcmaster.png" alt="mcmaster university logo" class="mcmaster-logo" />
		</div>
		<div class="uni-crest-container">
			<img src="images/westerncrest.png" alt="western university crest" class="western-crest" />
			<img src="images/waterloocrest.png" alt="waterloo university crest" class="waterloo-crest" />
			<img src="images/mcmastercrest.png" alt="mcmaster university crest" class="mcmaster-crest" />
		</div>
		<!-- TODO update anchor -->
		<button><a href="/#">Learn more about our tutors</a></button>
	</div>
</div>

<style>
	.section {
		background-color: var(--beige);
	}

	.container {
		width: 100%;
		margin: auto;
		padding: 2rem;
		/* center all elements under this */
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.title {
		font-size: 3rem;
		text-align: center;
		margin: 1rem 0;
	}

	.description {
		font-size: 1.5rem;
		text-align: center;
		margin: 1rem 0;
		width: 100%;
		line-height: 1.5;
	}

	.uni-logo-container {
		display: none;
	}

	.uni-crest-container img {
		height: 6rem;
	}

	.uni-crest-container {
		width: 30rem;
		display: flex;
		justify-content: space-evenly;
		margin: 2.5rem 0;
	}

	.western-logo {
		height: 7rem;
	}

	.waterloo-logo {
		height: 8rem;
		padding-left: 2rem;
		padding-right: 2rem;
	}

	.mcmaster-logo {
		height: 9rem;
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

	@media (min-width: 600px) {
		.uni-crest-container img {
			height: 8rem;
		}

		.container {
			padding: 4rem;
		}
	}

	@media (min-width: 900px) {
		.container {
			width: 100%;
		}

		.description {
			margin: 0.5rem 0;
		}
	}

	@media (min-width: 1300px) {
		.description {
			width: 80%;
		}

		.uni-logo-container {
			width: 100%;
			display: flex;
			justify-content: space-evenly;
			margin: 2.5rem 0;
		}

		.uni-crest-container {
			display: none;
		}
	}
</style>
