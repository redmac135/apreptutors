<script lang="ts">
	// webinar time in unix is 1689984000 -> 1689989400
	const WEBINAR_START = 1689984000;
	const WEBINAR_END = 1689989400;

	function pad2(num: number): string {
		return String(num).padStart(2, '0');
	}
	function webinarLive(): string {
		const now = Math.floor(Date.now() / 1000);
		if (now < WEBINAR_START) {
			const timeLeft = WEBINAR_START - now;
			const hours = Math.floor(timeLeft / 3600);
			const minutes = Math.floor((timeLeft % 3600) / 60);
			const seconds = timeLeft % 60;
			return `starting in ${hours}:${pad2(minutes)}:${pad2(seconds)}!`;
		} else if (now < WEBINAR_END) {
			return 'happening now!';
		} else {
			return 'over! Watch the recording';
		}
	}

	let webinarText = webinarLive();
	setInterval(() => {
		webinarText = webinarLive();
	}, 1000);
</script>

<a class="wrapper" href="/webinar">
	<svg
		xmlns="http://www.w3.org/2000/svg"
		class="icon"
		x="0px"
		y="0px"
		width="128"
		height="128"
		viewBox="0 0 24 24"
		fill="currentColor"
	>
		<path
			d="M 12 2 C 11.172 2 10.5 2.672 10.5 3.5 L 10.5 4.1953125 C 7.9131836 4.862095 6 7.2048001 6 10 L 6 16 L 4.4648438 17.15625 L 4.4628906 17.15625 A 1 1 0 0 0 4 18 A 1 1 0 0 0 5 19 L 12 19 L 19 19 A 1 1 0 0 0 20 18 A 1 1 0 0 0 19.537109 17.15625 L 18 16 L 18 10 C 18 7.2048001 16.086816 4.862095 13.5 4.1953125 L 13.5 3.5 C 13.5 2.672 12.828 2 12 2 z M 10 20 C 10 21.1 10.9 22 12 22 C 13.1 22 14 21.1 14 20 L 10 20 z"
		/>
	</svg>
	<p><i>The IB Pespective</i> Webinar is {webinarText}</p>
	<p class="ending">Learn More &rarr;</p>
</a>

<style>
	.wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		background-color: var(--beige);
		padding: 1rem;

		text-decoration: none;
		color: black;
	}

	.icon {
		margin-right: 0.5rem;
		height: 1.25rem;
		width: 1.25rem;
		color: var(--dark-blue);
	}

	.ending {
		padding-left: 0.5rem;
		font-weight: bold;
	}
</style>
