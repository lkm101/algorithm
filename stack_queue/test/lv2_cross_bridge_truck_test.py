import sys, os, time
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from lv2_cross_bridge_truck import solution, solution2

class TestClothes(unittest.TestCase):
  def test1(self):
    params1 = 2
    params2 = 10
    params3 = [7,4,5,6]
    expect = 8
    start = time.time()
    result = solution(params1, params2, params3)
    end = time.time()
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print(f'Rsult: %s ({end - start:.5f} sec)\n' %('SUCCESS' if expect == result else 'FAILED'))
  
  def test2(self):
    params1 = 100
    params2 = 100
    params3 = [10]
    expect = 101
    start = time.time()
    result = solution(params1, params2, params3)
    end = time.time()
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print(f'Rsult: %s ({end - start:.5f} sec)\n' %('SUCCESS' if expect == result else 'FAILED'))

  def test3(self):
    params1 = 100
    params2 = 100
    params3 = [10,10,10,10,10,10,10,10,10,10]
    expect = 110
    start = time.time()
    result = solution(params1, params2, params3)
    end = time.time()
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print(f'Rsult: %s ({end - start:.5f} sec)\n' %('SUCCESS' if expect == result else 'FAILED'))
  
  def test4(self):
    params1 = 666
    params2 = 444
    params3 = [121, 331, 353, 154, 1, 422, 7, 8, 10, 120]
    expect = 3998
    start = time.time()
    result = solution2(params1, params2, params3)
    end = time.time()
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print(f'Rsult: %s ({end - start:.5f} sec)\n' %('SUCCESS' if expect == result else 'FAILED'))

  def test5(self):
    params1 = 11
    params2 = 111
    params3 = [11, 1, 111, 11, 1, 1, 1, 111, 1, 111, 11, 11, 11, 1]
    expect = 85
    start = time.time()
    result = solution2(params1, params2, params3)
    end = time.time()
    print('Input > %s, %s, %s' %(params1, params2, params3))
    print('Expect > %s' %(expect))
    self.assertEqual(result, expect)
    print(f'Rsult: %s ({end - start:.5f} sec)\n' %('SUCCESS' if expect == result else 'FAILED'))

if __name__ == '__main__':
  unittest.main()