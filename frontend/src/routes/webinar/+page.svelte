<div class="container">
	<p class="intro">aPrep Tutors presents...</p>
	<p class="title"><span class="highlight">The IB Perspective Webinar!</span></p>
	<p class="date">July 21, 7:00pm - 8:30pm</p>
	<p class="description">
		Join us for a discussion of the following topics, from recent graduates of the IB Programme.
	</p>
	<a
		class="register"
		href="https://westernuniversity.zoom.us/j/92168956716"
		target="_blank"
		rel="noopener noreferrer"
	>
		Zoom Meeting Link &rarr;
	</a>
	<div class="topic">
		<div class="topic-text">
			<h2>Getting into the <span class="highlight">IB Programme.</span></h2>
		</div>
		<div class="promo">
			<img src="/images/webinar/promo1.png" alt="webinar promotion" />
		</div>
	</div>
	<div class="topic reverse">
		<div class="topic-text">
			<h2>Applying to <span class="highlight">university</span> from IB.</h2>
		</div>
		<div class="promo">
			<img src="/images/webinar/promo2.png" alt="webinar promotion" />
		</div>
	</div>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		padding: 1rem;
		text-align: center;
		align-items: center;
		justify-content: center;
	}

	.container * {
		margin: 0.2rem 0;
	}

	.highlight {
		color: var(--dark-blue);
	}

	.intro {
		font-style: italic;
		font-size: 1.5rem;
	}

	.title {
		font-size: 2.5rem;
		font-weight: bold;
	}

	.date::before {
		content: '📅 ';
	}

	.date {
		font-size: 1.3rem;
		background-color: var(--light-blue);
		padding: 0.5rem;
		border-radius: 0.5rem;
		color: var(--white);
		font-weight: 500;
		margin: 1rem 0;
	}

	.description {
		font-size: 1.25rem;
	}

	.topic {
		display: flex;
		flex-direction: column;
		width: 100%;
		max-width: 76rem;
	}

	.topic-text {
		display: flex;
		align-items: center;
		justify-content: center;
		text-align: center;
		padding: 0 2rem;
	}

	h2 {
		font-size: 2rem;
		font-weight: bold;
	}

	.promo {
		padding: 0 2rem;
	}

	img {
		width: 100%;
		height: auto;
		border-radius: 2rem;
		box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
	}

	.register {
		background-color: var(--dark-blue);
		text-decoration: none;
		font-size: 1.25rem;
		color: var(--white);
		padding: 1rem 4rem;
		border-radius: 1rem;
		border: 2px solid var(--dark-blue);
		transition: all 0.4s ease-in-out;
		margin: 3rem 0;
	}

	.register:hover {
		background-color: var(--white);
		color: var(--dark-blue);
	}

	@media (min-width: 800px) {
		.container {
			margin: 2rem 0;
		}

		.title {
			font-size: 3rem;
		}

		.topic {
			flex-direction: row;
		}

		.topic-text {
			width: 50%;
		}

		h2 {
			font-size: 2.5rem;
		}

		.promo {
			width: 50%;
		}

		.reverse {
			flex-direction: row-reverse;
		}

		.register {
			font-size: 1.25rem;
		}
	}
</style>
