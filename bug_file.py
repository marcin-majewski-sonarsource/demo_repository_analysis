def fun(a):
  i = 21
  return i + a       # Noncompliant
  i += 1             # this is never executed
