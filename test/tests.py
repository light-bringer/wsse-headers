# Python code to demonstrate working of unittest 
import unittest
import WsseHeaders

class TestUtilsMethods(unittest.TestCase): 
		
	def test_import(self):
		'''
		check for initializing as None
		'''
		try:
			a = WsseHeaders.WsseToken("None",None,None)
			self.assertEqual(1, 0)
			print(type(a))
		except Exception as e:
			print(e)
			if type(e) is ValueError:
				self.assertEqual(1, 1)
			else:
				self.assertEqual(1, 0)
			


class TestWSSEMethods(unittest.TestCase): 
	
	def test_check_init(self):
		'''
		check for return type STRING
		'''
		try:
			a = WsseHeaders.WsseToken("Debapriya","yodebu","YmFzZTY0c3R0cmluZw==", True)
			print(type(a))
			self.assertEqual(str(""), a.generateHeaders())
			
		except Exception as e:
			print(e)
			if type(e) is ValueError:
				self.assertEqual(1, 1)
			else:
				self.assertEqual(1, 0)

testSuite = unittest.TestSuite()


if __name__ == '__main__': 
	unittest.main()