<script lang="ts">
    const YEAR = new Date().getFullYear();
</script>

<div class="container">
	<div class="top">
		<div class="col-1">
			<h1 class="logo">aPrep Tutors</h1>
			<p class="slogan">for ib students by ib students</p>
			<div class="socials">
				<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"
					><path
						fill="currentColor"
						d="M64 112c-8.8 0-16 7.2-16 16v22.1L220.5 291.7c20.7 17 50.4 17 71.1 0L464 150.1V128c0-8.8-7.2-16-16-16H64zM48 212.2V384c0 8.8 7.2 16 16 16H448c8.8 0 16-7.2 16-16V212.2L322 328.8c-38.4 31.5-93.7 31.5-132 0L48 212.2zM0 128C0 92.7 28.7 64 64 64H448c35.3 0 64 28.7 64 64V384c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V128z"
					/></svg
				>
				<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512"
					><path
						fill="currentColor"
						d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"
					/></svg
				>
			</div>
		</div>
		<div class="col-2">
			<h2>About</h2>
			<ul>
				<li>About us</li>
				<li>Our tutors</li>
				<li>Pricing</li>
			</ul>
		</div>
        <div class="col-2">
            <h2>Support</h2>
            <ul>
                <li>Become a tutor</li>
            </ul>
        </div>
	</div>
    <div class="line"></div>
	<div class="bottom">
		<p>Copyright &copy; {YEAR} aPrep Tutors - All Rights Reserved.</p>
	</div>
</div>

<style>
	.container {
		background-color: var(--dark-blue);
		color: var(--white);
		padding: 2rem;
	}

	.top {
		max-width: 60%;
		margin: 0 auto;
		display: flex;
        justify-content: space-between;
		gap: 2rem;
	}

	.col-1 {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	.logo {
		font-size: 3.5rem;
	}

	.slogan {
		font-size: 1.5rem;
	}

	.socials {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 1rem;
		margin-top: 2rem;
	}

	svg {
		height: 3rem;
		aspect-ratio: 1/1;
	}

	.col-2 {
		margin-top: 1rem;
	}

	.col-2 h2 {
		font-size: 2.5rem;
	}

	ul {
		list-style: none;
	}

	ul li {
		margin-top: 0.5rem;
        font-size: 1.5rem;
	}

    .line {
        height: 1px;
        background-color: var(--white);
        margin: 2.5rem auto;
        width: 60%;
    }

	.bottom {
		text-align: center;
	}

	@media (max-width: 800px) {
		.top {
			flex-direction: column;
			align-items: center;
			width: 100%;
		}

		.line {
			width: 100%;
		}

		.socials {
			justify-content: space-evenly;
			width: 100%;
		}

		svg {
			height: 2rem;
		}
	}
</style>
