<div class="container">
	<h1>Tutor with aPrep Tutors</h1>
	<p>
		Existing tutors: Log in with your designated authorization code to fill in information regarding
		the subjects and times you're willing to tutor!
	</p>

	<p>
		Interested tutors: Please
		<a id="email" href="mailto:info@apreptutors.ca" target="_blank" rel="noopener noreferrer">
			email us
		</a>
		for further inquiries!
	</p>
	<button>
		<a id="a-button" href="/become-a-tutor/form">Get started</a>
	</button>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
        text-align: center;
		padding: 4rem;
        max-width: 40rem;
        margin: 0 auto;
	}

	p {
		font-size: 1.2rem;
		margin: 0.5rem 0;
	}

	button {
		background-color: var(--dark-blue);
		border: none;
		border-radius: 0.3rem;
		padding: 1rem 1.5rem;
		cursor: pointer;
		transition: background-color 0.2s ease-in-out;
		margin-top: 1rem;
	}

	button:hover {
		background-color: var(--light-blue);
	}

	#a-button {
		color: var(--white);
		text-decoration: none;
		font-size: 1.5rem;
		font-weight: bold;
	}

	#email {
		color: var(--dark-blue);
	}
</style>
