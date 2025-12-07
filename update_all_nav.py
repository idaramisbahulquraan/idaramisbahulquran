
import os

# Define the navigation item to look for and the one to add
nav_item_marker = 'online-admission.html'
scholarship_nav_item = '''
<li id="menu-item-scholarship" class="menu-item menu-item-type-custom menu-item-object-custom parent hfe-creative-menu">
    <a href="scholarship.html" class="hfe-menu-item">Scholarship</a>
</li>'''

# Directory to search in
directory = '.'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if Scholarship link already exists
        if 'scholarship.html' in content and 'id="menu-item-scholarship"' in content:
            print(f"Skipping {filename}: Scholarship link already exists.")
            continue
            
        # Find the Online Admission link to insert after
        # We look for the closing </li> of the online admission item
        # This is a bit heuristic, assuming standard formatting
        
        # Pattern to find: 
        # <li ...>
        #    <a href="online-admission.html" ...>...</a>
        # </li>
        
        # Let's try to find the specific substring for the online admission link href
        if nav_item_marker in content:
            # Find the index of the marker
            index = content.find(nav_item_marker)
            
            # Find the closing </li> after this marker
            closing_li_index = content.find('</li>', index)
            
            if closing_li_index != -1:
                # Insert after the closing </li>
                insert_pos = closing_li_index + 5 # len('</li>')
                
                new_content = content[:insert_pos] + '\n' + scholarship_nav_item + content[insert_pos:]
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"Could not find closing </li> for {filename}")
        else:
            print(f"Skipping {filename}: Online Admission link not found.")
