<script lang="ts">
	export let pause: Boolean = false;
</script>

<div
	class="circle"
	class:pause-animation={pause}
/>

<style>
	.circle {
		height: 5rem;
		width: 5rem;
		border-color: var(--dark-blue) transparent var(--dark-blue) var(--dark-blue);
		border-width: calc(var(--size) / 15);
		border-style: solid;
		border-image: initial;
		border-radius: 50%;
		animation: 0.75s linear 0s infinite normal none running rotate;
	}
	.pause-animation {
		animation-play-state: paused;
	}
	@keyframes rotate {
		0% {
			transform: rotate(0);
		}
		100% {
			transform: rotate(360deg);
		}
	}
</style>