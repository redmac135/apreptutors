<script lang="ts">
	import { GoogleAuthProvider, getAuth, signInWithPopup } from 'firebase/auth';
    import { get } from 'svelte/store';
    import firebaseApp from '../store';

    const app = get(firebaseApp);

    const loginWithGoogle = () => {
        const auth = getAuth(app);
        signInWithPopup(auth, new GoogleAuthProvider());
    }
</script>

<button on:click={loginWithGoogle}>Login with Google</button>