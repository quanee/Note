
class SharedData:
    spam = 44


x = SharedData()
y = SharedData()

print(x.spam, y.spam)
SharedData.spam = 55
print(x.spam, y.spam, SharedData.spam)
x.spam = 66