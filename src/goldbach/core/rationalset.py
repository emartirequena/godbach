from goldbach.core.rationals import Rational


class RationalSet(object):
	"""Base class for the rational set of a number on a given base
	It stores all the rationals formed with the number as denominator

	Args:
		n (int): number for the rational set
		base (int): base for the rationals
	"""
	def __init__(self, n, base):
		self.n = n
		self.base = base
		self.rationalset = []
		self.groups = []
		r = Rational(1, n, base)
		if r.getPeriod() == 0 or not r.isPurePeriod():
			return

		rlist = range(self.n + 1)
		while rlist:
			group = []
			rgroup = Rational(rlist[0], self.n, self.base)
			for m in rgroup.getReminders():
				r = Rational(m, self.n, self.base)
				self.rationalset.append(r)
				group.append(r)
				rlist.remove(m)
			self.groups.append(group)

	def getPeriod(self):
		"""Returns de maximum period for n in the base

		Returns:
			(int): period of n in the base
		"""
		if not self.groups:
			return 0
		return self.groups[1][0].getPeriod()

	def output(self):
		for group in self.groups:
			print len(group)
			for r in group:
				print r.m, r.n, r.getDigits()


if __name__ == '__main__':
	rset = RationalSet(25, 16)
	rset.output()
