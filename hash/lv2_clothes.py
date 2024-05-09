# [문제 설명]
# 코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.
# 예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.
# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# [제한사항]
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

# [입출력 예]
#   clothes                                                                                       | return
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]      | 5
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]                  | 3

# [입출력 예 설명]
# 예제 #1
# headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.
# 1. yellow_hat
# 2. blue_sunglasses
# 3. green_turban
# 4. yellow_hat + blue_sunglasses
# 5. green_turban + blue_sunglasses

def solution(clothes):
  # MN + M + N 이 계산 식
  # M(N+1) + N 에서 식을 간단하게 하기 위해 +1을 추가 
  # 때문에 answer = 1로 초기화 하고 return 할 때 -1
  # M(N+1) + N+1 = (N+1)(M+1)
  # 위 식을 코딩으로 바꾸면 answer *= (count+1)
  answer = 1

  hash_map = {}

  for cloth in clothes:
    hash_map[cloth[1]] = hash_map.get(cloth[1], 0) + 1
  
  for count in hash_map.values():
    answer *= (count+1)

  return answer - 1