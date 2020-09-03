def fun(a):
  i = 10
  return i + a       # Noncompliant
  i += 1             # this is never executed
