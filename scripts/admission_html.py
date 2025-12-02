ADMISSION_HTML = """
<div class="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 font-sans">
    <div class="max-w-4xl mx-auto bg-white rounded-xl shadow-lg overflow-hidden">
        <!-- Header -->
        <div class="bg-brand-teal px-8 py-6 text-white text-center">
            <h1 class="text-3xl font-bold mb-2 font-urdu">آن لائن داخلہ فارم</h1>
            <p class="text-blue-100">Online Admission Form</p>
        </div>

        <!-- Loading Overlay -->
        <div id="loadingOverlay" class="hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div class="bg-white p-6 rounded-lg shadow-xl flex flex-col items-center">
                <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-brand-teal mb-4"></div>
                <p class="text-gray-700">Submitting application...</p>
            </div>
        </div>

        <!-- Success Message -->
        <div id="successMessage" class="hidden p-8 text-center">
            <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
            </div>
            <h2 class="text-2xl font-bold text-gray-900 mb-2">Application Submitted!</h2>
            <p class="text-gray-600 mb-6">Your admission form has been successfully submitted.</p>
            <button onclick="resetForm()" class="bg-brand-teal text-white px-6 py-2 rounded-lg hover:bg-brand-darkTeal transition-colors">
                Submit Another Application
            </button>
        </div>

        <!-- Error Message -->
        <div id="errorMessage" class="hidden bg-red-50 border-l-4 border-red-500 p-4 mb-6 mx-8 mt-6">
            <div class="flex">
                <div class="flex-shrink-0">
                    <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
                    </svg>
                </div>
                <div class="ml-3">
                    <p class="text-sm text-red-700" id="errorText"></p>
                </div>
            </div>
        </div>

        <form id="admissionForm" class="p-8 space-y-8">
            <!-- Student Information -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">1</span>
                    Student Information / کوائف طالب علم
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Full Name / نام طالب علم</label>
                        <input type="text" name="studentName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Admission Class / درجہ داخلہ</label>
                        <select name="admissionClass" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                            <option value="">Select Class</option>
                            <option value="Nazra">Nazra / ناظرہ</option>
                            <option value="Hifz">Hifz / حفظ</option>
                            <option value="Tajweed">Tajweed / تجوید</option>
                            <option value="Dars-e-Nizami">Dars-e-Nizami / درس نظامی</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Date of Birth / تاریخ پیدائش</label>
                        <input type="date" name="dob" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">CNIC/B-Form / شناختی کارڈ نمبر</label>
                        <input type="text" name="cnic" id="cnic_number" required placeholder="xxxxx-xxxxxxx-x" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Nationality / قومیت</label>
                        <input type="text" name="nationality" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Religion / مذہب</label>
                        <select name="religion" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                            <option value="Islam">Islam</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                </div>
            </section>

            <!-- Father's Information -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">2</span>
                    Father's Information / کوائف والد
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Father's Name / نام والد</label>
                        <input type="text" name="fatherName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">CNIC / شناختی کارڈ نمبر</label>
                        <input type="text" name="fatherCnic" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Occupation / پیشہ</label>
                        <input type="text" name="fatherOccupation" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Mobile Number / موبائل نمبر</label>
                        <input type="tel" name="contactNumber" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                </div>
            </section>

            <!-- Address -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">3</span>
                    Address / پتہ
                </h3>
                <div class="space-y-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Current Address / موجودہ پتہ</label>
                        <textarea name="currentAddress" required rows="2" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent"></textarea>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Permanent Address / مستقل پتہ</label>
                        <textarea name="permanentAddress" required rows="2" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent"></textarea>
                    </div>
                </div>
            </section>

            <!-- Documents Upload -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">4</span>
                    Documents / دستاویزات
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Student Photo / طالب علم کی تصویر</label>
                        <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-lg hover:border-brand-teal transition-colors">
                            <div class="space-y-1 text-center">
                                <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                                    <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                </svg>
                                <div class="flex text-sm text-gray-600">
                                    <label class="relative cursor-pointer bg-white rounded-md font-medium text-brand-teal hover:text-brand-darkTeal focus-within:outline-none">
                                        <span>Upload a file</span>
                                        <input type="file" name="studentImage" accept="image/*" class="sr-only">
                                    </label>
                                </div>
                                <p class="text-xs text-gray-500">PNG, JPG up to 5MB</p>
                            </div>
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Documents (B-Form/CNIC) / دستاویزات</label>
                        <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-lg hover:border-brand-teal transition-colors">
                            <div class="space-y-1 text-center">
                                <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                                    <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                </svg>
                                <div class="flex text-sm text-gray-600">
                                    <label class="relative cursor-pointer bg-white rounded-md font-medium text-brand-teal hover:text-brand-darkTeal focus-within:outline-none">
                                        <span>Upload a file</span>
                                        <input type="file" name="documentFile" accept=".pdf,image/*" class="sr-only">
                                    </label>
                                </div>
                                <p class="text-xs text-gray-500">PDF, PNG, JPG up to 5MB</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Submit Button -->
            <div class="pt-6">
                <button type="submit" id="submitButton" class="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-brand-teal hover:bg-brand-darkTeal focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-teal transition-colors">
                    Submit Application / درخواست جمع کروائیں
                </button>
            </div>
        </form>
    </div>
</div>
<script type="module" src="js/admission.js"></script>
"""
