<script lang="ts">
	let open = false;
	function toggle() {
		open = !open;
	}
</script>

<nav>
	<ul class="nav-left">
		<li><a class="logo" href="/#">aPrep Tutors</a></li>
		<button class="burger" on:click={toggle}>
			<div class="line line1" />
			<div class="line line2" />
			<div class="line line3" />
		</button>
	</ul>
	<ul class="nav-right" class:nav-open={open}>
		<li class="link"><a href="/#aboutus">About us</a></li>
		<li class="link"><a href="/#pricing">Pricing</a></li>
		<li class="link"><a href="/comingsoon">Become a Tutor</a></li>
		<div class="divider-vertical" />
		<li class="link"><a href="/comingsoon">Log In</a></li>
		<li class="link"><a href="/comingsoon">中文</a></li>
		<!-- todo: change href to find-a-tutor -->
		<li><a href="/comingsoon"><button class="button">Find a Tutor</button></a></li>
	</ul>
</nav>

<style>
	nav {
		background-color: var(--white);
		justify-content: space-between;
		width: 100%;
		max-width: 1140px;
		margin: 0.7rem auto;
		align-items: center;
		padding: 0rem 1rem;
	}

	.burger {
		display: block;
		cursor: pointer;
		margin: 0.5rem;
		height: max-content;
		background: none;
		border: none;
	}

	.line {
		width: 2rem;
		height: 0.2rem;
		background-color: black;
		margin: 0.3rem;
	}

	ul {
		list-style-type: none;
		overflow: hidden;
	}

	li a {
		text-decoration: none;
		display: block;
		color: black;
		text-align: center;
	}

	ul.nav-right li.link a {
		padding: 0.5rem;
		border-bottom: 2px solid transparent;
		transition: ease 0.5s;
		width: max-content;
		margin: auto;
	}

	ul.nav-right li.link a:hover {
		border-bottom: 2px solid var(--light-blue);
	}

	.nav-right {
		display: none;
	}

	.nav-left {
		display: flex;
		align-items: center;
		width: 100%;
		justify-content: space-between;
	}

	.nav-open {
		display: flex;
		flex-direction: column;
	}

	.logo {
		font-size: 1.5rem;
		font-weight: 600;
	}

	.divider-vertical {
		display: none;
		width: 1px;
		height: 40px;
		background-color: #b6ad90;
		margin-left: 0.25rem;
		margin-right: 0.25rem;
	}

	.button {
		background-color: var(--dark-blue);
		border: none;
		color: white;
		padding: 0.5rem;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: small;
		margin: 4px 2px;
		transition-duration: 0.4s;
		cursor: pointer;
		border: 2px solid transparent;
	}

	.button:hover {
		background-color: white;
		color: var(--dark-blue);
		border-color: var(--dark-blue);
	}

	@media (min-width: 600px) {
		nav {
			display: flex;
		}

		.divider-vertical {
			display: block;
		}

		.burger {
			display: none;
		}

		.nav-left {
			width: max-content;
		}

		.nav-right {
			display: flex;
			align-items: center;
			flex-direction: row;
		}

		ul.nav-right li.link a {
			padding: 0.5rem 0.25rem;
			margin: 0.5rem 1rem;
		}
	}

	@media (min-width: 800px) {
		nav {
			font-size: large;
		}

		.logo {
			font-size: 2rem;
		}

		ul.nav-right li.link a {
			padding: 0.5rem 0.25rem;
			margin: 0.5rem 1rem;
		}

		.button {
			padding: 0.5rem 1rem;
			font-size: medium;
		}
	}
</style>
