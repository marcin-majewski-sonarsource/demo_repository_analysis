def fun(a):
  i = 1
  return i + a       # Noncompliant
  i += 1             # this is never executed
