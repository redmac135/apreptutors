<script lang="ts">
	import '../app.css';
</script>

<nav>
	<ul class="nav-left">
        <li><a href="/#">LOGO</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/pricing">Pricing</a></li>
    </ul>
    <ul class="nav-right">
        <li><a href="/login">Log In</a></li>
        <!-- why does the chinese unicode mess up vert spacing :weary: -->
        <li><a href="/zh">chinese</a></li>
    </ul>
</nav>

<slot />

<style>
    nav {
        display: flex;
        background-color: var(--light-blue);
        justify-content: space-between;
        max-width: 75%;
        margin: 0.7rem auto;
        border-radius: 0.5rem;
    }

    ul {
        list-style-type: none;
        overflow: hidden;
    }

    li {
        float: left;
    }

    li a {
        text-decoration: none;
        display: block;
        color: var(--white);
        padding: 1rem 1.5rem;
        text-align: center;
    }

    li a:hover {
        background-color: var(--dark-blue);
        border-radius: 0.5rem;
    }
</style>
