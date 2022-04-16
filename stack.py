class stack:
    def __init__(self):
        self.a=[]
    def push(self,data):
       return  self.a.append(data)
    def pop(self):
        return self.a.pop()
    def is_empty(self):
        if len(self.a)==0:
            return True
    def get_min(self,s=[]):
        b=[]

        i=0
        n=len(s)
        while s!=[]:
            top = self.pop()
            print(top)
            if top<s[-1]:
                b.append(top)
                top=None
            else:
                b.append(s[-1])
                
                self.pop()


        return b




s1=stack()
s1.push(4)
s1.push(8)
s1.push(3)
s1.push(1)
s1.push(9)

print(s1.a)
print(s1.get_min(s1.a))
