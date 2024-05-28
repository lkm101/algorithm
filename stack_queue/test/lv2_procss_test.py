import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from lv2_process import solution

class TestClothes(unittest.TestCase):
  def test_solution1(self):
    params1 = [2, 1, 3, 2]
    params2 = 2
    expect = 1
    result = solution(params1, params2)
    print('Input > %s, %s' %(params1, params2))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print('Rsult: %s\n' %('SUCCESS' if expect == result else 'FAILED'))
  
  def test_solution2(self):
    params1 = [1, 1, 9, 1, 1, 1]	
    params2 = 0
    expect = 5
    result = solution(params1, params2)
    print('Input > %s, %s' %(params1, params2))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print('Rsult: %s\n' %('SUCCESS' if expect == result else 'FAILED'))

if __name__ == '__main__':
  unittest.main()