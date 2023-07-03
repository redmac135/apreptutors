const API_BASE = "https://redmac.pythonanywhere.com/api";
export function apiUrl(path: string) {
    return `${API_BASE}${path}`;
}

type Subject = {
    pk: number;
    type: string;
    name: string;
}
export async function getSubjects(): Promise<Subject[]> {
    const API_URL = apiUrl("/qualifications");
    const response = await fetch(API_URL);
    return await response.json();
}

type Location = {
    pk: number;
    name: string;
    address: string;
}
export async function getLocations(): Promise<Location[]> {
    const API_URL = apiUrl("/locations");
    const response = await fetch(API_URL);
    return await response.json();
}
