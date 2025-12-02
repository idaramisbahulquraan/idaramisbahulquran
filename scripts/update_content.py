import os
from admission_html import ADMISSION_HTML
from admin_html import ADMIN_HTML

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMISSION_FILE = os.path.join(BASE_DIR, 'online-admission.html')
ADMIN_FILE = os.path.join(BASE_DIR, 'admin.html')

def update_file(file_path, new_content):
    print(f"Updating {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Define markers
        start_marker = '<div data-elementor-type="wp-post" data-elementor-id="7"'
        end_marker = '<footer'
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        
        if start_idx == -1 or end_idx == -1:
            print(f"Error: Markers not found in {file_path}")
            print(f"Start found: {start_idx != -1}, End found: {end_idx != -1}")
            return False
            
        # Keep the footer tag, replace everything before it up to start marker
        new_file_content = content[:start_idx] + new_content + content[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)
            
        print(f"Successfully updated {file_path}")
        return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

if __name__ == "__main__":
    update_file(ADMISSION_FILE, ADMISSION_HTML)
    update_file(ADMIN_FILE, ADMIN_HTML)
