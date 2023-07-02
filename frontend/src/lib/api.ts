const API_BASE = "https://redmac.pythonanywhere.com/api";
export function apiUrl(path: string) {
    return `${API_BASE}${path}`;
}