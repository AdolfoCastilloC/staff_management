# Staff class
import random

class Staff(object):
    def __init__(self, id_number):
        self.id = id_number
        self.age = random.randint(18,40)
        self.gender = random.sample(["Male", "Female"],1).pop()


class Position():
    def __init__(self, job_code, level):
        self.job_coda = job_code
        self.level = level
        




if __name__=="__main__":
    employee = Staff("80214583")
    print("Age:",employee.age)
    print("Gender:", employee.gender)
