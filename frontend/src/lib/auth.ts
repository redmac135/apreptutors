import firebase from "firebase/compat/app";
import firebaseApp, { firebaseUser, type UserProfile } from "../routes/store";
import { get } from "svelte/store";
import { getAuth, signInWithPopup } from "firebase/auth";

export async function loginWithGoogle() {
    const provider = new firebase.auth.GoogleAuthProvider();
    const auth = getAuth(get(firebaseApp));
    await signInWithPopup(auth, provider).then(async (result) => {
        const user = result.user;
        const  profile: UserProfile = {
            loggedIn: true,
            token: await user.getIdToken(),
            displayName: user.displayName ?? "",
            photoUrl: user.photoURL ?? ""
        };
        firebaseUser.set(profile);
        console.log("login successful");
    }).catch((error) => {
        console.log(error);
    });
}