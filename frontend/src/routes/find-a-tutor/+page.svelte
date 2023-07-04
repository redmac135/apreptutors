<script lang="ts">
	import type { SubjectTimeslot, Timeslot } from '$lib/types';
	import { firebaseUser } from '../store';

	export let data: any;
	const { subjects, locations, subjectTimeslots } = data;

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
		} else if (selectedSubject >= subjects.length || selectedLocation >= locations.length) {
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
</script>

<form action="">
	<h1>find a ttuuuutor</h1>
	{#if !$firebaseUser.loggedIn}
		<p class="warning">
			You are not logged in. Please <a class="login" href="/login?next=become-a-tutor/form"
				>log in</a
			> before continuing.
		</p>
	{:else}
		<p>answer deez questions</p>

		<div class="form-section">
			<h2>subject</h2>
			<select
				name="subjects"
				id="subjects"
				bind:value={selectedSubject}
				on:change={updateBySubject}
			>
				<option value={-1}>Select a subject</option>
				{#each subjects as { pk, name, type }}
					<option value={pk}>{`${name} ${type}`}</option>
				{/each}
			</select>
		</div>

		<div class="divider" />

		<div class="form-section">
			<h2>location</h2>
			<select
				name="locations"
				id="locations"
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
			<h2>pick a time</h2>
			<p>select {MAX_SELECTION} time</p>
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
	table {
		min-width: 80rem;
		table-layout: fixed;
		overflow-x: auto;
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
</style>
