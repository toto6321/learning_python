
import math

# author: TTH
# date: 2019/10/28
class MajorRules():
    """
    p -> probability of an event for single experiment
    n -> number of experiment 
    tp -> expected minimum probability
    """
    import numpy as np

    def __init__(self, p=1, n=1, tp=1):
        self.p=p
        self.n=n
        self.tp=tp


    def get_overall_p(self):
        try:
            # combination
            sum_p = 0
            # when there are even number people, it needs to be at least (n/2+1)
            t = math.ceil(self.n/2) if self.n%2 != 0 else (self.n//2+1)
            for i in range(t,self.n+1):
                p_i = self.caculate_p_of_a_combination(i, self.n, self.p)
                sum_p += p_i
                # print(f"combiantion {i}/{self.n} has probability of {p_i}")
            return sum_p    
        except Exce`ption as e:
            print(e)


    def get_min_n(self):
        op = self.get_overall_p()
        while op < self.tp:
            self.n +=1
            op=self.get_overall_p()
        return self.n,op

    def get_op_list(self):
        if self.n > 0 and self.tp == 1:
            n = self.n
            self.n = 1
            op = self.get_overall_p()
            op_list = [op]
            while self.n < n:
                self.n +=1
                op = self.get_overall_p()
                op_list.append(op)
            return op_list
        elif 0 < self.tp <= 1 and self.n == 1:
            op = self.get_overall_p()
            op_list = [op]
            while op < self.tp:
                self.n +=1
                op = self.get_overall_p()
                op_list.append(op)
            return op_list
        else:
            raise Exception("Invalid parameters!")



    def caculate_p_of_a_combination(self,c=1,n=1,p=1):
        if n>0 and 0 <= c <= n and 0<= p <=1:
            # accumulate possiblities
            combination = (math.factorial(n)/math.factorial(n-c)/math.factorial(c))
            p_i = combination * (p**c) * ((1-p)**(n-c))
            # print(str(combination)+"*"+str(p)+"^"+str(c)+"*"+str(1-p)+"^"+str(n-c))
            return p_i
        else:
            raise Exception("Invalid parameters!")


if __name__ == "__main__":

    # 单个概率为0.55, 人数为7, 求总概率　
    # 60.829%
    a = MajorRules(p=0.55, n=7)
    print(a.get_overall_p())


    # 单个概率为0.55, 期望最低概率为90%, 求所需最少人数
    # 163
    b = MajorRules(p=0.55, tp=0.90)
    print(b.get_min_n())


    # visualize the overal probability 
    c = MajorRules(p=0.55, tp=0.90)
    op_list = c.get_op_list()
    # import matplotlib
    # matplotlib.use('tkagg')
    import matplotlib.pyplot as plt
    import numpy as np
    y = op_list
    x = list(range(1,len(op_list)+1))
    plt.plot(x, y)
    plt.show()
