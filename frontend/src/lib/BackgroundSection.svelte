<div class="section">
	<div class="container">
		<h1 class="title">Taught by experienced graduates</h1>
		<p class="description">
			Our tutors are good students graduating from the IB program. Each of them have scored 7s in
			their respective subjects. They will be attending top canadian universities such as:
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
		width: 75%;
		margin: auto;
		padding: 4rem;
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
		width: 60%;
	}

	.uni-logo-container {
		display: none;
	}

	.uni-crest-container img {
		height: 8rem;
	}

	.uni-crest-container {
		width: 30rem;
		display: flex;
		justify-content: space-evenly;
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

	@media (min-width: 1300px) {
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
