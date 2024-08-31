transitions = {}

states = []
inputStates = input().split()
for i in inputStates:
  states.append(i)

start = input()

accStates = []
inputAccStates = input().split()
for i in inputAccStates:
  accStates.append(i)

data = []
inputDatas = input().split()
for i in inputDatas:
  data.append(i)

for state in states:
  inputTransitionState = input().split()
  transitions[state] = {data[0]: inputTransitionState[1], data[1]: inputTransitionState[2]}

mistery = input().split()
current = start

for attempt in mistery:
  for char in attempt:
    if char not in attempt:
      print("char inválido")
      break
    current = transitions[current][char]
  
  if current in accStates:
    print("aceita")

  else:
    print("rejeita")

  current = start
