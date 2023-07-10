<script lang="ts">
	import { onMount } from 'svelte';
	import Card from '$lib/timer/Card.svelte';

	let time = {
		days: 0,
		hours: 0,
		minutes: 0,
		seconds: 0
	};

	const handleTick = () => {
		const currentDate = new Date();
		const gap = 1688479200000 - currentDate.getTime(); // Number is epoch time for June 30th 4pm

		const getDays = Math.floor(gap / (1000 * 60 * 60 * 24));
		const getHours = Math.floor((gap / (1000 * 60 * 60)) % 24);
		const getMinutes = Math.floor((gap / 1000 / 60) % 60);
		const getSeconds = Math.floor((gap / 1000) % 60);

		time.days = getDays;
		time.hours = getHours;
		time.minutes = getMinutes;
		time.seconds = getSeconds;
	};

	onMount(() => {
		handleTick();
	});
</script>

<main>
	<div class="title">
		<h1>aPrep Tutors</h1>
		<h2>is coming soon</h2>
	</div>
	<div class="countdown">
		<Card callback={handleTick} name="Days" number={time.days} />
		<Card callback={handleTick} name="Hours" number={time.hours} />
		<Card callback={handleTick} name="Minutes" number={time.minutes} />
		<Card callback={handleTick} name="Seconds" number={time.seconds} />
	</div>
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		justify-content: center;
		flex: 0.75;
		row-gap: 7rem;
		height: 80vh;
		background-image: url('/images/sloganbackground.jpg');
		background-position: center;
		background-size: cover;
		background-attachment: fixed;
	}
	.title {
		display: flex;
		justify-content: center;
		flex-direction: column;
		align-items: center;
	}
	h1 {
		font-size: 3rem;
		color: black;
		letter-spacing: 5px;
		font-weight: 600;
	}
	h2 {
		font-weight: 400;
	}
	.countdown {
		display: flex;
		justify-content: center;
		gap: 0.5rem;
	}

	@media (min-width: 768px) {
		h1 {
			font-size: 4rem;
			letter-spacing: 9px;
		}
		.countdown {
			gap: 5rem 2.5rem;
			flex-wrap: wrap;
		}
	}
</style>
