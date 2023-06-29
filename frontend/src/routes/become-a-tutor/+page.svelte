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

	const subjects = [
		{ id: 1, subject: 'Math AA HL' },
		{ id: 2, subject: 'Chemistry HL' },
		{ id: 3, subject: 'Biology HL' },
		{ id: 4, subject: 'Physics HL' },
		{ id: 5, subject: 'English Literature HL' },
		{ id: 6, subject: 'Economics HL' },
		{ id: 7, subject: 'Math AA SL' },
		{ id: 8, subject: 'Chemistry SL' },
		{ id: 9, subject: 'Biology SL' },
		{ id: 10, subject: 'Physics SL' },
		{ id: 11, subject: 'English Literature SL' },
		{ id: 12, subject: 'French SL' },
		{ id: 13, subject: 'Economics SL' }
	];
	const locations = [
		{ id: 1, name: 'Richmond Green Library', address: 'https://goo.gl/maps/nDAza2zVVGBrfRgcA' },
		{
			id: 2,
			name: 'Central Branch Library - Richmond Hill',
			address: 'https://goo.gl/maps/DboNypwCr1BLfERC7'
		},
		{ id: 3, name: 'Angus Glen CC', address: 'https://goo.gl/maps/RYnqD1B2X5Pgu2yY6' },
		{ id: 4, name: 'Unionville Library', address: 'https://goo.gl/maps/pLn379rV6jN7AGFr8' },
		{ id: 5, name: 'Aaniin CC', address: 'https://goo.gl/maps/PsT6Dvtr2Xd3XiFx8' },
		{ id: 6, name: 'Centennial CC', address: 'https://goo.gl/maps/eCk6fF9Usv7Hig4h8' },
		{ id: 7, name: 'Markham Village Library', address: 'https://goo.gl/maps/axa396HNRXGrZK199' },
		{ id: 8, name: 'Cornell CC', address: 'https://goo.gl/maps/eebd6mHQ9mdb4SZf6' },
		{ id: 9, name: 'Thornhill Village Library', address: 'https://goo.gl/maps/NuJz26cKGE6G295R6' },
		{ id: 10, name: 'Thornhill CC', address: 'https://goo.gl/maps/UaDC4GGQoHQzMiU4A' },
		{ id: 11, name: 'Milliken Mills CC', address: 'https://goo.gl/maps/AmKmLsBnymh8p4YP9' },
		{
			id: 12,
			name: 'North York Central Library',
			address: 'https://goo.gl/maps/45Lw6tJiJzXHSKTb9'
		},
		{ id: 13, name: 'Fairview Library', address: 'https://goo.gl/maps/z7XThQ71vN8iExAXA' }
	];
	const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
	const timeslots = ['Early afternoons (12-4pm)', 'Late afternoons (4-7pm)', 'Evenings (7-10pm)'];
</script>

<form action="POST">
	<div class="form-section">
		<p class="question">What courses can you teach?</p>
		{#each subjects as subject}
			<input type="checkbox" name="subject" value={subject.id.toString()} />
			<label for={subject.id.toString()}>{subject.subject}</label>
		{/each}
	</div>

	<div class="form-section">
		<p class="question">What location can you teach at?</p>
		{#each locations as location}
			<input type="checkbox" name="location" value={location.id.toString()} />
			<label for={location.id.toString()}>
				<a href={location.address}>{location.name}</a>
			</label>
		{/each}
	</div>

	<div class="form-section">
		<p class="question">At what times are you available?</p>
		{#each timeslots as tslot}
			<span>{tslot}</span>
		{/each}
		{#each days as day}
			<span>{day}</span>
			{#each timeslots as tslot}
				<input type="checkbox" name="timeslot" value={day + tslot} />
			{/each}
		{/each}
	</div>
</form>

<style>

</style>
