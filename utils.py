import csv
from employee import Employee
from job_position import JobPosition

def load_csv_file(file_path, class_type):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if class_type == Employee:
                employee_id, shift_availability, absenteeism = row
                data.append(Employee(employee_id, shift_availability, absenteeism))
            elif class_type == JobPosition:
                job_id, required_skills = row
                data.append(JobPosition(job_id, required_skills))
    return data

def add_skills_to_employees(employees, employee_skills_file):
    with open(employee_skills_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            employee_id, skill = row
            for employee in employees:
                if employee.id == employee_id:
                    employee.add_skill(skill)

def add_required_skills_to_jobs(job_positions, job_skills_file):
    with open(job_skills_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            job_id, skill = row
            for job in job_positions:
                if job.id == job_id:
                    job.add_required_skill(skill)

