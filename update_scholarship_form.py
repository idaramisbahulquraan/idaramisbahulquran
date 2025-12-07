
import os

file_path = 'scholarship.html'

# New Form Content
new_form_content = '''
        <form id="scholarshipForm" class="p-8 space-y-8">
            <!-- 1. Personal Information -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">1</span>
                    Personal Information / ذاتی کوائف
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Full Name / نام طالب علم</label>
                        <input type="text" name="studentName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Father's Name / نام والد</label>
                        <input type="text" name="fatherName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">CNIC / شناختی کارڈ نمبر</label>
                        <input type="text" name="cnic" id="cnic_number" required placeholder="00000-0000000-0" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Father's CNIC / والد کا شناختی کارڈ نمبر</label>
                        <input type="text" name="fatherCnic" placeholder="00000-0000000-0" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Date of Birth / تاریخ پیدائش</label>
                        <input type="date" name="dob" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Mobile Number / موبائل نمبر</label>
                        <input type="tel" name="contactNumber" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Father's Mobile Number / والد کا موبائل نمبر</label>
                        <input type="tel" name="fatherContactNumber" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Email / ای میل</label>
                        <input type="email" name="email" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">WhatsApp Number / واٹس ایپ نمبر</label>
                        <input type="tel" name="whatsapp" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Present Address / موجودہ پتہ</label>
                        <textarea name="currentAddress" required rows="2" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent"></textarea>
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Permanent Address / مستقل پتہ</label>
                        <textarea name="permanentAddress" required rows="2" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent"></textarea>
                    </div>
                </div>
            </section>

            <!-- 2. Educational Details -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">2</span>
                    Educational Details / تعلیمی کوائف
                </h3>
                <div class="space-y-4">
                    <!-- Matriculation -->
                    <div class="bg-gray-50 p-4 rounded-lg">
                        <h4 class="font-medium text-gray-700 mb-3">Matriculation / میٹرک</h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Board/University</label>
                                <input type="text" name="matricBoard" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Marks Obtained</label>
                                <input type="number" name="matricMarks" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Percentage</label>
                                <input type="text" name="matricPercentage" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                        </div>
                    </div>

                    <!-- Intermediate -->
                    <div class="bg-gray-50 p-4 rounded-lg">
                        <h4 class="font-medium text-gray-700 mb-3">Intermediate / انٹرمیڈیٹ</h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Board/University</label>
                                <input type="text" name="interBoard" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Marks Obtained</label>
                                <input type="number" name="interMarks" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Percentage</label>
                                <input type="text" name="interPercentage" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                        </div>
                    </div>

                    <!-- Other -->
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Other (if applicable) / دیگر تعلیم</label>
                        <input type="text" name="otherEdu" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                </div>
            </section>

            <!-- 3. Current Education -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">3</span>
                    Current Education / موجودہ تعلیم
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Field of Study / شعبہ</label>
                        <input type="text" name="currentFieldOfStudy" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Present College/University / موجودہ ادارہ</label>
                        <input type="text" name="currentInstitution" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Date of Admission / تاریخ داخلہ</label>
                        <input type="date" name="admissionDate" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                </div>
            </section>

            <!-- 4. Financial Information / Bio Data -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">4</span>
                    Financial Information / مالی کوائف
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Father's Profession / والد کا پیشہ</label>
                        <input type="text" name="fatherOccupation" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Father's Monthly Income / والد کی ماہانہ آمدن</label>
                        <input type="text" name="fatherIncome" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Total Siblings / کل بہن بھائی</label>
                        <input type="number" name="totalSiblings" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Siblings Studying / زیر تعلیم بہن بھائی</label>
                        <input type="number" name="studyingSiblings" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Total Family Members / کل افراد خانہ</label>
                        <input type="number" name="totalFamilyMembers" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Earning Members / کمانے والے افراد</label>
                        <input type="number" name="earningMembers" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">House Status / رہائش</label>
                        <select name="houseStatus" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                            <option value="Owned">Owned / ذاتی</option>
                            <option value="Rented">Rented / کرایہ</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Rent Amount (if rented) / کرایہ</label>
                        <input type="text" name="rentAmount" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Monthly Electricity Bill / ماہانہ بجلی بل</label>
                        <input type="text" name="electricityBill" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Transport / سواری</label>
                        <input type="text" name="transport" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                    
                    <div class="md:col-span-2">
                        <h4 class="font-medium text-gray-700 mb-3 mt-2">Property Details / تفصیل جائیداد</h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Agricultural Land / زرعی زمین</label>
                                <input type="text" name="propertyLand" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Residential House / رہائشی مکان</label>
                                <input type="text" name="propertyHouse" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">City Plots / شہری پلاٹ</label>
                                <input type="text" name="propertyPlots" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Shops/Other / دوکانات و دیگر</label>
                                <input type="text" name="propertyShops" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Cattle / مال مویشی</label>
                                <input type="text" name="propertyCattle" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                        </div>
                    </div>

                    <div class="md:col-span-2">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Justification for Financial Assistance / وظیفہ کی وجہ</label>
                        <textarea name="scholarshipReason" required rows="4" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent" placeholder="Please explain why you need financial assistance..."></textarea>
                    </div>
                </div>
            </section>

            <!-- 5. Accommodation -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">5</span>
                    Accommodation / رہائش
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Do you require accommodation? / کیا آپ کو رہائش درکار ہے؟</label>
                        <select name="accommodationRequired" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                            <option value="No">No / نہیں</option>
                            <option value="Yes">Yes / ہاں</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">If yes, specify type / اگر ہاں، تو قسم بتائیں</label>
                        <input type="text" name="accommodationType" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                </div>
            </section>

            <!-- 6. References -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">6</span>
                    References / حوالہ جات
                </h3>
                <div class="space-y-6">
                    <!-- Reference 1 -->
                    <div class="bg-gray-50 p-4 rounded-lg">
                        <h4 class="font-medium text-gray-700 mb-3">Reference 1</h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Name</label>
                                <input type="text" name="ref1Name" required class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Relationship</label>
                                <input type="text" name="ref1Relation" required class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Contact Number</label>
                                <input type="tel" name="ref1Contact" required class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Email</label>
                                <input type="email" name="ref1Email" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                        </div>
                    </div>

                    <!-- Reference 2 -->
                    <div class="bg-gray-50 p-4 rounded-lg">
                        <h4 class="font-medium text-gray-700 mb-3">Reference 2</h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Name</label>
                                <input type="text" name="ref2Name" required class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Relationship</label>
                                <input type="text" name="ref2Relation" required class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Contact Number</label>
                                <input type="tel" name="ref2Contact" required class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                            <div>
                                <label class="block text-xs font-medium text-gray-500 mb-1">Email</label>
                                <input type="email" name="ref2Email" class="w-full px-3 py-2 border border-gray-300 rounded-md">
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 7. Documents -->
            <section>
                <h3 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 flex items-center">
                    <span class="bg-brand-teal text-white w-8 h-8 rounded-full flex items-center justify-center text-sm mr-3">7</span>
                    Documents / دستاویزات
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Student's Photo / طالب علم کی تصویر</label>
                        <input type="file" name="studentImage" accept="image/*" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                        <p class="text-xs text-gray-500 mt-1">Upload a recent passport size photograph</p>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">CNIC/B-Form Copy / شناختی کارڈ/ب فارم کی کاپی</label>
                        <input type="file" name="documentFile" accept=".pdf,.jpg,.jpeg,.png" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                    </div>
                </div>
            </section>

            <!-- 8. Declaration -->
            <section class="bg-gray-50 p-6 rounded-lg border border-gray-200">
                <h3 class="text-xl font-semibold text-gray-800 mb-4">Declaration / اقرار نامہ</h3>
                <div class="space-y-4">
                    <label class="flex items-start space-x-3">
                        <input type="checkbox" name="declaration" required class="mt-1 h-4 w-4 text-brand-teal border-gray-300 rounded focus:ring-brand-teal">
                        <span class="text-sm text-gray-700">
                            I hereby declare that the information provided is accurate and true. I understand that any false information may lead to the cancellation of my application.
                            <br>
                            میں حلفیہ بیان کرتا ہوں کہ فراہم کردہ معلومات درست ہیں۔ میں سمجھتا ہوں کہ کوئی بھی غلط معلومات میری درخواست منسوخ ہونے کا باعث بن سکتی ہیں۔
                        </span>
                    </label>
                </div>
            </section>

            <!-- Submit Button -->
            <div class="pt-6">
                <button type="submit" id="submitButton" class="w-full bg-brand-teal text-white py-3 px-6 rounded-lg text-lg font-semibold hover:bg-brand-darkTeal transition-colors shadow-lg flex items-center justify-center">
                    <span>Submit Application / درخواست جمع کروائیں</span>
                    <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>
                    </svg>
                </button>
            </div>
        </form>
'''

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start and end of the form to replace
start_marker = '<form id="scholarshipForm"'
end_marker = '</form>'

start_index = content.find(start_marker)
end_index = content.find(end_marker, start_index) + len(end_marker)

if start_index != -1 and end_index != -1:
    new_content = content[:start_index] + new_form_content + content[end_index:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated scholarship form.")
else:
    print("Could not find form to replace.")
