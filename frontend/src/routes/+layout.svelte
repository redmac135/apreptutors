<script lang="ts">
	import Navbar from '../lib/Navbar.svelte';
	import Footer from '../lib/Footer.svelte';
	import InfoBar from '../lib/InfoBar.svelte';

	// should this be before or after the components
	import '../app.css';
</script>

<Navbar />
<InfoBar />
<slot />
<Footer />