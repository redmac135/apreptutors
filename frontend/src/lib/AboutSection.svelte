<div class="container" id="aboutus">
	<div class="content">
		<div class="text-container">
			<h1 class="title">Our Mission</h1>
			<p class="description">
				Preparing future IB students to excel in examinations with curated lessons, networking with
				recent alumni, and a vast database of resources specifically for IB students.
			</p>
		</div>
		<div class="info-container">
			<div class="info">
				<h2>IB</h2>
				<p>graduates</p>
			</div>
			<div class="right-sep" />
			<div class="info">
				<h2>7s</h2>
				<p>in all courses</p>
			</div>
			<div class="right-sep" />
			<div class="info">
				<h2>97<span class="weak">+</span></h2>
				<p>final mark averages</p>
			</div>
		</div>
	</div>
</div>

<style>
	.container {
		background-color: var(--light-blue);
		padding: 6rem;
		width: 100%;
		display: flex;
		justify-content: center;
	}

	.content {
		max-width: 60rem;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.text-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.title {
		font-size: 2rem;
		margin-bottom: 1rem;
	}

	.description {
		font-size: 1.5rem;
		width: 20rem;
		text-align: center;
		line-height: 1.5;
	}

	.info-container {
		display: flex;
		justify-content: space-evenly;
		margin-top: 3rem;
		width: 23rem;
	}

	.info {
		display: flex;
		flex-direction: column;
		justify-content: start;
		text-align: center;
		height: 100%;
		width: 7rem;
		margin: auto;
	}

	.right-sep {
		border-right: 2px solid var(--dark-blue);
	}

	.info h2 {
		font-size: 3rem;
	}

	.info h2 span.weak {
		font-size: 2rem;
		vertical-align: top;
	}

	@media (min-width: 450px) {
		.title {
			font-size: 3rem;
		}

		.description {
			width: 25rem;
		}
	}

	@media (min-width: 700px) {
		.info h2 {
			font-size: 4rem;
		}

		.description {
			width: 75%;
		}
	}

	@media (min-width: 1000px) {
		.content {
			flex-direction: row;
		}

		.info-container {
			flex-direction: column;
			justify-content: center;
			align-items: center;
			width: 8rem;
			margin: 0;
		}

		.info {
			width: 7rem;
		}

		.right-sep {
			border-right: 0;
			border-bottom: 2px solid var(--dark-blue);
			margin-top: 0.5rem;
			margin-bottom: 0.5rem;
			width: 100%;
		}
	}
</style>
