def foo(avar):
    def bar():
        return "The variable avar was \
                this value when I was created %s" % avar
    return bar

results = []
for i in range(10):
    results.append(foo(i))

for x in results:
    print x()
