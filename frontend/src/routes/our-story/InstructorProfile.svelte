<script lang="ts">
	import { DEFAULT_PHOTO } from './founders';

	export let name: string,
		position: string,
		specialties: string[],
		university: string,
		photo: string | undefined;
</script>

<div class="container">
	{#if photo}
		<img src={photo} alt={`headshot of ${name}`} />
	{:else}
		<img src={DEFAULT_PHOTO} alt="default user profile" />
	{/if}
	<div class="description">
		<h2>{name}</h2>
		<p class="position">{position}</p>
		<p class="uni">{university}</p>
		<ul>
			{#each specialties as specialty}
				<li>{specialty}</li>
			{/each}
		</ul>
	</div>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 2rem;
		border-radius: 1rem;
		width: 18rem;
		height: 27rem;
		border: 5px solid var(--beige);
		box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2);
	}

	img {
        height: 9rem;
        width: auto;
        border-radius: 15%;
		margin-bottom: 0.3rem;
		box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
		border-bottom: 3px solid var(--dark-blue);
		border-right: 3px solid var(--dark-blue);
	}

	.description {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		text-align: center;
	}

	.description * {
		margin-top: 0.4rem;
	}

	h2 {
		font-size: 1.7rem;
		font-weight: bold;
	}

	.position {
		font-size: 1rem;
	}

	.uni {
		font-style: italic;
		font-size: 0.9rem;
	}

	ul {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}

	ul li {
		border-radius: 0.3rem;
		padding: 0.3rem 0.5rem;
		font-size: 0.8rem;
		background-color: var(--beige);
		list-style: none;
		margin: 0.2rem;
		box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
	}
</style>
