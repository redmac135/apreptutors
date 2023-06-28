<script lang="ts">
	import '../app.css';
</script>

<nav>
	<ul class="nav-left">
		<li><a class="logo" href="/#">aPrep Tutors</a></li>
	</ul>
	<ul class="nav-right">
		<li class="link"><a href="/#aboutus">About us</a></li>
		<li class="link"><a href="/#pricing">Pricing</a></li>
		<li class="link"><a href="/comingsoon">Become a Tutor</a></li>
		<div class="divider-vertical" />
		<li class="link"><a href="/comingsoon">Log In</a></li>
		<!-- why does the chinese unicode mess up vert spacing :weary: -->
		<li class="link"><a href="/comingsoon">中文</a></li>
		<li><a href="/comingsoon"><button class="button">Find a Tutor</button></a></li>
	</ul>
</nav>

<style>
	nav {
		display: flex;
		background-color: var(--white);
		justify-content: space-between;
		width: 100%;
		max-width: 1140px;
		margin: 0.7rem auto;
		border-radius: 0.5rem;
		font-size: large;
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
		padding: 0.5rem 0.25rem;
		margin: 0.5rem 1rem;

		border-bottom: 2px solid transparent;
		transition: ease 0.5s;
	}

	ul.nav-right li.link a:hover {
		border-bottom: 2px solid var(--light-blue);
	}

	.nav-right {
		display: flex;
		align-items: center;
	}

	.nav-left {
		display: flex;
		align-items: center;
	}

	.logo {
		font-size: 3rem;
		font-weight: 600;
	}

	.divider-vertical {
		width: 1px;
		height: 40px;
		background-color: #b6ad90;
		margin-left: 0.25rem;
		margin-right: 0.25rem;
	}

	.button {
		background-color: var(--dark-blue); /* Green */
		border: none;
		color: white;
		padding: 1rem 2rem;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 16px;
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
</style>
