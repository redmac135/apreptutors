<script lang="ts">
	import { loading } from "$lib/loading";
	import LoadingCircle from "$lib/loadingCircle.svelte";
	import { firebaseUser } from "../store";
</script>

{#if $loading}
<div class="loading-wrapper">
	<LoadingCircle />
</div>
{:else}
	{#if !$firebaseUser.loggedIn}
		<div class="warning-wrapper">
			<p class="warning">
				You are not logged in. Please <a class="login" href="/login?next=become-a-tutor/form"
					>log in</a
				> before continuing.
			</p>
		</div>
	{:else}
		<div class="container">
			<h1>Tutor with aPrep Tutors</h1>
			<p>
				Existing tutors: Log in with your designated authorization code to fill in information regarding
				the subjects and times you're willing to tutor!
			</p>

			<p>
				Interested tutors: Please
				<a id="email" href="mailto:info@apreptutors.ca" target="_blank" rel="noopener noreferrer">
					email us
				</a>
				for further inquiries!
			</p>
			<a id="a-button" href="/become-a-tutor/form">Get started</a>
		</div>
	{/if}
{/if}

<style>
	.loading-wrapper {
		display: flex;
        align-items: center;
        justify-content: center;
        height: 80vh;
	}

	.warning-wrapper {
		background-color: var(--beige);
		padding: 1.5rem;
		margin: 2rem;
		border-radius: 0.3rem;
		box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
    }

	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		text-align: center;
		padding: 4rem;
		max-width: 40rem;
		margin: 0 auto;
	}

	p {
		font-size: 1.2rem;
		margin: 0.5rem 0;
	}

	#a-button {
		background-color: var(--dark-blue);
		border: none;
		border-radius: 0.3rem;
		padding: 1rem 1.5rem;
		cursor: pointer;
		transition: background-color 0.2s ease-in-out;
		margin-top: 1rem;
		color: var(--white);
		text-decoration: none;
		font-size: 1.5rem;
		font-weight: bold;
	}

	#a-button:hover {
		background-color: var(--light-blue);
	}

	#email {
		color: var(--dark-blue);
	}
</style>
