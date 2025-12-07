import { db, collection, getDocs, doc, deleteDoc, updateDoc } from './firebase-config.js';

const loginSection = document.getElementById('loginSection');
const dashboardSection = document.getElementById('dashboardSection');
const loginForm = document.getElementById('loginForm');
const loginError = document.getElementById('loginError');
const studentsTableBody = document.getElementById('studentsTableBody');
const totalApplications = document.getElementById('totalApplications');
const loadingData = document.getElementById('loadingData');
const dashboardContent = document.getElementById('dashboardContent');
const tableHead = document.querySelector('thead tr');
const tabAdmissions = document.getElementById('tabAdmissions');
const tabScholarships = document.getElementById('tabScholarships');

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

let currentCollection = 'admissions';
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

window.switchTab = (tab) => {
    currentCollection = tab;

    // Update Tab UI
    if (tab === 'admissions') {
        tabAdmissions.classList.add('border-brand-teal', 'text-brand-teal');
        tabAdmissions.classList.remove('border-transparent', 'text-gray-500');
        tabScholarships.classList.add('border-transparent', 'text-gray-500');
        tabScholarships.classList.remove('border-brand-teal', 'text-brand-teal');
    } else {
        tabScholarships.classList.add('border-brand-teal', 'text-brand-teal');
        tabScholarships.classList.remove('border-transparent', 'text-gray-500');
        tabAdmissions.classList.add('border-transparent', 'text-gray-500');
        tabAdmissions.classList.remove('border-brand-teal', 'text-brand-teal');
    }

    fetchData();
};

async function fetchData() {
    loadingData.classList.remove('hidden');
    dashboardContent.classList.add('hidden');

    try {
        const querySnapshot = await getDocs(collection(db, currentCollection));
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
        loadingData.classList.add('hidden');
    }
}

function renderTable() {
    studentsTableBody.innerHTML = '';

    // Update Table Headers
    if (currentCollection === 'admissions') {
        tableHead.innerHTML = `
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Student</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Class</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Father Name</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Contact</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">CNIC</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Submitted</th>
            <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        `;
    } else {
        tableHead.innerHTML = `
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Student</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Financial</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Father Name</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Contact</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">House</th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Submitted</th>
            <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
        `;
    }

    if (studentsData.length === 0) {
        studentsTableBody.innerHTML = '<tr><td colspan="7" class="text-center py-8 text-gray-500">No records found.</td></tr>';
        return;
    }

    studentsData.forEach(student => {
        const row = document.createElement('tr');
        row.className = "hover:bg-blue-50 transition-colors border-b border-gray-200";

        let specificColumn = '';
        let extraColumn = '';

        if (currentCollection === 'admissions') {
            specificColumn = `
                <div class="flex flex-col space-y-1">
                    <span class="bg-brand-teal text-white py-1 px-3 rounded-full text-xs w-fit">
                        ${student.admissionLevel || '-'}
                    </span>
                    <span class="text-xs text-gray-500">
                        ${student.admissionClass || '-'}
                    </span>
                </div>`;
            extraColumn = `<td class="px-6 py-4">${student.cnic || '-'}</td>`;
        } else {
            specificColumn = `
                <div class="flex flex-col space-y-1">
                    <span class="text-sm font-medium">Inc: ${student.fatherIncome || '-'}</span>
                    <span class="text-xs text-gray-500">Exp: ${student.monthlyExpenses || '-'}</span>
                </div>`;
            extraColumn = `<td class="px-6 py-4">${student.houseStatus || '-'}</td>`;
        }

        row.innerHTML = `
            <td class="px-6 py-4 font-medium text-gray-900">
                <div class="flex items-center">
                    ${student.studentImage ? `<img src="${student.studentImage}" alt="pic" class="w-8 h-8 rounded-full mr-2 object-cover border border-gray-300"/>` : ''}
                    ${student.studentName || '-'}
                </div>
            </td>
            <td class="px-6 py-4">
                ${specificColumn}
            </td>
            <td class="px-6 py-4">${student.fatherName || '-'}</td>
            <td class="px-6 py-4">${student.contactNumber || '-'}</td>
            ${extraColumn}
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
                    <button onclick="window.downloadStudentPDF('${student.id}')" class="text-red-600 hover:text-red-800" title="Download PDF">
                        <i class="fas fa-file-pdf"></i>
                    </button>
                    ${currentCollection === 'admissions' ? `
                    <button onclick="window.openEditModal('${student.id}')" class="text-indigo-600 hover:text-indigo-900" title="Edit">
                        <i class="fas fa-edit"></i>
                    </button>` : ''}
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
            await deleteDoc(doc(db, currentCollection, id));
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
            const studentRef = doc(db, currentCollection, id);
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

    let headers = [];
    if (currentCollection === 'admissions') {
        headers = [
            "studentName", "fatherName", "admissionLevel", "admissionClass", "contactNumber", "cnic",
            "gender", "dob", "cityOfBirth", "religion", "nationality",
            "currentAddress", "permanentAddress", "guardianName", "guardianMobile",
            "prevClass", "institution", "grades", "submittedAtFormatted"
        ];
    } else {
        headers = [
            "studentName", "fatherName", "cnic", "fatherCnic", "dob", "contactNumber", "fatherContactNumber", "email", "whatsapp",
            "currentAddress", "permanentAddress",
            "matricBoard", "matricMarks", "matricPercentage",
            "interBoard", "interMarks", "interPercentage",
            "otherEdu",
            "currentFieldOfStudy", "currentInstitution", "admissionDate",
            "fatherOccupation", "fatherIncome", "totalSiblings", "studyingSiblings", "totalFamilyMembers", "earningMembers",
            "houseStatus", "rentAmount", "electricityBill", "transport",
            "propertyLand", "propertyHouse", "propertyPlots", "propertyShops", "propertyCattle",
            "scholarshipReason",
            "accommodationRequired", "accommodationType",
            "ref1Name", "ref1Relation", "ref1Contact", "ref1Email",
            "ref2Name", "ref2Relation", "ref2Contact", "ref2Email",
            "submittedAtFormatted"
        ];
    }

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
    link.setAttribute("download", `${currentCollection}_export_${new Date().toISOString().split('T')[0]}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};

// PDF Generation Function for Individual Student
window.downloadStudentPDF = function (studentId) {
    const student = studentsData.find(s => s.id === studentId);
    if (!student) {
        alert('Student data not found.');
        return;
    }

    const { jsPDF } = window.jspdf;
    const doc = new jsPDF('p', 'mm', 'a4');
    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();
    const margin = 15;
    let yPos = 15;

    // Colors
    const tealColor = [0, 128, 128];
    const grayColor = [100, 100, 100];
    const blackColor = [0, 0, 0];

    // ===== HEADER =====
    doc.setFillColor(...tealColor);
    doc.rect(0, 0, pageWidth, 40, 'F');

    doc.setTextColor(255, 255, 255);
    doc.setFontSize(20);
    doc.setFont('helvetica', 'bold');
    doc.text('IDARA MISBAH UL QURAN', pageWidth / 2, 14, { align: 'center' });

    doc.setFontSize(11);
    doc.setFont('helvetica', 'normal');
    doc.text('Institute of Islamic Education', pageWidth / 2, 22, { align: 'center' });
    doc.text('Bahawalpur, Punjab, Pakistan', pageWidth / 2, 28, { align: 'center' });

    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    const title = currentCollection === 'admissions' ? 'ADMISSION APPLICATION FORM' : 'SCHOLARSHIP APPLICATION FORM';
    doc.text(title, pageWidth / 2, 37, { align: 'center' });

    doc.setTextColor(...blackColor);
    yPos = 50;

    // Application Date & ID
    doc.setFontSize(9);
    doc.setFont('helvetica', 'normal');
    const submittedDate = student.submittedAt?.seconds
        ? new Date(student.submittedAt.seconds * 1000).toLocaleDateString('en-GB')
        : 'N/A';
    doc.text('Application Date: ' + submittedDate, pageWidth - margin, yPos, { align: 'right' });
    doc.text('Application ID: ' + student.id.substring(0, 8).toUpperCase(), margin, yPos);
    yPos += 8;

    // Helper function to draw section header
    const drawSectionHeader = (title, y) => {
        if (y > pageHeight - 30) {
            doc.addPage();
            y = 20;
        }
        doc.setFillColor(...tealColor);
        doc.rect(margin, y, pageWidth - 2 * margin, 7, 'F');
        doc.setTextColor(255, 255, 255);
        doc.setFontSize(10);
        doc.setFont('helvetica', 'bold');
        doc.text(title, margin + 3, y + 5);
        doc.setTextColor(...blackColor);
        return y + 10;
    };

    // Helper function to add field
    const addField = (label, value, y, colOffset = 0) => {
        if (y > pageHeight - 20) {
            doc.addPage();
            y = 20;
        }
        const xPos = margin + colOffset;
        doc.setFontSize(9);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(...grayColor);
        doc.text(label + ':', xPos, y);
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(...blackColor);
        const displayValue = value || 'N/A';
        doc.text(String(displayValue), xPos + 45, y);
        return y + 6;
    };

    // Helper for two-column layout
    const addFieldRow = (label1, value1, label2, value2, y) => {
        if (y > pageHeight - 20) {
            doc.addPage();
            y = 20;
        }
        const colWidth = (pageWidth - 2 * margin) / 2;
        addField(label1, value1, y, 0);
        if (label2) addField(label2, value2, y, colWidth);
        return y + 6;
    };

    if (currentCollection === 'admissions') {
        // ===== ADMISSION FORM PDF =====
        yPos = drawSectionHeader('1. STUDENT INFORMATION', yPos);
        yPos = addFieldRow('Full Name', student.studentName, 'CNIC / B-Form', student.cnic, yPos);
        yPos = addFieldRow('Date of Birth', student.dob, 'Nationality', student.nationality, yPos);
        yPos = addFieldRow('Religion', student.religion, 'Admission Level', student.admissionLevel, yPos);
        yPos = addFieldRow('Admission Class', student.admissionClass, '', '', yPos);
        yPos += 4;

        yPos = drawSectionHeader('2. FATHER / GUARDIAN INFORMATION', yPos);
        yPos = addFieldRow('Father Name', student.fatherName, 'Father CNIC', student.fatherCnic, yPos);
        yPos = addFieldRow('Guardian Name', student.guardianName, 'Guardian CNIC', student.guardianCnic, yPos);
        yPos = addFieldRow('Occupation', student.fatherOccupation, 'Monthly Income', student.fatherIncome, yPos);
        yPos = addFieldRow('Mobile Number', student.contactNumber, 'Business Address', student.businessAddress, yPos);
        yPos += 4;

        yPos = drawSectionHeader('3. ADDRESS DETAILS', yPos);
        yPos = addField('Current Address', student.currentAddress, yPos);
        yPos = addField('Permanent Address', student.permanentAddress, yPos);
        yPos = addFieldRow('Accommodation Type', student.accommodationType, '', '', yPos);
        yPos += 4;

        yPos = drawSectionHeader('4. PREVIOUS EDUCATION', yPos);
        yPos = addFieldRow('Religious Education', student.previousReligiousEducation, 'Duration', student.religiousEducationDuration, yPos);
        yPos = addFieldRow('Secular Education', student.secularEducation, 'Previous Institute', student.previousInstitute, yPos);
        yPos += 4;

        yPos = drawSectionHeader('5. QURAN & HIFZ INFORMATION', yPos);
        yPos = addFieldRow('Hafiz Status', student.hafizStatus, 'Hifz Duration', student.hifzDuration, yPos);
        yPos = addFieldRow('Quran Reading Quality', student.quranReadingQuality, 'Quran Memorized', student.quranMemorized, yPos);
        yPos += 4;

        yPos = drawSectionHeader('6. HEALTH INFORMATION', yPos);
        yPos = addFieldRow('Any Illness/Disability', student.hasIllness, 'Details', student.illnessDetails, yPos);
        yPos += 4;

    } else {
        // ===== SCHOLARSHIP FORM PDF =====
        yPos = drawSectionHeader('1. PERSONAL INFORMATION', yPos);
        yPos = addFieldRow('Full Name', student.studentName, 'Father Name', student.fatherName, yPos);
        yPos = addFieldRow('CNIC', student.cnic, 'Father CNIC', student.fatherCnic, yPos);
        yPos = addFieldRow('Date of Birth', student.dob, 'Mobile', student.contactNumber, yPos);
        yPos = addFieldRow('Father Mobile', student.fatherContactNumber, 'Email', student.email, yPos);
        yPos = addField('WhatsApp', student.whatsapp, yPos);
        yPos = addField('Current Address', student.currentAddress, yPos);
        yPos = addField('Permanent Address', student.permanentAddress, yPos);
        yPos += 4;

        yPos = drawSectionHeader('2. EDUCATIONAL DETAILS', yPos);
        doc.setFont('helvetica', 'bold');
        doc.text('Matriculation:', margin, yPos);
        yPos += 5;
        yPos = addFieldRow('Board', student.matricBoard, 'Marks', student.matricMarks, yPos);
        yPos = addField('Percentage', student.matricPercentage, yPos);

        doc.setFont('helvetica', 'bold');
        doc.text('Intermediate:', margin, yPos + 2);
        yPos += 7;
        yPos = addFieldRow('Board', student.interBoard, 'Marks', student.interMarks, yPos);
        yPos = addField('Percentage', student.interPercentage, yPos);
        yPos = addField('Other Education', student.otherEdu, yPos);
        yPos += 4;

        yPos = drawSectionHeader('3. CURRENT EDUCATION', yPos);
        yPos = addFieldRow('Field of Study', student.currentFieldOfStudy, 'Institution', student.currentInstitution, yPos);
        yPos = addField('Admission Date', student.admissionDate, yPos);
        yPos += 4;

        yPos = drawSectionHeader('4. FINANCIAL INFORMATION', yPos);
        yPos = addFieldRow('Father Profession', student.fatherOccupation, 'Monthly Income', student.fatherIncome, yPos);
        yPos = addFieldRow('Total Siblings', student.totalSiblings, 'Studying Siblings', student.studyingSiblings, yPos);
        yPos = addFieldRow('Family Members', student.totalFamilyMembers, 'Earning Members', student.earningMembers, yPos);
        yPos = addFieldRow('House Status', student.houseStatus, 'Rent Amount', student.rentAmount, yPos);
        yPos = addFieldRow('Electricity Bill', student.electricityBill, 'Transport', student.transport, yPos);

        doc.setFont('helvetica', 'bold');
        doc.text('Property Details:', margin, yPos + 2);
        yPos += 7;
        yPos = addFieldRow('Land', student.propertyLand, 'House', student.propertyHouse, yPos);
        yPos = addFieldRow('Plots', student.propertyPlots, 'Shops', student.propertyShops, yPos);
        yPos = addField('Cattle', student.propertyCattle, yPos);

        yPos += 2;
        doc.setFont('helvetica', 'bold');
        doc.text('Reason for Scholarship:', margin, yPos);
        yPos += 5;
        doc.setFont('helvetica', 'normal');
        const splitReason = doc.splitTextToSize(student.scholarshipReason || 'N/A', pageWidth - 2 * margin);
        doc.text(splitReason, margin, yPos);
        yPos += splitReason.length * 5 + 4;

        yPos = drawSectionHeader('5. ACCOMMODATION', yPos);
        yPos = addFieldRow('Required?', student.accommodationRequired, 'Type', student.accommodationType, yPos);
        yPos += 4;

        yPos = drawSectionHeader('6. REFERENCES', yPos);
        doc.setFont('helvetica', 'bold');
        doc.text('Reference 1:', margin, yPos);
        yPos += 5;
        yPos = addFieldRow('Name', student.ref1Name, 'Relation', student.ref1Relation, yPos);
        yPos = addFieldRow('Contact', student.ref1Contact, 'Email', student.ref1Email, yPos);

        yPos += 2;
        doc.setFont('helvetica', 'bold');
        doc.text('Reference 2:', margin, yPos);
        yPos += 5;
        yPos = addFieldRow('Name', student.ref2Name, 'Relation', student.ref2Relation, yPos);
        yPos = addFieldRow('Contact', student.ref2Contact, 'Email', student.ref2Email, yPos);
        yPos += 4;
    }

    // Footer / Pledge
    yPos = drawSectionHeader('DECLARATION', yPos);
    doc.setFontSize(8);
    doc.setFont('helvetica', 'normal');
    const declarationText = "I hereby declare that the information provided is accurate and true. I understand that any false information may lead to the cancellation of my application.";
    const splitDecl = doc.splitTextToSize(declarationText, pageWidth - 2 * margin);
    doc.text(splitDecl, margin, yPos);
    yPos += 15;

    // Signatures
    if (yPos > pageHeight - 30) {
        doc.addPage();
        yPos = 40;
    }

    doc.line(margin, yPos, margin + 60, yPos);
    doc.text('Applicant Signature', margin, yPos + 5);

    doc.line(pageWidth - margin - 60, yPos, pageWidth - margin, yPos);
    doc.text('Guardian Signature', pageWidth - margin - 60, yPos + 5, { align: 'left' });

    // Save PDF
    doc.save(`${currentCollection}_${student.studentName || 'application'}_${student.id}.pdf`);
};
