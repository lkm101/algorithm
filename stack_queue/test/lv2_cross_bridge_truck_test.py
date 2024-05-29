import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from lv2_cross_bridge_truck import solution

class TestClothes(unittest.TestCase):
  def test_solution1(self):
    params1 = 2
    params2 = 10
    params3 = [7,4,5,6]
    expect = 8
    result = solution(params1, params2, params3)
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print('Rsult: %s\n' %('SUCCESS' if expect == result else 'FAILED'))
  
  def test_solution2(self):
    params1 = 100
    params2 = 100
    params3 = [10]
    expect = 101
    result = solution(params1, params2, params3)
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print('Rsult: %s\n' %('SUCCESS' if expect == result else 'FAILED'))

  def test_solution3(self):
    params1 = 100
    params2 = 100
    params3 = [10,10,10,10,10,10,10,10,10,10]
    expect = 110
    result = solution(params1, params2, params3)
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print('Rsult: %s\n' %('SUCCESS' if expect == result else 'FAILED'))

if __name__ == '__main__':
  unittest.main()