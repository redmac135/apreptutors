import type firebase from 'firebase/compat/app';
import { writable, type Writable } from "svelte/store";
import { persisted } from 'svelte-local-storage-store';

const firebaseApp: Writable<firebase.app.App> = writable();

export type UserProfile = {
    loggedIn: boolean;
    token: string;
    displayName: string;
    photoUrl: string | null;
}
export const firebaseUser: Writable<UserProfile> = persisted("firebaseUser", {
    loggedIn: false,
    token: "",
    displayName: "",
    photoUrl: ""
});

export default firebaseApp;