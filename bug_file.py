def fun(a):
  i = 5 
  return i + a       # Noncompliant
  i += 1             # this is never executed
