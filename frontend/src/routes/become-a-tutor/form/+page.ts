import { getLocations, getSubjects } from "$lib/api";

export const load = async () => {
    const subjects = await getSubjects();
    const locations = await getLocations();
    return {
        subjects,
        locations
    };
}