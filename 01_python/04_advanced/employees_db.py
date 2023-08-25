#!/usr/bin/env python3
""" Print the number of arguments and the list of the arguments """

import cmd


class Employee:
    """ Employee class """
    __base_id = 0

    def __init__(self, name, job, salary):
        """ Employee constructor """
        self.__id = Employee.__base_id
        Employee.__base_id += 1

        self.name = name
        self.job = job
        self.salary = salary

    @property
    def id(self):
        """ Employee id (read only) """
        return self.__id

    def __str__(self):
        """ Employee string representation """
        return "ID: {} | Name: {} | Job: {} | Salary: {}".format(
            self.__id, self.name, self.job, self.salary)


class EmplyeesDB:
    """ EmployeesDB class """

    PROMPT = '> '

    def __init__(self):
        """ EmployeesDB constructor """
        self.__employees = {}

    @property
    def employees(self):
        """ Employees property """
        return self.__employees.copy()

    def add(self, employee):
        """ Add employee to database """
        if not isinstance(employee, Employee):
            raise TypeError("Employee must be an instance of Employee")
        self.__employees[employee.id] = employee

    def remove(self, id):
        """ Remove employee from database """
        del self.__employees[id]

    def print(self, id):
        """ Print employee from database """
        employee = self.__employees[id]
        print(employee)


class EmployeesCLI(cmd.Cmd):
    """ EmployeesCLI class """

    def __init__(self, emp_db):
        """ EmployeesCLI constructor """
        cmd.Cmd.__init__(self)
        self.emp_db = emp_db

    def do_add(self, args):
        """ Add employee to database """

        try:
            name, job, salary = args.strip().split(' ')[0:3]
        except Exception:
            print('Invalid command usage: add <name> <job> <salary>')
            return

        try:
            salary = float(salary)
        except Exception:
            print('Salary must be a number')
            return

        employee = Employee(name, job, salary)
        self.emp_db.add(employee)
        print(f'saved with id: {employee.id}')

    def help_add(self):
        """ The add command documentation """
        print('Usage: add <name> <job> <salary>')

    def do_remove(self, id):
        """ Remove employee from database """
        self.emp_db.remove(int(id))
        print(f'removed with id: {id}')

    def help_remove(self):
        """ The remove command documentation """
        print('Usage: remove <id>')

    def do_print(self, id):
        """ Print employee from database """
        self.emp_db.print(int(id))

    def help_print(self):
        """ The print command documentation """
        print('Usage: print <id>')

    def do_all(self, _):
        """ Print all employees from database """
        for employee in self.emp_db.employees.values():
            print(employee)

    def help_all(self):
        """ The all command documentation """
        print('Usage: all')

    def do_exit(self, _):
        """ Exit command """
        return True

    def help_exit(self):
        """ The exit command documentation """
        print('Usage: exit')

    def do_EOF(self, _):
        """ Exit command """
        return True


if __name__ == '__main__':
    emp_db = EmplyeesDB()
    emp_cli = EmployeesCLI(emp_db)
    emp_cli.cmdloop()
