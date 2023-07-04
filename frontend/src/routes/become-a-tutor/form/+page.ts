import { getLocations, getSubjects } from "$lib/api";

export const load = async ({ fetch }) => {
    const subjects = await getSubjects(fetch);
    const locations = await getLocations(fetch);
    return {
        subjects,
        locations
    };
}