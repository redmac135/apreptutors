<script lang="ts">
	import { getAuth } from 'firebase/auth';
	import { get } from 'svelte/store';
	import firebaseApp from '../../store';
	import { apiUrl } from '$lib/api';

	// from +page.ts
	export let data: any;
	const { subjects, locations } = data;

	const app = get(firebaseApp);
	// @ts-ignore
	const auth = getAuth(app);
	$: loggedIn = auth.currentUser ? true : false;

	const checkLoggedIn = () => {
		// @ts-ignore
		const auth = getAuth(app);
		if (auth.currentUser) {
			return true;
		}
		return false;
	};

	const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
	const timeslots = [
		'9:00 AM - 10:30 AM',
		'10:30 AM - 12:00 PM',
		'12:00 PM - 1:30 PM',
		'1:30 PM - 3:00 PM',
		'3:00 PM - 4:30 PM',
		'4:30 PM - 6:00 PM',
		'6:00 PM - 7:30 PM',
		'7:30 PM - 9:00 PM',
		'9:00 PM - 10:30 PM'
	];

	type FormData = {
		verification: string;
		subjects: number[];
		locations: number[];
		timeslots: {
			monday: number[];
			tuesday: number[];
			wednesday: number[];
			thursday: number[];
			friday: number[];
			saturday: number[];
			sunday: number[];
		};
	};

	function handleSubmit(e: any) {
		const ACTION_URL = e.target.action;
		const FORM_DATA = new FormData(e.target);
		let data: FormData = {
			verification: '',
			subjects: [],
			locations: [],
			timeslots: {
				monday: [],
				tuesday: [],
				wednesday: [],
				thursday: [],
				friday: [],
				saturday: [],
				sunday: []
			}
		};

		for (const field of FORM_DATA) {
			let [key, value] = field;
			if (key === 'subject') {
				data.subjects.push(parseInt(value.toString()));
			} else if (key === 'location') {
				data.locations.push(parseInt(value.toString()));
			} else if (key === 'timeslot') {
				let [day, timeslot] = value.toString().split('-');
				// @ts-ignore
				data.timeslots[day.toLowerCase()].push(parseInt(timeslot));
			} else if (key === 'verification') {
				data.verification = value.toString();
			} // else?
		}

		// check if any fields are empty
		if (
			data.subjects.length === 0 ||
			data.locations.length === 0 ||
			!Object.values(data.timeslots).some((day) => day.length > 0)
		) {
			alert('Please fill out all fields.');
			return;
		}

		// @ts-ignore
		const auth = getAuth(app);
		const user = auth.currentUser;
		if (!user) {
			alert('Please log in first.');
			return;
		}
		user.getIdToken().then((token) => {
			fetch(ACTION_URL, {
				method: 'POST',
				body: JSON.stringify(data),
				headers: {
					Authorization: token
				}
			})
				.then((res) => {
					if (res.status === 200) {
						// TODO: change this redirect
						window.location.href = '/comingsoon';
					} else {
						alert('Something went wrong. Please try again.');
					}
				})
				.catch((err) => {
					console.error(err);
					alert('Something went wrong. Please try again.');
				});
		});
	}
</script>

<div class="container">
	<form action={apiUrl("/createtutor/")} on:submit|preventDefault={handleSubmit}>
		<h1>Sign up to tutor with aPrep Tutors</h1>
		{#if !loggedIn}
			<p class="warning">
				You are not logged in. Please <a class="login" href="/login">log in</a> before continuing.
			</p>
		{:else}
			<p>Please answer the following questions so we can best pair you with suitable students.</p>

			<div class="form-section">
				<input type="text" name="verification" placeholder="Verification code" required />
				<p>Didn't get a code? Email info@apreptutors.ca!</p>
			</div>

			<div class="divider" />

			<div class="form-section">
				<h2>What courses can you teach?</h2>
				{#each subjects as { pk, name, type }}
					<div class="select">
						<input type="checkbox" name="subject" value={pk.toString()} id={`subject${pk}`} />
						<label for={`subject${pk}`}>{`${name} ${type}`}</label>
					</div>
				{/each}
			</div>

			<div class="divider" />

			<div class="form-section">
				<h2>What location can you teach at?</h2>
				{#each locations as { pk, name, address }}
					<div class="select">
						<input type="checkbox" name="location" value={pk.toString()} id={`location${pk}`} />
						<label for={`location${pk}`}>
							{name}
							<a class="maps-link" href={address} title={`View ${name} on Google Maps`}>
								<svg
									class="link-icon"
									xmlns="http://www.w3.org/2000/svg"
									height="1em"
									viewBox="0 0 512 512"
								>
									<path
										d="M320 0c-17.7 0-32 14.3-32 32s14.3 32 32 32h82.7L201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L448 109.3V192c0 17.7 14.3 32 32 32s32-14.3 32-32V32c0-17.7-14.3-32-32-32H320zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z"
									/>
								</svg>
							</a>
						</label>
					</div>
				{/each}
			</div>

			<div class="divider" />

			<div class="form-section table-container">
				<h2>At what times are you available?</h2>
				<table id="time-selection">
					<tr>
						<th />
						{#each days as day}
							<th>{day}</th>
						{/each}
					</tr>
					{#each timeslots as tslot, i}
						<tr>
							<th>{tslot}</th>
							{#each days as day}
								<td><input type="checkbox" name="timeslot" value={`${day}-${i}`} /></td>
							{/each}
						</tr>
					{/each}
				</table>
			</div>

			<input type="submit" value="Submit" />
		{/if}
	</form>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
	}

	form {
		background-color: var(--beige);
		padding: 1.5rem;
		margin: 2rem;
		border-radius: 0.3rem;
		box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
	}

	h1 {
		font-size: 2rem;
	}

	p {
		font-size: 1.2rem;
		margin: 0.5rem 0;
	}

	.warning {
		color: red;
	}

	.login {
		color: red;
	}

	.divider {
		width: 100%;
		height: 4px;
		background-color: var(--white);
		margin: 1rem 0;
		border-radius: 99rem;
	}

	h2 {
		font-size: 1.5rem;
		font-weight: bold;
		margin-bottom: 1rem;
	}

	.form-section {
		display: flex;
		flex-direction: column;
		margin-bottom: 2rem;
	}

	/* verfication code */
	input[type='text'] {
		width: 100%;
		height: 2rem;
		font-size: 1.2rem;
		padding: 0.5rem;
		border-radius: 0.3rem;
		border: 1px solid var(--dark-blue);
		background-color: var(--white);
		max-width: 25rem;
		margin: 0.5rem 0;
	}

	/* first two questions */
	.select {
		margin-left: 0.5rem;
		margin-top: 0.1rem;
	}

	input {
		margin-right: 1rem;
	}

	label {
		font-size: 1.2rem;
	}

	.maps-link {
		align-self: center;
	}

	.link-icon {
		width: 0.8rem;
		height: 0.8rem;
		margin-left: 0.3rem;
	}

	/* third question */
	.table-container {
		overflow-x: auto;
	}

	#time-selection {
		width: 100%;
		border-collapse: collapse;
	}

	tr:first-child {
		background-color: var(--light-blue);
	}

	tr:nth-child(even) {
		background-color: var(--white);
	}

	th {
		padding: 0.5rem 1rem;
		font-weight: bold;
	}

	td {
		padding: 0.5rem 1rem;
		text-align: center;
	}

	@media (min-width: 800px) {
		form {
			margin: 2rem 10rem;
		}
		th {
			font-size: 1.2rem;
		}
	}

	/* submit button */
	input[type='submit'] {
		display: block;
		background-color: var(--dark-blue);
		color: var(--white);
		border: none;
		border-radius: 0.3rem;
		padding: 1rem 1.5rem;
		font-size: 1.5rem;
		font-weight: bold;
		cursor: pointer;
		transition: background-color 0.2s ease-in-out;
		margin: auto;
	}

	input[type='submit']:hover {
		background-color: var(--light-blue);
	}
</style>
