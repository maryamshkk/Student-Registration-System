class student:   
    def __init__(self,fname,lname,id,department,age):

        self.fname=fname
        self.lname=lname
        self.id=id
        self.department=department
        self.age=age
        self.email=fname+'.'+lname +'@gmail.com'

        

    def get_id(self):
        return self.id

    def get_name(self):
        print(f" NAME:                |",self.fname, self.lname)
        
    def get_department(self):
        print(f" DEPARTMENT:          |",self.department)
        
    def get_age(self):
        print(f' AGE:                 |',self.age)
        
    def get_email(self):
        print(f" EMAIL:               |",self.email)

    def set_fname(self,fname):
        self.fname=fname
        self.email=fname + '.' + self.lname + '@gmail.com'
        print()

    def set_lname(self,lname):
        self.lname=lname
        self.email=self.fname + '.' + lname + '@gmail.com'