<script lang="ts">
	import Navbar from '../lib/Navbar.svelte';
	import Footer from '../lib/Footer.svelte';
	import InfoBar from '../lib/InfoBar.svelte';

	// should this be before or after the components
	import '../app.css';
</script>

<svelte:head>
	<title>aPrep Tutors</title>
</svelte:head>

<Navbar />
<InfoBar />
<slot />
<Footer />
