<script lang="ts">
	import '../app.css';
</script>

<nav>
	<div>LOGO</div>
	<div class="nav-right">
		<p>中文</p>
		<button>login</button>
	</div>
</nav>

<style>
	nav {
		display: flex;
		justify-content: space-between;
		align-items: center;
        padding: 0.5rem;
		background-color: var(--light-blue);
	}

    .nav-right {
        display: flex;
        align-items: center;
    }

    /* have a bit of space in between chinese and login */
    .nav-right > * {
        margin-left: 1rem;
    }

    .nav-right > button {
        background-color: var(--light-blue);
        padding: 0.5rem;
        border-color: var(--dark-blue);
        border-radius: 0.4rem;
    }
</style>
