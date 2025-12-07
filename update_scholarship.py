
import os

file_path = 'scholarship.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Title
content = content.replace('آن لائن داخلہ فارم', 'درخواست برائے وظیفہ')
content = content.replace('Online Admission Form', 'Scholarship Application Form')

# Replace Form ID
content = content.replace('id="admissionForm"', 'id="scholarshipForm"')

# Replace Script
content = content.replace('src="js/admission.js"', 'src="js/scholarship.js"')

# Add Scholarship Fields
# Find the Father Income field and add more fields after it
income_field = 'name="fatherIncome" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent">'
new_fields = income_field + '</div><div><label class="block text-sm font-medium text-gray-700 mb-1">Number of Dependents / زیر کفالت افراد کی تعداد</label><input type="number" name="dependents" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent"></div><div><label class="block text-sm font-medium text-gray-700 mb-1">Monthly Expenses / ماہانہ اخراجات</label><input type="text" name="monthlyExpenses" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent"></div><div class="md:col-span-2"><label class="block text-sm font-medium text-gray-700 mb-1">Reason for Scholarship / وظیفہ کی وجہ</label><textarea name="scholarshipReason" required rows="3" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-brand-teal focus:border-transparent" placeholder="Why do you need this scholarship? / آپ کو اس وظیفہ کی ضرورت کیوں ہے؟"></textarea>'

content = content.replace(income_field, new_fields)

# Add Scholarship Link in Navigation
# Find 'Online Admission' menu item and add 'Scholarship' after it
nav_item = '<li id="menu-item-admission" class="menu-item menu-item-type-custom menu-item-object-custom parent hfe-creative-menu">\n    <a href="online-admission.html" class="hfe-menu-item">Online Admission</a>\n</li>'
new_nav_item = nav_item + '\n<li id="menu-item-scholarship" class="menu-item menu-item-type-custom menu-item-object-custom parent hfe-creative-menu">\n    <a href="scholarship.html" class="hfe-menu-item">Scholarship</a>\n</li>'

content = content.replace(nav_item, new_nav_item)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
