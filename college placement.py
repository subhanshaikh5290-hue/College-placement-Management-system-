import tkinter as tk
from tkinter import ttk, messagebox

# Temporary storage
students = []
companies = []
placements = []


# Main Window
root = tk.Tk()
root.title("College Placement Management System")
root.geometry("1000x650")
root.configure(bg="#eaf2f8")


# Heading
title = tk.Label(
    root,
    text="COLLEGE PLACEMENT MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#154360",
    fg="white",
    pady=15
)
title.pack(fill="x")


# Notebook Tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)


# ================= STUDENT TAB =================

student_tab = tk.Frame(notebook, bg="#eaf2f8")
notebook.add(student_tab, text="Student Registration")

tk.Label(
    student_tab, text="Student Registration",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8"
).pack(pady=10)

form = tk.Frame(student_tab, bg="#eaf2f8")
form.pack(pady=10)


def create_entry(parent, label, row):
    tk.Label(
        parent, text=label,
        font=("Arial", 12),
        bg="#eaf2f8"
    ).grid(row=row, column=0, padx=10, pady=8, sticky="w")

    entry = tk.Entry(parent, font=("Arial", 12), width=30)
    entry.grid(row=row, column=1, padx=10, pady=8)
    return entry


name_entry = create_entry(form, "Student Name:", 0)
roll_entry = create_entry(form, "Roll Number:", 1)
course_entry = create_entry(form, "Course:", 2)
marks_entry = create_entry(form, "Percentage:", 3)
email_entry = create_entry(form, "Email:", 4)


# Student Table
student_table = ttk.Treeview(
    student_tab,
    columns=("Roll", "Name", "Course", "Percentage", "Email"),
    show="headings",
    height=10
)

for col in ("Roll", "Name", "Course", "Percentage", "Email"):
    student_table.heading(col, text=col)
    student_table.column(col, width=150)

student_table.pack(fill="both", expand=True, padx=10, pady=10)


def add_student():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()
    course = course_entry.get().strip()
    marks = marks_entry.get().strip()
    email = email_entry.get().strip()

    if not all([name, roll, course, marks, email]):
        messagebox.showerror("Error", "Please fill all fields!")
        return

    if any(s["roll"] == roll for s in students):
        messagebox.showerror("Error", "Roll number already exists!")
        return

    try:
        percentage = float(marks)
        if not 0 <= percentage <= 100:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Error", "Enter a valid percentage between 0 and 100!"
        )
        return

    student = {
        "name": name,
        "roll": roll,
        "course": course,
        "percentage": percentage,
        "email": email
    }

    students.append(student)

    student_table.insert(
        "", "end",
        values=(roll, name, course, percentage, email)
    )

    for entry in (
        name_entry, roll_entry, course_entry,
        marks_entry, email_entry
    ):
        entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Student registered successfully!")


tk.Button(
    form, text="Register Student",
    font=("Arial", 12, "bold"),
    bg="#2874a6", fg="white",
    command=add_student
).grid(row=5, column=1, pady=15)


# ================= COMPANY TAB =================

company_tab = tk.Frame(notebook, bg="#eaf2f8")
notebook.add(company_tab, text="Company Registration")

tk.Label(
    company_tab, text="Company Registration",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8"
).pack(pady=15)

company_form = tk.Frame(company_tab, bg="#eaf2f8")
company_form.pack(pady=20)

company_name = create_entry(company_form, "Company Name:", 0)
job_role = create_entry(company_form, "Job Role:", 1)
salary = create_entry(company_form, "Package (LPA):", 2)
eligibility = create_entry(company_form, "Minimum Percentage:", 3)


company_table = ttk.Treeview(
    company_tab,
    columns=("Company", "Role", "Package", "Eligibility"),
    show="headings",
    height=10
)

for col in ("Company", "Role", "Package", "Eligibility"):
    company_table.heading(col, text=col)
    company_table.column(col, width=200)

company_table.pack(fill="both", expand=True, padx=10, pady=10)


def add_company():
    name = company_name.get().strip()
    role = job_role.get().strip()
    package = salary.get().strip()
    minimum = eligibility.get().strip()

    if not all([name, role, package, minimum]):
        messagebox.showerror("Error", "Please fill all fields!")
        return

    try:
        package_value = float(package)
        minimum_value = float(minimum)

        if package_value < 0 or not 0 <= minimum_value <= 100:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error", "Enter valid package and eligibility values!"
        )
        return

    company = {
        "name": name,
        "role": role,
        "package": package_value,
        "minimum": minimum_value
    }

    companies.append(company)

    company_table.insert(
        "", "end",
        values=(name, role, package_value, minimum_value)
    )

    for entry in (company_name, job_role, salary, eligibility):
        entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Company added successfully!")


tk.Button(
    company_form,
    text="Add Company",
    font=("Arial", 12, "bold"),
    bg="#239b56",
    fg="white",
    command=add_company
).grid(row=4, column=1, pady=15)


# ================= PLACEMENT TAB =================

placement_tab = tk.Frame(notebook, bg="#eaf2f8")
notebook.add(placement_tab, text="Placement")

tk.Label(
    placement_tab,
    text="Student Placement",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8"
).pack(pady=15)

placement_form = tk.Frame(placement_tab, bg="#eaf2f8")
placement_form.pack(pady=20)

tk.Label(
    placement_form,
    text="Select Student:",
    font=("Arial", 12),
    bg="#eaf2f8"
).grid(row=0, column=0, padx=10, pady=10)

student_combo = ttk.Combobox(
    placement_form, width=35, state="readonly"
)
student_combo.grid(row=0, column=1, padx=10, pady=10)

tk.Label(
    placement_form,
    text="Select Company:",
    font=("Arial", 12),
    bg="#eaf2f8"
).grid(row=1, column=0, padx=10, pady=10)

company_combo = ttk.Combobox(
    placement_form, width=35, state="readonly"
)
company_combo.grid(row=1, column=1, padx=10, pady=10)


placement_table = ttk.Treeview(
    placement_tab,
    columns=("Roll", "Student", "Company", "Role", "Package"),
    show="headings",
    height=12
)

for col in ("Roll", "Student", "Company", "Role", "Package"):
    placement_table.heading(col, text=col)
    placement_table.column(col, width=170)

placement_table.pack(fill="both", expand=True, padx=10, pady=10)


def update_combos():
    student_combo["values"] = [
        f'{s["roll"]} - {s["name"]}' for s in students
    ]

    company_combo["values"] = [
        c["name"] for c in companies
    ]


def place_student():
    selected_student = student_combo.get()
    selected_company = company_combo.get()

    if not selected_student or not selected_company:
        messagebox.showerror(
            "Error", "Please select a student and company!"
        )
        return

    roll = selected_student.split(" - ", 1)[0]

    student = next(
        (s for s in students if s["roll"] == roll),
        None
    )

    company = next(
        (c for c in companies if c["name"] == selected_company),
        None
    )

    if not student or not company:
        messagebox.showerror("Error", "Invalid selection!")
        return

    if student["percentage"] < company["minimum"]:
        messagebox.showwarning(
            "Not Eligible",
            f"Student needs at least {company['minimum']}%."
        )
        return

    if any(p["roll"] == roll for p in placements):
        messagebox.showerror(
            "Error", "Student is already placed!"
        )
        return

    placement = {
        "roll": roll,
        "student": student["name"],
        "company": company["name"],
        "role": company["role"],
        "package": company["package"]
    }

    placements.append(placement)

    placement_table.insert(
        "", "end",
        values=(
            roll,
            student["name"],
            company["name"],
            company["role"],
            company["package"]
        )
    )

    messagebox.showinfo(
        "Success", "Student placed successfully!"
    )


tk.Button(
    placement_form,
    text="Place Student",
    font=("Arial", 12, "bold"),
    bg="#884ea0",
    fg="white",
    command=place_student
).grid(row=2, column=1, pady=15)


# ================= SEARCH TAB =================

search_tab = tk.Frame(notebook, bg="#eaf2f8")
notebook.add(search_tab, text="Search Student")

tk.Label(
    search_tab,
    text="Search Student by Roll Number",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8"
).pack(pady=20)

search_form = tk.Frame(search_tab, bg="#eaf2f8")
search_form.pack(pady=10)

search_entry = tk.Entry(search_form, font=("Arial", 13), width=30)
search_entry.grid(row=0, column=0, padx=10)

search_result = tk.Label(
    search_tab,
    text="",
    font=("Arial", 13),
    bg="#eaf2f8",
    justify="left"
)
search_result.pack(pady=20)


def search_student():
    roll = search_entry.get().strip()

    student = next(
        (s for s in students if s["roll"] == roll),
        None
    )

    if student:
        search_result.config(
            text=(
                f"Name: {student['name']}\n"
                f"Roll Number: {student['roll']}\n"
                f"Course: {student['course']}\n"
                f"Percentage: {student['percentage']}%\n"
                f"Email: {student['email']}"
            )
        )
    else:
        search_result.config(text="Student not found!")


tk.Button(
    search_form,
    text="Search",
    font=("Arial", 12, "bold"),
    bg="#2874a6",
    fg="white",
    command=search_student
).grid(row=0, column=1, padx=10)


# ================= DELETE STUDENT =================

def delete_student():
    selected = student_table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning", "Please select a student to delete!"
        )
        return

    item = selected[0]
    values = student_table.item(item, "values")
    roll = values[0]

    if not messagebox.askyesno(
        "Confirm", "Are you sure you want to delete this student?"
    ):
        return

    students[:] = [s for s in students if s["roll"] != roll]

    placements[:] = [p for p in placements if p["roll"] != roll]

    student_table.delete(item)

    for row in placement_table.get_children():
        row_values = placement_table.item(row, "values")
        if row_values[0] == roll:
            placement_table.delete(row)

    update_combos()

    messagebox.showinfo("Success", "Student deleted successfully!")


tk.Button(
    student_tab,
    text="Delete Selected Student",
    font=("Arial", 11, "bold"),
    bg="#c0392b",
    fg="white",
    command=delete_student
).pack(pady=5)


# ================= REFRESH =================

def refresh_data(event=None):
    update_combos()


notebook.bind("<<NotebookTabChanged>>", refresh_data)


# Main Loop
root.mainloop()