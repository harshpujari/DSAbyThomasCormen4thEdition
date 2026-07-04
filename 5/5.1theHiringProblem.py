def theHiringProblem(n):
  best = 0 
  for i in range (0,n) :
    if i > best :
      best = i
  return best
