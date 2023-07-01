<script lang="ts">
	import { GoogleAuthProvider, getAuth, signInWithPopup } from 'firebase/auth';
	import { get } from 'svelte/store';
	import firebaseApp from '../store';

	const app = get(firebaseApp);

	const loginWithGoogle = () => {
		// @ts-ignore
		const auth = getAuth(app);
		signInWithPopup(auth, new GoogleAuthProvider());
	};
</script>

<div class="container">
	<img class="logo" src="images/logos/logo1.png" alt="aprep tutors logo" />
	<h1>Your journey to success starts here!</h1>
	<button class="login-google" on:click={loginWithGoogle}>Sign up with Google</button>
</div>

<style>
	:root {
		--content-width: 18rem;
	}

	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		background-color: var(--beige);
		width: 24rem;
		padding: 2rem;
		margin: 6rem auto;
        border-radius: 0.3rem;
        box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
	}

	/* logo and welcome text */
	.logo {
		width: 5rem;
		height: auto;
	}

	h1 {
		font-size: 1.5rem;
		font-weight: 500;
		width: var(--content-width);
		text-align: center;
        margin-top: 0.5rem;
        margin-bottom: 1.5rem;
	}

	/* login button */
	.login-google {
		background-image: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNMTcuNiA5LjJsLS4xLTEuOEg5djMuNGg0LjhDMTMuNiAxMiAxMyAxMyAxMiAxMy42djIuMmgzYTguOCA4LjggMCAwIDAgMi42LTYuNnoiIGZpbGw9IiM0Mjg1RjQiIGZpbGwtcnVsZT0ibm9uemVybyIvPjxwYXRoIGQ9Ik05IDE4YzIuNCAwIDQuNS0uOCA2LTIuMmwtMy0yLjJhNS40IDUuNCAwIDAgMS04LTIuOUgxVjEzYTkgOSAwIDAgMCA4IDV6IiBmaWxsPSIjMzRBODUzIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNNCAxMC43YTUuNCA1LjQgMCAwIDEgMC0zLjRWNUgxYTkgOSAwIDAgMCAwIDhsMy0yLjN6IiBmaWxsPSIjRkJCQzA1IiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNOSAzLjZjMS4zIDAgMi41LjQgMy40IDEuM0wxNSAyLjNBOSA5IDAgMCAwIDEgNWwzIDIuNGE1LjQgNS40IDAgMCAxIDUtMy43eiIgZmlsbD0iI0VBNDMzNSIgZmlsbC1ydWxlPSJub256ZXJvIi8+PHBhdGggZD0iTTAgMGgxOHYxOEgweiIvPjwvZz48L3N2Zz4=');
		background-repeat: no-repeat;
		background-position: 12px center;
		padding: 12px 16px 12px 42px;
		font-size: 14px;
		font-weight: 500;
		color: #757575;
		background-color: var(--white);
		border-radius: 3px;
		border: none;
		box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 1px 1px rgba(0, 0, 0, 0.25);
		transition: 0.3s;
		cursor: pointer;
		width: var(--content-width);
	}

	.login-google:hover {
		box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.04), 0 2px 4px rgba(0, 0, 0, 0.25);
	}
</style>
