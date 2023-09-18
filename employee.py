class Employee:
    def __init__(self, id, shift_availability, absenteeism):
        self.id = id
        self.shift_availability = shift_availability
        self.absenteeism = absenteeism
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def has_skill(self, skill):
        return skill in self.skills

    def is_available(self, shift):
        return self.shift_availability == shift

    def get_absenteeism(self):
        return self.absenteeism

