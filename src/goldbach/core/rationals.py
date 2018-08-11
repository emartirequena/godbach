class Rational(object):
	"""Rational number on a given base

	Args:
		m (int): numerator
		n (int): denominator
		base (int): base
	"""
	def __init__(self, m, n, base):
		self. m = m
		self.n = n
		self.base = base
		self.init_digits = []
		self.init_reminders = []
		self.digits = []
		self.reminders = []
		self._compute()

	def _compute(self):
		"""Compute digits and reminders series,
		separating non pure period initial digits.
		"""
		if self.m == 0:
			self.digits = [0]
			self.reminders = [0]
			return

		if self.m == self.n:
			self.digits = [self.base - 1]
			self.reminders = [self.m]
			return

		reminder = self.m
		digit = int(reminder * self.base / self.n)
		while True:
			self.digits.append(digit)
			self.reminders.append(reminder)
			reminder = (reminder * self.base) % self.n
			digit = int(reminder * self.base / self.n)
			if reminder in self.reminders:
				break
		index = self.reminders.index(reminder)
		if index > 0:
			self.init_digits = self.digits[:index]
			self.init_reminders = self.reminders[:index]
			if self.digits[index] > 0:
				self.digits = self.digits[index:]
				self.reminders = self.reminders[index:]
			else:
				self.digits = []
				self.reminders = []

	def getDigits(self):
		"""Returns the digits sequence

		Returns:
			(list): list of digits as integers
		"""
		return self.digits

	def getReminders(self):
		"""Returns the reminders sequence

		Returns:
			(list): list of reminders

		"""
		return self.reminders

	def isPurePeriod(self):
		"""Returns true if digits sequence has non periodic
		inital digits.

		Returns:
			(bool): True if there are no non periodic digits,
					False otherwise

		"""
		return True if len(self.init_digits) == 0 else False

	def getPeriod(self):
		"""Returns the period of the rational number in the base

		Returns:
			(int): period of m/n in the base
		"""
		return len(self.digits)


if __name__ == '__main__':
	r = Rational(1, 15, 5)
	print r.init_digits, r.digits
	print r.init_reminders, r.reminders
