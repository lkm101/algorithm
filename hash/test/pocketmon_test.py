import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from pocketmon import solution

class TestPocketmon(unittest.TestCase):
  def test_solution1(self):
    nums = [3, 1, 2, 3]
    expect_result = 2
    result = solution(nums)
    self.assertEqual(result, expect_result)
    print('[TEST CASE 1]')
    print('nums: [' + ','.join(str(num) for num in nums) + ']')
    print('expect: %d, receive: %d, result: %r\n' %(expect_result, result, expect_result == result) )
  
  def test_solution2(self):
    nums = [3, 3, 3, 2, 2, 4]
    expect_result = 3
    result = solution(nums)
    self.assertEqual(result, expect_result)
    print('[TEST CASE 2]')
    print('nums: [' + ','.join(str(num) for num in nums) + ']')
    print('expect: %d, receive: %d, result: %r\n' %(expect_result, result, expect_result == result) )
  
  def test_solution3(self):
    nums = [3, 3, 3, 2, 2, 2]
    expect_result = 2
    result = solution(nums)
    self.assertEqual(result, expect_result)
    print('[TEST CASE 3]')
    print('nums: [' + ','.join(str(num) for num in nums) + ']')
    print('expect: %d, receive: %d, result: %r\n' %(expect_result, result, expect_result == result) )

if __name__ == '__main__':
  unittest.main()