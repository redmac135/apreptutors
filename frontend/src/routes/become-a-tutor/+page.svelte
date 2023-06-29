<script lang="ts">
	import { GoogleAuthProvider, getAuth, signInWithPopup } from 'firebase/auth';
	import { get } from 'svelte/store';
	import firebaseApp from '../store';
	import { onMount } from 'svelte';

	const app = get(firebaseApp);

	const loginWithGoogle = () => {
		// @ts-ignore
		const auth = getAuth(app);
		signInWithPopup(auth, new GoogleAuthProvider());
	};

	const checkLoggedIn = () => {
		// @ts-ignore
		const auth = getAuth(app);
		if (auth.currentUser) {
			return true;
		}
		return false;
	};

	onMount(() => {
        if (!checkLoggedIn()) {
            loginWithGoogle();
        }
    });
</script>
