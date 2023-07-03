<script lang="ts">
	import type { SubjectTimeslot, Timeslot } from '$lib/types';

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
		return d * timeslots.length + t;
	}

	let selectedSubject = -1;
	let selectedLocation = -1;

	let timeslotAvailable = Array<boolean>(days.length * timeslots.length).fill(false);
	function updateTimeslots() {
		if (selectedSubject === -1 || selectedLocation === -1) {
			timeslotAvailable.fill(false);
			return;
		} else if (selectedSubject >= subjects.length || selectedLocation >= locations.length) {
			// uncommon case
			timeslotAvailable.fill(false);
			return;
		}

		let subjectData: SubjectTimeslot = subjectTimeslots.find(
			(s: SubjectTimeslot) => s.subjectId === selectedSubject
		);
		let validLocationTimeslots = subjectData.timeslots.filter((t: Timeslot) => {
			return t.locations.includes(selectedLocation);
		});

		console.log(validLocationTimeslots)

		timeslotAvailable.fill(false);
		for (let t of validLocationTimeslots) {
			let index = getTimeslotIndex(t.weekday, t.start_time);
			if (index !== -1) {
				timeslotAvailable[index] = true;
			}
		}
	}
</script>

<form action="">
	<h1>find a ttuuuutor</h1>
	<p>answer deez questions</p>

	<div class="form-section">
		<h2>subject</h2>
		<select name="subjects" id="subjects" bind:value={selectedSubject} on:change={updateTimeslots}>
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
			on:change={updateTimeslots}
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
		<p>select 2 time</p>
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
					{#each days as day, j}
						<td>
							<input
								disabled={!timeslotAvailable[i * days.length + j]}
								type="checkbox"
								name="timeslot"
								class="timeslot-checkbox"
								value={`${day}-${i}`}
								id={`${day}-${i}`}
							/>
							<label for={`${day}-${i}`} class="timeslot-option" />
						</td>
					{/each}
				</tr>
			{/each}
		</table>
	</div>
</form>
