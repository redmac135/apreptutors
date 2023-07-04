import { getAllTimeslots, getLocations, getSubjects } from "$lib/api";

export const load = async () => {
    const subjects = await getSubjects();
    const locations = await getLocations();
    const subjectTimeslots = await getAllTimeslots();
    return {
        subjects,
        locations,
        subjectTimeslots
    };
}