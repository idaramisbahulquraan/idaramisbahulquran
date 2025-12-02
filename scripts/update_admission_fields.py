
import os

def update_file(file_path, target_str, replacement_str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_str in content:
            new_content = content.replace(target_str, replacement_str)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated {file_path}")
        else:
            print(f"Target string not found in {file_path}")
            # Try to find partial match or print context
            start_index = content.find("Admission Class")
            if start_index != -1:
                print(f"Context found around 'Admission Class':\n{content[start_index-50:start_index+200]}")
            else:
                print("Could not find 'Admission Class' anywhere.")

    except Exception as e:
        print(f"Error updating {file_path}: {e}")

# Update online-admission.html
admission_html_path = r"f:\New Website of Idara with Admission Form with Firebase\newwebsite new\online-admission.html"
target_admission = """                        <label class="block text-sm font-medium text-gray-700 mb-1">Admission Class / درجہ داخلہ</label>
                        <select name="admissionClass" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                            <option value="">Select Class</option>
                            <option value="Nazra">Nazra / ناظرہ</option>
                            <option value="Hifz">Hifz / حفظ</option>
                            <option value="Tajweed">Tajweed / تجوید</option>
                            <option value="Dars-e-Nizami">Dars-e-Nizami / درس نظامی</option>
                        </select>"""

replacement_admission = """                        <label class="block text-sm font-medium text-gray-700 mb-1">Admission Level / درجہ داخلہ</label>
                        <select name="admissionLevel" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                            <option value="">Select Level</option>
                            <option value="Nazra">Nazra / ناظرہ</option>
                            <option value="Hifz">Hifz / حفظ</option>
                            <option value="Tajweed">Tajweed / تجوید</option>
                            <option value="Dars-e-Nizami">Dars-e-Nizami / درس نظامی</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-1">Admission Class / نام کلاس</label>
                        <select name="admissionClass" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">
                            <option value="">Select Class</option>
                            <option value="Mutwasta">Mutwasta / متوسطہ</option>
                            <option value="Aama Arabic (A)">Aama Arabic (A) / (عامہ عربی (A))</option>
                            <option value="Aama Arabic (B)">Aama Arabic (B) / (عامہ عربی (B))</option>
                            <option value="Aama English">Aama English / عامہ انگلش</option>
                            <option value="Khasa - I">Khasa - I / خاصہ اول</option>
                            <option value="Khasa - II">Khasa - II / خاصہ دوم</option>
                            <option value="Matric">Matric / میٹرک</option>
                            <option value="Intermediate (IX)">Intermediate (IX) / (IX) انٹرمیڈیٹ</option>
                            <option value="Aalia - I (X)">Aalia - I (X) / (X) عالیہ اول</option>
                            <option value="Aalia - II (XI)">Aalia - II (XI) / (XI) عالیہ دوم</option>
                            <option value="Aalamia - I (XII)">Aalamia - I (XII) / (XII) عالمیہ اول</option>
                            <option value="Aalamia - II">Aalamia - II / عالمیہ دوم</option>
                        </select>"""

update_file(admission_html_path, target_admission, replacement_admission)

# Update admin.html
admin_html_path = r"f:\New Website of Idara with Admission Form with Firebase\newwebsite new\admin.html"
# Note: In admin.html, the select tag has attributes on new lines
target_admin = """                            <div>
                                <label class="block text-sm font-medium text-gray-700">Admission Class</label>
                                <select id="editAdmissionClass"
                                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-brand-teal focus:ring-brand-teal sm:text-sm border p-2">
                                    <option value="">Select Class</option>
                                    <option value="Nazra">Nazra</option>
                                    <option value="Hifz">Hifz</option>
                                    <option value="Dars-e-Nizami">Dars-e-Nizami</option>
                                    <option value="Fahmi-e-Deen">Fahmi-e-Deen</option>
                                </select>
                            </div>"""

replacement_admin = """                            <div>
                                <label class="block text-sm font-medium text-gray-700">Admission Level</label>
                                <select id="editAdmissionLevel" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-brand-teal focus:ring-brand-teal sm:text-sm border p-2">
                                    <option value="">Select Level</option>
                                    <option value="Nazra">Nazra</option>
                                    <option value="Hifz">Hifz</option>
                                    <option value="Tajweed">Tajweed</option>
                                    <option value="Dars-e-Nizami">Dars-e-Nizami</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700">Admission Class</label>
                                <select id="editAdmissionClass" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-brand-teal focus:ring-brand-teal sm:text-sm border p-2">
                                    <option value="">Select Class</option>
                                    <option value="Mutwasta">Mutwasta</option>
                                    <option value="Aama Arabic (A)">Aama Arabic (A)</option>
                                    <option value="Aama Arabic (B)">Aama Arabic (B)</option>
                                    <option value="Aama English">Aama English</option>
                                    <option value="Khasa - I">Khasa - I</option>
                                    <option value="Khasa - II">Khasa - II</option>
                                    <option value="Matric">Matric</option>
                                    <option value="Intermediate (IX)">Intermediate (IX)</option>
                                    <option value="Aalia - I (X)">Aalia - I (X)</option>
                                    <option value="Aalia - II (XI)">Aalia - II (XI)</option>
                                    <option value="Aalamia - I (XII)">Aalamia - I (XII)</option>
                                    <option value="Aalamia - II">Aalamia - II</option>
                                </select>
                            </div>"""

update_file(admin_html_path, target_admin, replacement_admin)
