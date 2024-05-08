def solution(participant, completion):
  answer = ''
  
  hashDict = {}
  sumHash = 0

  for part in participant:
    hashDict[hash(part)] = part
    sumHash += hash(part)
  
  for comp in completion:
    sumHash -= hash(comp)
  
  answer = hashDict[sumHash]
  
  return answer