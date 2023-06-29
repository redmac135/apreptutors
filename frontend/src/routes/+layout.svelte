<script lang="ts">
	import { onMount } from 'svelte';
	import firebaseApp from './store';
	import Navbar from '../lib/Navbar.svelte';
	import Footer from '../lib/Footer.svelte';
	import InfoBar from '../lib/InfoBar.svelte';

	// should this be before or after the components
	import '../app.css';

	// firebase config
	import firebase from 'firebase/compat/app';
	import 'firebase/compat/auth';
	onMount(() => {
		const firebaseConfig = {
			apiKey: 'AIzaSyA-rItlIc6ZKX5C6Nr_xaYbUV2aW6rOoGg',
			authDomain: 'apreptutors-1ff86.firebaseapp.com',
			projectId: 'apreptutors-1ff86',
			storageBucket: 'apreptutors-1ff86.appspot.com',
			messagingSenderId: '189724914356',
			appId: '1:189724914356:web:83ce912a327d3a9446dde1'
		};

		firebaseApp.set(firebase.initializeApp(firebaseConfig));
	});
</script>

<svelte:head>
	<title>aPrep Tutors</title>
</svelte:head>

<Navbar />
<InfoBar />
<slot />
<Footer />
