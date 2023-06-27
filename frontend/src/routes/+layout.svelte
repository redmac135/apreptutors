<script lang="ts">
	import '../app.css';
</script>

<nav>
	<ul class="nav-left">
		<li><a href="/#">LOGO</a></li>
	</ul>
	<ul class="nav-right">
        <li><a href="">About us</a></li>
        <li><a href="">Become a Tutor</a></li>
        <li><a href="/pricing">Pricing</a></li>
		<div class="divider-vertical" />
		<li><a href="/login">Log In</a></li>
		<!-- why does the chinese unicode mess up vert spacing :weary: -->
		<li><a href="/zh">中文</a></li>
		<li><a href="">Find a Tutor</a></li>
	</ul>
</nav>

<slot />

<style>
	nav {
		display: flex;
		background-color: white;
		justify-content: space-between;
        width: 100%;
		max-width: 1140px;
		margin: 0.7rem auto;
		border-radius: 0.5rem;
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

	ul.nav-right li a {
		padding: 0.5rem 0.25rem;
        margin: 0.5rem 1rem;

        border-bottom: 2px solid transparent;
        transition: ease 0.5s;
	}

	ul.nav-right li a:hover {
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

	.divider-vertical {
		width: 1px;
		height: 40px;
		background-color: #b6ad90;
        margin-left: 0.25rem;
        margin-right: 0.25rem;
	}
</style>
