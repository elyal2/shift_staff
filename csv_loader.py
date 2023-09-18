import csv
from employee import Employee
from job_position import JobPosition

class CSVLoader:
    def __init__(self, employees_file, employee_skills_file, job_skills_file):
        self.employees_file = employees_file
        self.employee_skills_file = employee_skills_file
        self.job_skills_file = job_skills_file

    def load_employees(self):
        employees = []
        with open(self.employees_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                employee_id, shift_availability, absenteeism = row
                employees.append(Employee(employee_id, shift_availability, absenteeism))
        return employees

    def load_employee_skills(self, employees):
        with open(self.employee_skills_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                employee_id, skill = row
                for employee in employees:
                    if employee.id == employee_id:
                        employee.add_skill(skill)

    def load_job_positions(self):
        job_positions = []
        with open(self.job_skills_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                job_id, skills = row
                required_skills = skills.split(",")  # Split the skills by comma
                job_positions.append(JobPosition(job_id, required_skills))
        return job_positions
