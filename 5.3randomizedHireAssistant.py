lst = []# list of candidates will come here 
random.shuffle(lst)
best = 0 
for i in lst : 
  if lst[i]>best :
    best = lst[i]
return best 
