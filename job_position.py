class JobPosition:
    def __init__(self, id, required_skills):
        self.id = id
        self.required_skills = required_skills

    def add_required_skill(self, skill):
        self.required_skills.append(skill)

    def has_required_skill(self, skill):
        return skill in self.required_skills

    def get_required_skills(self):
        return self.required_skills

    def is_suitable_for_employee(self, employee):
        for skill in self.required_skills:
            print(f'Checking if employee has skill: {skill}')
            if not employee.has_skill(skill):
                print(f'Employee does not have skill: {skill}')
                return False
        return True
