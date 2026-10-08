'''a=10
b=0
try:
  print(a/b)

  try:
    print(a/2)

  except:
    print("No error")

except:
  print("No error1")
  

a=10
b=0
try:
  print(a/2)

  try:
    print(a/b)

  except ZeroDivisionError:
    print("Handling")

except:
  print("No error1")
  
a=10
b=0
try:
  print(a/2)

  try:
    print(a/b)

  except ZeroDivisionError:
    print("Handling")

except:
  print("No error1")

else:
  print("step1")

finally:
  print("Finally-done")
  
a=10
b=0
try:
  print(a/2)

  try:
    print(a/3)

  except:
    print("Handling")

except:
  print("No error1")

else:
  print("step1")

finally:
  print("Finally-done")
  
a=10
b=0
try:
  print(a/2)

  try:
    print(a/3)

  except:
    print("Handling")

  else:
    print("step2")

  finally:
    print("Finally-done-done")

except:
  print("No error1")

else:
  print("step1")

finally:
  print("Finally-done")

a=10
b=0
try:
  print(a/2)

  try:
    print(a/0)

  except:
    print("Handling")

  else:
    print("step2")

  finally:
    print("Finally-done-done")

except:
  print("No error1")

else:
  print("step1")

finally:
  print("Finally-done")

a=10
b=0
try:
  print(a/c)

  try:
    print(a/0)

  except:
    print("Handling")

  else:
    print("step2")

  finally:
    print("Finally-done-done")

except:
  print("Handling done")

else:
  print("step1")

finally:
  print("Finally-done")
  
class PENERROR (BaseException):
  ...

def demo(a):
  if a>0:
    print("+ve Number")

  else:
    raise PENERROR

demo(-10)



class InvalidAgeError(Exception):
    pass

age = -5
if age < 0:
    raise InvalidAgeError("Age cannot be negative")

'''