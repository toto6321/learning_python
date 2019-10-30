import math


# author: TTH
# date: 2019/10/25

class MajorRules():
	"""
	p -> probability of an event for single experiment
	n -> number of experiment 
	tp -> expected minimum probility
	"""
	def __init__(self, p=1, n=1, tp=1):
		self.p=p
		self.n=n
		self.tp=tp


	def get_overall_p(self):
		try:
			# combination
			sum_p = 0
			t = math.ceil(self.n/2) if self.n%2 != 0 else (self.n//2+1)
			for i in range(t,self.n+1):
				p_i = self.caculate_p_of_a_combination(i, self.n, self.p)
				sum_p += p_i
				# print(f"combiantion {i}/{self.n} has probability of {p_i}")
			return sum_p	
		except Exception as e:
			print(e)


	def get_min_n(self):
		while self.get_overall_p() < self.tp:
			self.n +=1
		return self.n


	def caculate_p_of_a_combination(self,c=1,n=1,p=1):
		if n>0 and 0 <= c <= n and 0<= p <=1:
			# accumulate possiblities
			combination = (math.factorial(n)/math.factorial(n-c)/math.factorial(c))
			p_i = combination * (p**c) * ((1-p)**(n-c))
			# print(str(combination)+"*"+str(p)+"^"+str(c)+"*"+str(1-p)+"^"+str(n-c))
			return p_i
		else:
			raise Execption("Invalid parameters!")


if __name__ == "__main__":

	# 单个概念为0.55, 人数为7, 求总概率　
	# 60.829%
	a = MajorRules(p=0.55, n=7)
	print(a.get_overall_p())


	# 单个概念为0.55, 期望最低概率为90%, 求所需最少人数
	# 163
	b = MajorRules(p=0.55, tp=0.90)
	print(b.get_min_n())