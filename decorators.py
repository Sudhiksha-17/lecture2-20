def announce(f):
     def wrapper():
         print("Announce to run")
         f()
          print("Done")
return Wrapper

@announce
def hello():
print("Hello World")
hello()s

 