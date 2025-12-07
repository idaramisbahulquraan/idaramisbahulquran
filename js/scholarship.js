import { db, storage, collection, addDoc, ref, uploadBytes, getDownloadURL } from './firebase-config.js';

const scholarshipForm = document.getElementById('scholarshipForm');
const loadingOverlay = document.getElementById('loadingOverlay');
const successMessage = document.getElementById('successMessage');
const errorMessage = document.getElementById('errorMessage');
const errorText = document.getElementById('errorText');
const submitButton = document.getElementById('submitButton');

if (scholarshipForm) {
    scholarshipForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        setLoading(true);
        hideError();

        try {
            const formData = new FormData(scholarshipForm);
            const data = Object.fromEntries(formData.entries());

            // 1. Upload Images
            let studentImageUrl = '';
            let documentUrl = '';

            const studentImageFile = formData.get('studentImage');
            if (studentImageFile && studentImageFile.name) {
                studentImageUrl = await uploadFile(studentImageFile, 'scholarship_images');
            }

            const documentFile = formData.get('documentFile');
            if (documentFile && documentFile.name) {
                documentUrl = await uploadFile(documentFile, 'scholarship_documents');
            }

            // 2. Prepare Data for Firestore
            const submissionData = {
                ...data,
                studentImage: studentImageUrl,
                documentFile: documentUrl,
                submittedAt: new Date(),
                type: 'scholarship' // Tag as scholarship
            };

            // Remove file objects from data to be saved
            delete submissionData.studentImageFile;
            delete submissionData.documentFileObj;

            // 3. Save to Firestore
            await addDoc(collection(db, "scholarships"), submissionData);

            showSuccess();
            scholarshipForm.reset();
            window.scrollTo(0, 0);

        } catch (err) {
            console.error("Error submitting form:", err);
            let msg = "Failed to submit form. Please check your internet connection and try again.";
            if (err.message && err.message.includes("Cloud Firestore API")) {
                msg = "Configuration Error: The Firestore API is not enabled for this project.";
            } else if (err.code === 'permission-denied') {
                msg = "Permission Denied: Database security rules prevented this submission.";
            }
            showError(msg);
        } finally {
            setLoading(false);
        }
    });
}

async function uploadFile(file, path) {
    const storageRef = ref(storage, `${path}/${Date.now()}_${file.name}`);
    const snapshot = await uploadBytes(storageRef, file);
    return await getDownloadURL(snapshot.ref);
}

function setLoading(isLoading) {
    if (isLoading) {
        loadingOverlay.classList.remove('hidden');
        submitButton.disabled = true;
        submitButton.classList.add('opacity-70', 'cursor-not-allowed');
    } else {
        loadingOverlay.classList.add('hidden');
        submitButton.disabled = false;
        submitButton.classList.remove('opacity-70', 'cursor-not-allowed');
    }
}

function showSuccess() {
    successMessage.classList.remove('hidden');
    scholarshipForm.classList.add('hidden');
}

function showError(msg) {
    errorText.textContent = msg;
    errorMessage.classList.remove('hidden');
    window.scrollTo(0, 0);
}

function hideError() {
    errorMessage.classList.add('hidden');
}

// Reset form handler
window.resetForm = function () {
    successMessage.classList.add('hidden');
    scholarshipForm.classList.remove('hidden');
    scholarshipForm.reset();
}
