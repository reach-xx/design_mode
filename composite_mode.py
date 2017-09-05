"""
###                                      公司组织架构图
###               总公司
###      ------------------------------
###      |       |      |       |
###     HR部门  财务部  研发部   东部分公司
###                     -----------------------------------------------------
###                     |      |       |                |                   |
###                  东分HR  东分财务 东分研发         东南分公司            东北分公司
###                                          -------------------     -----------------
###                                          |        |        |     |       |       |
###                                          HR     财务部    研发部   HR     财务部  研发部
"""

class Company(object):
    def add(self):
        pass

    def remove(self):
        pass

    def display(self):
        pass

    def listduty(self):
        pass


class ConcreteCompany(Company):
    def __init__(self, name):
        self.name = name
        self.company_list=[]

    def add(self,company):
        self.company_list.append(company)

    def remove(self, company):
        self.company_list.remove(company)

    def display(self,depth):
        print('-'*depth, self.name)
        for component in self.company_list:
            if isinstance(component, ConcreteCompany):
                component.display(depth+1)
            else:
                component.display(depth*2)

    def listduty(self):
        for component in self.company_list:
            component.listduty()


class HRDepartment(Company):
    def __init__(self, name):
        self.name = name

    def display(self, depth):
        print('-'*depth, self.name)

    def listduty(self):
        print("HRDepartment:" ,self.name)


class FinanceDepartment(Company):
    def __init__(self, name):
        self.name = name

    def display(self,depth):
        print('-'*depth, self.name)

    def listduty(self):
        print("FinanceDepartment:", self.name)


class RDDepartment(Company):
    def __init__(self, name):
        self.name = name

    def display(self,depth):
        print('-'*depth, self.name)

    def listduty(self):
        print("RDDepartment:", self.name)

if __name__ == '__main__':
    root = ConcreteCompany('HeadQuarter')
    root.add(HRDepartment('HQ HR'))
    root.add(FinanceDepartment('HQ Finance'))
    root.add(RDDepartment('HQ R&D'))

    comp1 = ConcreteCompany('East Branch')
    comp1.add(HRDepartment('EB HR'))
    comp1.add(FinanceDepartment('EB Finance'))
    comp1.add(RDDepartment('EB R&D'))
    root.add(comp1)

    comp2 = ConcreteCompany('SouthEast Branch')
    comp2.add(HRDepartment('SEB HR'))
    comp2.add(FinanceDepartment('SEB Finance'))
    comp2.add(RDDepartment('SEB R&D'))
    comp1.add(comp2)

    comp3 = ConcreteCompany('NorthEast Branch')
    comp3.add(HRDepartment('NEB HR'))
    comp3.add(FinanceDepartment('NEB Finance'))
    comp3.add(RDDepartment('NEB R&D'))
    comp1.add(comp3)

    root.display(2)

    root.listduty()


