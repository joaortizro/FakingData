from faker import Faker
import random
import pprint
import json

factory = Faker()
pp = pprint.PrettyPrinter(indent=2)


def dummyProblemObject():
    problemObject = {}
    problemObject.update(id=factory.pyint(min_value=1, max_value=100, step=1))
    problemObject.update(title=factory.text())
    problemObject.update(description=factory.text())
    problemObject.update(topic=1)
    problemObject.update(user=1)
    return problemObject


def dummyNumeralObject(problem_id):
    numeralObject = {}
    numeralObject.update(id=factory.pyint(min_value=1))
    numeralObject.update(question=factory.text())
    numeralObject.update(number=factory.pyint(min_value=1, max_value=10, step=1))
    numeralObject.update(math_type=factory.pyint(min_value=1, max_value=2, step=1))
    numeralObject.update(problem_id=problem_id)
    if numeralObject["math_type"] == 1:
        numeralObject.update(solve=dummySolveObject())
    elif numeralObject["math_type"] == 2:
        numeralObject.update(simplify=dummySimplifyObject())
    return numeralObject


def arrayOfObjects():
    array = []
    for i in range(random.randint(1, 10)):
        obj = {}
        obj.update(id=factory.pyint(min_value=1, step=1))
        obj.update(latex=factory.text())
        array.append(obj)
    return array


def dummySolveObject():
    solveObject = {}
    solveObject.update(unknow_variable=arrayOfObjects())
    solveObject.update(starting_expression=arrayOfObjects())
    return solveObject


def dummySimplifyObject():
    simplifyObject = {}
    simplifyObject.update(target=factory.text())
    simplifyObject.update(reference=factory.text())


problemObject = dummyProblemObject()
num = dummyNumeralObject(problem_id=problemObject["id"])
problemObject.update(numerals=[num])

pp.pprint(problemObject)

with open("problem.json", "w") as f:
    json.dump(problemObject, f)
