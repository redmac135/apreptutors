import { apiUrl } from "$lib/api";

type Subject = {
    pk: number;
    type: string;
    name: string;
}
async function getSubjects(): Promise<Subject[]> {
    const API_URL = apiUrl("/qualifications");
    const response = await fetch(API_URL);
    return await response.json();
}

type Location = {
    pk: number;
    name: string;
    address: string;
}
async function getLocations(): Promise<Location[]> {
    const API_URL = apiUrl("/locations");
    const response = await fetch(API_URL);
    return await response.json();
}

export const load = async () => {
    const subjects = await getSubjects();
    const locations = await getLocations();
    return {
        subjects,
        locations
    };
}