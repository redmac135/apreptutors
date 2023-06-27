<main>
	<div class="intro">
		<div class="left-side">
			<h1>aPrep Tutoring</h1>
			<p class="description">
				small description goes here Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
				eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
				nostrud exercita
			</p>
			<div class="subjects">
                <p>HL: subjects subjects subjects</p>
                <p>SL: subjects subjects subjects</p>
            </div>
            <button type="button">Register</button>
		</div>
		<div class="right-side">image</div>
	</div>
</main>

<style>
	main {
		margin: auto;
		max-width: 75%;
	}

	.intro {
		display: flex;
		justify-content: space-evenly;
        margin: 6rem 0;
	}

    .left-side {
        width: 50%;
    }

	.left-side > h1 {
		padding: 0.5rem;
		font: x-large;
		color: var(--white);
		background-color: var(--dark-blue);
		transform: skew(-5deg);
		transform-origin: top;
	}

    .description {
        margin: 0.5rem 0;
    }

	.right-side {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 30%;
	}

	button {
		font-size: large;
        color: var(--white);
		padding: 0.7rem;
		background-color: var(--light-blue);
		border-radius: 0.5rem;
	}
</style>
