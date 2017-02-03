
"""
Its hard to say if this is closures. It kind of is I guess.
"""

callbacks = []

def generate(a):
    def acallback():
        return "the value of a when I existed was %s" % a
    callbacks.append(acallback)

generate(1)
generate(2)
generate(3)

for i in callbacks:
    print i()

