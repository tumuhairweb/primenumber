import unittest
from primenumbers import primenumbers,checkPrime

class PrimeNumberTest(unittest.TestCase):
	
	def test_isPrime_function_returns_correct_result(self):
		result = checkPrime(23)
		self.assertEqual(True, result)
		
	def test_primes_returns_correct_result(self):
		result = primenumbers(20)
		self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], result)

	def test_primes_function_returns_list(self):
		result = primenumbers(20)
		self.assertIsInstance(result, list)

	def test_primes_function_returns_error_if_arg_not_integer(self):
		result = primenumbers(20)
		self.assertRaises(TypeError, primenumbers, 'string')

	def test_primes_function_returns_error_if_arg_negative_number(self):
		self.assertRaises(ValueError, primenumbers, -20)

	def test_isPrime_function_returns_bool(self):
		result = checkPrime(23)
		self.assertIsInstance(result, bool)

				
if __name__ == '__main__':
    unittest.main()