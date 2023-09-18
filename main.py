from csv_loader import CSVLoader
from scheduler import Scheduler

def main():
    # Define the paths to the CSV files
    employees_file = 'employees.csv'
    employee_skills_file = 'employee_skills.csv'
    job_skills_file = 'job_skills.csv'

    # Create a CSVLoader object
    csv_loader = CSVLoader(employees_file, employee_skills_file, job_skills_file)

    # Load the employees and their skills
    employees = csv_loader.load_employees()
    print(f'Loaded {len(employees)} employees')
    csv_loader.load_employee_skills(employees)

    # Load the job positions
    job_positions = csv_loader.load_job_positions()
    print(f'Loaded {len(job_positions)} job positions')

    # Create a Scheduler object
    scheduler = Scheduler(employees, job_positions)

    # Generate the schedule
    schedule = scheduler.schedule()

    # Print the schedule
    schedule_size = 0
    for job_id, employee_ids in schedule.items():
        schedule_size += len(employee_ids)
        print(f'Job {job_id} will be performed by employees {", ".join(employee_ids)}')

    # Print the schedule output size
    print(f'Schedule output size: {schedule_size}')

if __name__ == '__main__':
    main()

