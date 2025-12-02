import { db, collection, getDocs, doc, deleteDoc, updateDoc } from './firebase-config.js';

const loginSection = document.getElementById('loginSection');
const dashboardSection = document.getElementById('dashboardSection');
const loginForm = document.getElementById('loginForm');
const loginError = document.getElementById('loginError');
const studentsTableBody = document.getElementById('studentsTableBody');
const totalApplications = document.getElementById('totalApplications');
const loadingData = document.getElementById('loadingData');
const dashboardContent = document.getElementById('dashboardContent');

// Edit Modal Elements
const editModal = document.getElementById('editModal');
const editForm = document.getElementById('editForm');
const editStudentId = document.getElementById('editStudentId');
const editStudentName = document.getElementById('editStudentName');
const editFatherName = document.getElementById('editFatherName');
const editAdmissionLevel = document.getElementById('editAdmissionLevel');
const editAdmissionClass = document.getElementById('editAdmissionClass');
const editContactNumber = document.getElementById('editContactNumber');
const editCnic = document.getElementById('editCnic');
const editGender = document.getElementById('editGender');

let studentsData = [];

// Login Handler
if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const username = loginForm.username.value;
        const password = loginForm.password.value;

        if (username === 'admin' && password === 'admin') {
            showDashboard();
        } else {
            loginError.classList.remove('hidden');
        }
    });
}

function showDashboard() {
    loginSection.classList.add('hidden');
    dashboardSection.classList.remove('hidden');
    fetchData();
}

async function fetchData() {
    try {
        const querySnapshot = await getDocs(collection(db, 'admissions'));
        studentsData = querySnapshot.docs.map(doc => {
            const docData = doc.data();
            const submittedDate = docData.submittedAt?.seconds
                ? new Date(docData.submittedAt.seconds * 1000).toLocaleString()
                : 'N/A';
            return { id: doc.id, ...docData, submittedAtFormatted: submittedDate };
        });

        // Sort by newest first
        studentsData.sort((a, b) => (b.submittedAt?.seconds || 0) - (a.submittedAt?.seconds || 0));

        renderTable();
        totalApplications.textContent = `Total Applications: ${studentsData.length}`;
        loadingData.classList.add('hidden');
        dashboardContent.classList.remove('hidden');

    } catch (error) {
        console.error("Error fetching data:", error);
        alert("Error fetching data. Check console for details.");
    }
}

function renderTable() {
    studentsTableBody.innerHTML = '';

    if (studentsData.length === 0) {
        studentsTableBody.innerHTML = '<tr><td colspan="8" class="text-center py-8 text-gray-500">No admission records found.</td></tr>';
        return;
    }

    studentsData.forEach(student => {
        const row = document.createElement('tr');
        row.className = "hover:bg-blue-50 transition-colors border-b border-gray-200";
        row.innerHTML = `
            <td class="px-6 py-4 font-medium text-gray-900">
                <div class="flex items-center">
                    ${student.studentImage ? `<img src="${student.studentImage}" alt="pic" class="w-8 h-8 rounded-full mr-2 object-cover border border-gray-300"/>` : ''}
                    ${student.studentName || '-'}
                </div>
            </td>
            <td class="px-6 py-4">
                <div class="flex flex-col space-y-1">
                    <span class="bg-brand-teal text-white py-1 px-3 rounded-full text-xs w-fit">
                        ${student.admissionLevel || '-'}
                    </span>
                    <span class="text-xs text-gray-500">
                        ${student.admissionClass || '-'}
                    </span>
                </div>
            </td>
            <td class="px-6 py-4">${student.fatherName || '-'}</td>
            <td class="px-6 py-4">${student.contactNumber || '-'}</td>
            <td class="px-6 py-4">${student.cnic || '-'}</td>
            <td class="px-6 py-4 text-gray-500">${student.submittedAtFormatted}</td>
            <td class="px-6 py-4 text-center">
                <div class="flex justify-center space-x-2">
                    ${student.studentImage ? `
                        <a href="${student.studentImage}" target="_blank" rel="noreferrer" title="View Photo" class="text-blue-600 hover:text-blue-800">
                            <i class="fas fa-image"></i>
                        </a>` : ''}
                    ${student.documentFile ? `
                        <a href="${student.documentFile}" target="_blank" rel="noreferrer" title="View Document" class="text-green-600 hover:text-green-800">
                            <i class="fas fa-file-alt"></i>
                        </a>` : ''}
                </div>
            </td>
            <td class="px-6 py-4 text-center">
                <div class="flex justify-center space-x-2">
                    <button onclick="window.openEditModal('${student.id}')" class="text-indigo-600 hover:text-indigo-900" title="Edit">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button onclick="window.deleteStudent('${student.id}')" class="text-red-600 hover:text-red-900" title="Delete">
                        <i class="fas fa-trash-alt"></i>
                    </button>
                </div>
            </td>
        `;
        studentsTableBody.appendChild(row);
    });
}

// Global functions for inline event handlers
window.deleteStudent = async (id) => {
    if (confirm("Are you sure you want to delete this application? This action cannot be undone.")) {
        try {
            await deleteDoc(doc(db, "admissions", id));
            // Update local data
            studentsData = studentsData.filter(s => s.id !== id);
            renderTable();
            totalApplications.textContent = `Total Applications: ${studentsData.length}`;
            alert("Application deleted successfully.");
        } catch (error) {
            console.error("Error deleting document: ", error);
            alert("Error deleting application: " + error.message);
        }
    }
};

window.openEditModal = (id) => {
    const student = studentsData.find(s => s.id === id);
    if (!student) return;

    editStudentId.value = student.id;
    editStudentName.value = student.studentName || '';
    editFatherName.value = student.fatherName || '';
    editAdmissionLevel.value = student.admissionLevel || '';
    editAdmissionClass.value = student.admissionClass || '';
    editContactNumber.value = student.contactNumber || '';
    editCnic.value = student.cnic || '';
    editGender.value = student.gender || 'Male';

    editModal.classList.remove('hidden');
};

window.closeEditModal = () => {
    editModal.classList.add('hidden');
};

// Edit Form Submission
if (editForm) {
    editForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const id = editStudentId.value;

        const updatedData = {
            studentName: editStudentName.value,
            fatherName: editFatherName.value,
            admissionLevel: editAdmissionLevel.value,
            admissionClass: editAdmissionClass.value,
            contactNumber: editContactNumber.value,
            cnic: editCnic.value,
            gender: editGender.value
        };

        try {
            const studentRef = doc(db, "admissions", id);
            await updateDoc(studentRef, updatedData);

            // Update local data
            const index = studentsData.findIndex(s => s.id === id);
            if (index !== -1) {
                studentsData[index] = { ...studentsData[index], ...updatedData };
            }

            renderTable();
            window.closeEditModal();
            alert("Application updated successfully.");

        } catch (error) {
            console.error("Error updating document: ", error);
            alert("Error updating application: " + error.message);
        }
    });
}

window.downloadCSV = function () {
    if (studentsData.length === 0) return;

    const headers = [
        "studentName", "fatherName", "admissionLevel", "admissionClass", "contactNumber", "cnic",
        "gender", "dob", "cityOfBirth", "religion", "nationality",
        "currentAddress", "permanentAddress", "guardianName", "guardianMobile",
        "prevClass", "institution", "grades", "submittedAtFormatted"
    ];

    const csvContent = "data:text/csv;charset=utf-8,"
        + headers.join(",") + "\n"
        + studentsData.map(row => {
            return headers.map(header => {
                let value = row[header];
                if (value === null || value === undefined) value = '';
                return `"${String(value).replace(/"/g, '""')}"`;
            }).join(',');
        }).join("\n");

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `admissions_export_${new Date().toISOString().split('T')[0]}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};
