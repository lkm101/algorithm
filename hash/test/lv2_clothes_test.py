import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from lv2_clothes import solution

class TestMarathone(unittest.TestCase):
  def test_solution1(self):
    params1 = 	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    expect = 5
    result = solution(params1)
    self.assertEqual(result, expect)
    print('[TEST CASE 1]')
    print('clothes: [' + ','.join(str(param) for param in params1) + ']')
    print('expect: %d, receive: %d, result: %r\n' %(expect, result, expect == result) )
  
  def test_solution1(self):
    params1 = 	[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    expect = 3
    result = solution(params1)
    self.assertEqual(result, expect)
    print('[TEST CASE 2]')
    print('clothes: [' + ','.join(str(param) for param in params1) + ']')
    print('expect: %d, receive: %d, result: %r\n' %(expect, result, expect == result) )

if __name__ == '__main__':
  unittest.main()