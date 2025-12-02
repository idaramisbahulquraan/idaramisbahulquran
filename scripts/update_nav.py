import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def update_navigation():
    html_files = glob.glob(os.path.join(BASE_DIR, '*.html'))
    
    admission_link = """
<li id="menu-item-admission" class="menu-item menu-item-type-custom menu-item-object-custom parent hfe-creative-menu">
    <a href="online-admission.html" class="hfe-menu-item">Online Admission</a>
</li>"""

    admin_link = ' | <a href="admin.html" style="color: #f6c640;">Admin</a>'

    for file_path in html_files:
        if 'assets' in file_path:
            continue
            
        print(f"Processing {os.path.basename(file_path)}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # 1. Add Online Admission link
        if 'href="online-admission.html"' not in content:
            # Find Online Academy link
            marker = 'href="online-academy.html"'
            idx = content.find(marker)
            if idx != -1:
                # Find the closing </li> of the Online Academy item
                # The structure is: <li ...><a ...>...</a></li>
                # We found the href inside the <a>.
                # We need to find the next </li> after this href.
                end_li_idx = content.find('</li>', idx)
                if end_li_idx != -1:
                    insert_pos = end_li_idx + 5 # after </li>
                    content = content[:insert_pos] + admission_link + content[insert_pos:]
                    modified = True
                    print("  Added Online Admission link")
                else:
                    print("  Could not find closing </li> for Online Academy")
            else:
                print("  Could not find Online Academy link")
        else:
            print("  Online Admission link already exists")

        # 2. Add Admin link to footer
        if 'href="admin.html"' not in content:
            marker = 'Dr. Ahmad Ghazali</em></a>.'
            idx = content.find(marker)
            if idx != -1:
                insert_pos = idx + len(marker)
                content = content[:insert_pos] + admin_link + content[insert_pos:]
                modified = True
                print("  Added Admin link to footer")
            else:
                print("  Could not find footer marker")
        else:
            print("  Admin link already exists")
            
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("  Saved changes")

if __name__ == "__main__":
    update_navigation()
