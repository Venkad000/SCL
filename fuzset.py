import numpy as np

class f_set:
    def __init__(self,se):
        self.se = {}
        if type(se) != type(dict()):
            for i in se:
                if i[0] in self.se:
                    self.se[i[0]] = max(self.se[i[0]],i[1])
                else:
                    self.se[i[0]] = i[1]
        else:
            self.se = se
            
    def add(self, i):
        if i[0] in self.se:
            self.se[i[0]] = max(self.se[i[0]],i[1])
        else:
            self.se[i[0]] = i[1]
    
        
        
    def remove(self,ele):
        tmp = self.se.pop(ele)
        return tmp
        
    def __str__(self):
        return str(self.se) 
    
    def __add__(self,se2):
        se2 = se2.se
        tmp = self.se.copy()
        for i in se2.items():
            if i[0] in tmp:
                tmp[i[0]] = max(tmp[i[0]],i[1])
            else:
                tmp[i[0]] = i[1]
        return f_set(tmp)
    
    def __sub__(self,se2):
        se2 = se2.se
        tmp = self.se.copy()
        for i in se2.items():
            if i[0] in tmp:
                tmp[i[0]] = round(min(tmp[i[0]],1 - i[1]),6)
            else:
                tmp[i[0]] = i[1]
        return f_set(tmp)
    
    def intersection(self,se2):
        se2 = se2.se
        tmp = self.se.copy()
        for i in se2.items():
            if i[0] in tmp:
                tmp[i[0]] = min(tmp[i[0]],i[1])
            else:
                tmp[i[0]] = i[1]
        return f_set(tmp)

    def complement(self):
        tmp = self.se.copy()
        for i in tmp.items():
                tmp[i[0]] = round(1 - i[1],6)
        return f_set(tmp)
    def cart_pro(self, se2):
        se2 = se2.se
        
        fin = [[(i[0],j[0],min(j[1],i[1])) for j in se2.items()] for i in self.se.items()]
        return fin
    
    @staticmethod
    def min_max(r, s):
        rx_l = len(r)
        sx_l = len(s)
        sy_l = len(s[0])
        
        fin = [[0 for i in range(sy_l)] for j in range(rx_l)]
        
        #print(fin)
        for i in range(rx_l):
            for j in range(sy_l):
                tmp = []
                for k in range(sx_l):
                     tmp.append((r[i][k][0],s[k][j][1],min(r[i][k][2], s[k][j][2])))
                fin[i][j] = max(tmp, key = lambda x: x[2])
                
        return fin
    
if __name__ == "__main__":
    a = [(2,1),(3,0.4),(1,0.6),(4,0.2)]
    b = [(2,0),(3,0.2),(1,0.2),(4,0.8)]
    
    te1 = f_set(a)
    te2 = f_set(b)
    print(te1)
    print(te2)
    
    
    print("INTERSECTION\n",te1.intersection(te2)) #INTERSECTION
    print("UNION\n",te1 + te2) #UNION
    print("COMPLEMENTS : \n",te1.complement(), te2.complement()) #COMPLEMENT
    print("DIFFERENCE\n",te1 - te2) #DIFFERECE
    print("DEMORGANS")
    print(te1.intersection(te2).complement(),te1.complement() + te2.complement())
    print((te1+te2).complement(),te1.complement().intersection(te2.complement()))
    
    #CARTESIAN PRODUCT
    a = [(2,1),(3,0.4),(1,0.6),(4,0.2)]
    b = [(5,0),(7,0.2),(6,0.2),(8,0.8)]
    c = [(2,0.5),(3,0.6),(1,0.1),(4,0.9)]
    
    te1 = f_set(a)
    te2 = f_set(b)
    te3 = f_set(c)
    
    print("\n\n~A : ", te1,"\n~B : ", te2 ,"\n~C : ", te3)
    
    print("\nCATESIAN PRODUCT ~R : \n")
    for i in te1.cart_pro(te2):
        for j in i:
            print(j, end =" ")
        print()
    
    
    print("\nCATESIAN PRODUCT ~S : \n")
    for i in te1.cart_pro(te3):
        for j in i:
            print(j, end =" ")
        print()
        
    print("\nMIN MAX COMPOSITION : \n")
    
    for i in f_set.min_max(te1.cart_pro(te2),te1.cart_pro(te3)):
        for j in i:
            print(j, end =" ")
        print()
        
    print("\n\n")
    r = [[('x1','y1',0.5),('x1','y2',0.1)],[('x2','y1',0.2),('x2','y2',0.9)],[('x3','y1',0.8),('x3','y2',0.6)]]
    s = [[('y1','z1',0.6),('y1','z2',0.4),('y1','z3',0.7)],[('y2','z1',0.5),('y2','z2',0.8),('y2','z3',0.9)]]
    print("r : \n",r,"\ns : \n", s,"\n")

    for i in f_set.min_max(r,s):
        for j in i:
            print(j, end =" ")
        print()
    