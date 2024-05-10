import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from lv2_phonebook import solution

class TestPhonebook(unittest.TestCase):
  def test_solution1(self):
    params1 = 	["119", "97674223", "1195524421"]
    expect = False
    result = solution(params1)
    self.assertEqual(result, expect)
    print('[TEST CASE 1]')
    print('phone_book: [' + ','.join(str(param) for param in params1) + ']')
    print('expect: %s, receive: %s, result: %r\n' %(expect, result, expect == result) )
  
  def test_solution2(self):
    params1 = 	["123","456","789"]
    expect = True
    result = solution(params1)
    self.assertEqual(result, expect)
    print('[TEST CASE 1]')
    print('phone_book: [' + ','.join(str(param) for param in params1) + ']')
    print('expect: %s, receive: %s, result: %r\n' %(expect, result, expect == result) )

if __name__ == '__main__':
  unittest.main()