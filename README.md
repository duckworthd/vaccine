Vaccine
=======

Vaccine is a tiny dependency injection framework for Python.


Usage
=====

At Vaccine's core is an instance of `vaccine.Vaccine`. Think of `Vaccine` as a
dict that automatically builds things for you as necessary. Begin by instantiating a single, global instance of `Vaccine`

```Python
i = Vaccine()
```

Next, register classes and functions as requiring and providing dependencies
with `Vaccine.requires` and `Vaccine.provides` (make sure `provides` appears
before `requires`!).


```Python
class SomeServiceInterface(object):
  pass


# register this class as providing for some interface and requiring some
# dependencies (this time, keyed on strings)
@i.provides(SomeServiceInterface)                   # you can uses interfaces as keys...
@i.requires(host="HOST", credentials="CREDENTIALS") # or just strings
class SomeService(SomeServiceInterface):

  def __init__(self, host, credentials):
    print '<SomeService>'
    self.host = host
    self.credentials =  credentials

  def hello_world(self):
    print "Logging into: {}".format(self.host)
    print "Username: {}".format(self.credentials['user'])
    print "Password: {}".format(self.credentials['password'])


# In addition to classes, you can also annotate functions with `provides` and
# `requires`.
@i.provides("CREDENTIALS")
def credentials():
  print '<credentials>'
  import os
  return {"user": os.environ["USER"], "password": "XXXX"}

# rather than registering a providing function/class that provide for a key,
# you can register already-instantiated values directly.
i.register("HOST", "localhost")
```

Finally, use `Vaccine.get(key)` to retrieve already-built dependencies. Each
key will only be called once.

```Python
# manually retrieving an instantiation is as sample as calling `get`. All
# dependencies will be handled automatically.
service = i.get(SomeServiceInterface)
service.hello_world()

# keys are only instantiated once
service2 = i.get(SomeServiceInterface)
service is service2   # True
```
