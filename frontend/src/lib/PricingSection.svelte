<div class="container">
	<h1>Pricing</h1>
	<div class="packages">
		<img src="images/privatepricing.png" alt="Prices for private lessons" />
		<img src="images/grouppricing.png" alt="Prices for group lessons" />
	</div>
</div>

<style>
	.container {
		padding: 4rem 0;
		background-color: var(--beige);
	}

	h1 {
		text-align: center;
		font-size: 3rem;
		margin: 2rem 0;
	}

	.packages {
		display: flex;
		justify-content: space-between;
		flex-wrap: wrap;
		max-width: 90%;
		margin: auto;
	}

	img {
		width: 100%;
		height: auto;
		padding: 1rem;
	}

	@media (min-width: 800px) {
		.packages {
			max-width: 60%;
		}

		img {
			width: 50%;
		}

	}
</style>
