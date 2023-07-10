import type { Subject, Location, SubjectTimeslot } from "./types";

const API_BASE = "https://redmac.pythonanywhere.com/api";
export function apiUrl(path: string) {
    return `${API_BASE}${path}`;
}

export async function getSubjects(fetch: Function): Promise<Subject[]> {
    const API_URL = apiUrl("/qualifications");
    const response = await fetch(API_URL);
    return await response.json();
}

export async function getLocations(fetch: Function): Promise<Location[]> {
    const API_URL = apiUrl("/locations");
    const response = await fetch(API_URL);
    return await response.json();
}

export async function getAllTimeslots(fetch: Function): Promise<SubjectTimeslot[]> {
    const API_URL = apiUrl("/timeslots/all");
    const response = await fetch(API_URL);
    return await response.json();
}