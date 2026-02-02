import os

def check_eligibility(file_path):
    if not file_path:
        return 0, "INVALID RESUME FILE"
        
    # Check file extension
    _, ext = os.path.splitext(file_path)
    if ext.lower() != '.txt':
        return 0, "INVALID INPUT FORMAT"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if not content.strip():
            return 0, "INVALID RESUME FILE" # Empty file treated as invalid
            
        # Split by comma, strip whitespace, remove empty entries
        skills = [skill.strip() for skill in content.split(',') if skill.strip()]
        
        skill_count = len(skills)
        
        # Determine status based on rules
        if skill_count == 0:
            status = "REJECTED"
        elif 1 <= skill_count <= 2:
            status = "NOT ELIGIBLE"
        elif 3 <= skill_count <= 6:
            status = "ELIGIBLE"
        else: # More than 6
            status = "HIGHLY ELIGIBLE"
            
        return skill_count, status

    except Exception as e:
        return 0, "INVALID RESUME FILE"
