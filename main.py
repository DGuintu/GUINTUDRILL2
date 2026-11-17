"""
Student Club Member Management System
Uses sets and set operators exclusively.
Strictly zero classes, conditional statements (if/elif/else), or loops (for/while).
"""

from pyscript import document

# 4 Predefined grade level sets (Requirement #4)
grade_7 = {"Thalia Sazaar", "Dallas Quinton"}
grade_8 = {"Fiona Dunkin", "Pricilla Dovey"}
grade_9 = {"Gracie Elliot", "Gruntun Gallagher"}
grade_10 = {"Susanne Collins", "Lynn Painter"}


def add_member_handler(event=None):
    """
    Retrieves user input, combines predefined sets with the new member into a master 
    set using set union (|) and difference (-), and outputs formatted HTML badges and total count.
    """
    # 1. Retrieve text box inputs from the DOM (Requirement #2)
    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()

    # 2. Combine and format the candidate's full name (Title Case)
    new_member = f"{first_name} {last_name}".strip().title()

    # 3. Combine sets using union (|) and remove any empty input strings using difference (-)
    master_set = (grade_7 | grade_8 | grade_9 | grade_10 | {new_member}) - {""}

    # 4. Calculate the total number of unique members using len()
    total_members = len(master_set)

    # 5. Generate stylish HTML badges for each member using a generator expression (No for/while loops!)
    member_badges = "".join(
        f'<span class="badge bg-primary-subtle text-primary border border-primary-subtle px-3 py-2 rounded-pill fw-medium fs-6 m-1 shadow-sm">{member}</span>'
        for member in sorted(master_set)
    )

    # 6. Output results as HTML using f-strings (Requirement #5)
    document.querySelector("#total-output").innerHTML = f"{total_members}"
    document.querySelector("#member-list-output").innerHTML = member_badges

    # 7. Clear input fields for a smoother user experience
    document.querySelector("#first-name").value = ""
    document.querySelector("#last-name").value = ""