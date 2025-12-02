// Firebase Configuration
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getFirestore, collection, addDoc, getDocs, doc, deleteDoc, updateDoc } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-lite.js";
import { getStorage, ref, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-storage.js";

const firebaseConfig = {
    apiKey: "AIzaSyB0oPTLEYuNiWCx5s9GmZzGzyH1z-HXwb8",
    authDomain: "onlineadmission-f85c6.firebaseapp.com",
    projectId: "onlineadmission-f85c6",
    storageBucket: "onlineadmission-f85c6.firebasestorage.app",
    messagingSenderId: "996707362986",
    appId: "1:996707362986:web:fea98a07bea032ff7e48d3",
    measurementId: "G-6H910NXDM1"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const storage = getStorage(app);

export { db, storage, collection, addDoc, getDocs, doc, deleteDoc, updateDoc, ref, uploadBytes, getDownloadURL };
