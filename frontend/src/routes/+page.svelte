<main>
	<div class="section slogan-container">
		<h1 class="slogan">SLOGAN</h1>
		<!-- TODO ANCHORs -->
		<div><a href="/#">Learn More</a></div>
	</div>

	<div class="section flex-container">
		<div class="left-side">
			<h1 class="title-text">Who we are</h1>
			<p class="description-text">
				mission statement text mission statement text mission statement text mission statement text
				mission statement text mission statement text mission statement text mission statement text
				mission statement text mission statement text mission statement text mission statement text
				mission statement text mission statement text mission statement text
			</p>
		</div>
		<div class="right-side">image</div>
	</div>

	<div class="section">
		<h1 class="title-text">Background</h1>
		<p class="description-text">
			background text background text background text background text background text background
			text background text background text background text background text background text
			background text background text background text background text background text background
			text background text background text background text background text background text
			background text background text background text
		</p>
	</div>

	<div class="section">
		<h1 class="title-text">What we offer</h1>
		<p>HL SUBJECT, HL SUBJECT, HL SUBJECT, HL SUBJECT, HL SUBJECT</p>
		<p>SL SUBJECT, SL SUBJECT, SL SUBJECT, SL SUBJECT, SL SUBJECT</p>
	</div>

	<div class="section">
		<h1 class="title-text">Pricing</h1>
		<div class="packages">
			<div class="pricing-package">
				<h2>Package 1</h2>
				<p>
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text
				</p>
			</div>
			<div class="pricing-package">
				<h2>Package 2</h2>
				<p>
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text
				</p>
			</div>
			<div class="pricing-package">
				<h2>Package 3</h2>
				<p>
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text pricing text pricing text pricing text pricing text pricing text pricing text
					pricing text
				</p>
			</div>
		</div>
	</div>
</main>

<style>
	main {
		margin: auto;
		max-width: 75%;
	}

	.section {
		margin: 10rem 0;
	}

	.slogan-container {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.slogan {
		font-size: 6rem;
	}

	.flex-container {
		display: flex;
		justify-content: space-between;
	}

	.left-side {
		width: 50%;
	}

	.title-text {
		font: x-large;
		margin: 1rem 0;
	}

	.description-text {
		margin: 1rem 0;
	}

	.right-side {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 30%;
	}

	.packages {
		display: flex;
		justify-content: space-between;
	}

	.pricing-package {
		padding: 1rem;
		border: 1px solid black;
		margin: 0 0.5rem;
	}

	.pricing-package > h2 {
		text-align: center;
	}
</style>
