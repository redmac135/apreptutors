export const prerender = true;

// firebase config
import firebaseApp from "./store";
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';

const firebaseConfig = {
    apiKey: 'AIzaSyA-rItlIc6ZKX5C6Nr_xaYbUV2aW6rOoGg',
    authDomain: 'apreptutors-1ff86.firebaseapp.com',
    projectId: 'apreptutors-1ff86',
    storageBucket: 'apreptutors-1ff86.appspot.com',
    messagingSenderId: '189724914356',
    appId: '1:189724914356:web:83ce912a327d3a9446dde1'
};

firebaseApp.set(firebase.initializeApp(firebaseConfig));