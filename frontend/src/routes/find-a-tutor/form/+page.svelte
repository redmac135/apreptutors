<script lang="ts">
	import type { SubjectTimeslot, Timeslot } from '$lib/types';
	import { loginWithGoogle } from '$lib/auth';
	import { firebaseUser } from '../../store';
	import { apiUrl } from '$lib/api';
	import { goto } from '$app/navigation';

	export let data: any;
	const { subjects, locations, subjectTimeslots } = data;
	const num_students_options = [1,3,4]

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

	function hasCommonElement(s1: Set<number>, s2: Set<number>): boolean {
		for (let e of s1) {
			if (s2.has(e)) return true;
		}
		return false;
	}

	function getTimeslotIndex(day: string, timeslot: string) {
		let d = {
			MON: 0,
			TUE: 1,
			WED: 2,
			THU: 3,
			FRI: 4,
			SAT: 5,
			SUN: 6
		}[day];
		let t = {
			'09:00:00': 0,
			'10:30:00': 1,
			'12:00:00': 2,
			'13:30:00': 3,
			'15:00:00': 4,
			'16:30:00': 5,
			'18:00:00': 6,
			'19:30:00': 7,
			'21:00:00': 8
		}[timeslot];

		if (d === undefined || t === undefined) {
			return -1;
		}
		return t * days.length + d;
	}

	const MAX_SELECTION = 2;
	let selectedSubject = -1;
	let selectedLocation = -1;
	let num_students = -1

	let timeslotAvailable = Array<boolean>(days.length * timeslots.length).fill(false);
	let checked = new Set<number>();
	let timeslotChecked = Array<boolean>(days.length * timeslots.length).fill(false);
	let timeslotInstructors = Array<Set<number>>(days.length * timeslots.length);
	for (let i = 0; i < timeslotInstructors.length; i++) {
		// .fill is shallow copy
		timeslotInstructors[i] = new Set<number>();
	}

	// note:
	// must use arr = arr.fill(val)
	// instead of arr.fill(val)
	// because svelte detects changes from assignment
	function updateBySubject() {
		if (selectedSubject === -1 || selectedLocation === -1) {
			timeslotAvailable = timeslotAvailable.fill(false);
			timeslotChecked = timeslotChecked.fill(false);
			return;
		} else if (selectedSubject > subjects.length || selectedLocation > locations.length) {
			// uncommon case
			timeslotAvailable = timeslotAvailable.fill(false);
			timeslotChecked = timeslotChecked.fill(false);
			return;
		}

		let subjectData: SubjectTimeslot = subjectTimeslots.find(
			(s: SubjectTimeslot) => s.subjectId === selectedSubject
		);
		let validLocationTimeslots = subjectData.timeslots.filter((t: Timeslot) => {
			return t.locations.includes(selectedLocation);
		});
		console.log(validLocationTimeslots);

		timeslotAvailable = timeslotAvailable.fill(false);
		timeslotInstructors.forEach((s) => s.clear());
		checked.clear();
		timeslotChecked = timeslotChecked.fill(false);
		for (let t of validLocationTimeslots) {
			let index = getTimeslotIndex(t.weekday, t.start_time);
			if (index === -1) continue;
			timeslotAvailable[index] = true;
			timeslotInstructors[index].add(t.instructor.pk);
		}
	}

	function updateFromSelectedInstructors() {
		let instructorsUnion = new Set<number>();
		for (let i of checked) {
			for (let j of timeslotInstructors[i]) {
				instructorsUnion.add(j);
			}
		}
		timeslotAvailable.forEach((avail, i) => {
			if (timeslotInstructors[i].size === 0) return;
			timeslotAvailable[i] = hasCommonElement(timeslotInstructors[i], instructorsUnion);
		});
	}
	function updateByInstructor(e: Event) {
		let target = e.target as HTMLInputElement;
		let index = parseInt(target.id.split('-')[1]);
		if (target.checked) {
			// add associated instructors to selectedInstructors
			// then update timeslotAvailable
			checked.add(index);
			if (checked.size >= MAX_SELECTION) {
				timeslotAvailable.forEach((v, i) => {
					timeslotAvailable[i] = checked.has(i);
				});
				return;
			}
		} else {
			// remove associated instructors from selectedInstructors
			// then update timeslotAvailable
			checked.delete(index);
			if (checked.size === 0) {
				updateBySubject();
				return;
			}
		}
		updateFromSelectedInstructors();
	}

	function handleSubmit(e: any) {
		const ACTION_URL = e.target.action;
		const FORM_DATA = new FormData(e.target);
		let data: FormData = {
			subject: '',
			location: '',
			num_students: '',
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
				data.subject = parseInt(value.toString());
			} else if (key === 'location') {
				data.location = parseInt(value.toString());
			} else if (key === 'num_students') {
				data.num_students = parseInt(value.toString());
			} else if (key === 'timeslot') {
				let [day, timeslot] = value.toString().split('-');
				// @ts-ignore
				data.timeslots[day.toLowerCase()].push(parseInt(timeslot));
			}
		}

		// check if any fields are empty
		if (
			data.subject === '' ||
			data.location === '' ||
			data.num_students === '' ||
			!Object.values(data.timeslots).some((day) => day.length > 0)
		) {
			alert('Please fill out all fields.');
			return;
		}

		fetch(ACTION_URL, {
			method: 'POST',
			body: JSON.stringify(data),
			headers: {
				Authorization: $firebaseUser.token
			}
		})
			.then((res) => {
				if (res.status === 200) {
					// TODO: change this redirect to /home
					goto('/find-a-tutor/success');
				} else if (res.status === 401) {
					loginWithGoogle();
				} else {
					alert('Something went wrong. Please try again.');
				}
			})
			.catch((err) => {
				console.error(err);
				alert('Something went wrong. Please try again.');
			});
	}
</script>

<form action={apiUrl('/createlesson/')} on:submit|preventDefault={handleSubmit}>
	<h1>Find a Tutor</h1>
	{#if !$firebaseUser.loggedIn}
		<p class="warning">
			You are not logged in. Please <a class="login" href="/login?next=find-a-tutor/form"
				>log in</a
			> before continuing.
		</p>
	{:else}
		<p>To register for your first FREE TRIAL lesson at the library closest to you, please enter your desired subject and library location. This information will allow us to automatically match you to one of our experienced IB tutors!</p>

		<div class="form-section">
			<h2>What do you want to learn?</h2>
			<select name="subject" id="subject" bind:value={selectedSubject} on:change={updateBySubject}>
				<option value={-1}>Select a subject</option>
				{#each subjects as { pk, name, type }}
					<option value={pk}>{`${name} ${type}`}</option>
				{/each}
			</select>
		</div>

		<div class="divider" />

		<div class="form-section">
			<h2>Where should we meet?</h2>
			<select
				name="location"
				id="location"
				bind:value={selectedLocation}
				on:change={updateBySubject}
			>
				<option value={-1}>Select a location</option>
				{#each locations as { pk, name, address }}
					<option value={pk}>{name}</option>
				{/each}
			</select>
		</div>

		<div class="divider" />

		<div class="form-section">
			<h2>How many students?</h2>
			<p>If you are registering for a GROUP, please indicate the number of students you wish to enroll. Please note that only ONE person from your group is registering for your session. Group lessons are $20/hour while individual 1-on-1 lessons are $50/hour.</p>
			<select
				name="num_students"
				id="num_students"
				bind:value={num_students}
			>
				<option value={-1}>Select number of students</option>
				{#each num_students_options as num}
					<option value={num}>{num}</option>
				{/each}
			</select>
		</div>


		<div class="divider" />

		<div class="form-section">
			<h2>Pick a time</h2>
			<p>When selecting times in the areas listed below, <strong>choose ONLY 1 timeslot for weekly lessons or 2 timeslots for twice-weekly lessons</strong>. 1 class a week will allow students to slowly learn the course throughout the summer while 2 classes a week will allow students the opportunity to learn the entire IB course in the span of the summer. The time slots are coloured RED for unavailable and BLUE for available times.</p>
			<table id="time-selection">
				<tr>
					<th />
					{#each days as day}
						<th>{day}</th>
					{/each}
				</tr>
				{#each timeslots as tslot, t}
					<tr>
						<th>{tslot}</th>
						{#each days as day, d}
							<td>
								<input
									disabled={!timeslotAvailable[t * days.length + d]}
									type="checkbox"
									name="timeslot"
									class="timeslot-checkbox"
									value={`${day}-${t}`}
									id={`timeslot-${t * days.length + d}`}
									on:change={updateByInstructor}
									bind:checked={timeslotChecked[t * days.length + d]}
								/>
								<label for={`timeslot-${t * days.length + d}`} class="timeslot-option" />
							</td>
						{/each}
					</tr>
				{/each}
			</table>
		</div>

		<input type="submit" value="Submit" />
	{/if}
</form>

<style>
	form {
		background-color: var(--beige);
		padding: 1.5rem;
		margin: 2rem;
		border-radius: 0.3rem;
		box-shadow: 0 0 6px rgba(0, 0, 0, 0.2);
	}

	.timeslot-option {
		display: block;
		height: 100%;
		width: 100%;
		padding: 0.75rem;
		background-color: var(--light-blue);
		border-radius: 5%;
		transition: all 200ms;
	}

	.timeslot-checkbox:checked + label.timeslot-option {
		scale: 0.9;
		background-color: blue;
	}

	.timeslot-checkbox {
		display: none;
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
		overflow: auto;
	}

	select {
		font-size: 1.2rem;
		padding: 0.5rem;
		border-radius: 0.3rem;
		border: 1px solid var(--black);
		background-color: var(--white);
	}

	table {
		min-width: 80rem;
		table-layout: fixed;
		overflow-x: auto;
		border-collapse: collapse;
	}

	.timeslot-option {
		display: block;
		height: 100%;
		width: 100%;
		padding: 0.75rem;
		background-color: var(--light-blue);
		border-radius: 5%;
		transition: all 200ms;
	}

	.timeslot-checkbox:disabled + label.timeslot-option {
		background-color: lightcoral;
	}

	.timeslot-checkbox:checked + label.timeslot-option {
		scale: 0.9;
		background-color: blue;
	}

	.timeslot-checkbox {
		display: none;
	}

	tr:first-child {
		background-color: var(--light-blue);
	}

	tr:nth-child(even) {
		background-color: var(--white);
	}

	th {
		width: 8.5rem;
		padding: 0.25rem 1rem;
		font-weight: bold;
	}

	td {
		padding: 0.25rem;
		text-align: center;
	}

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
