from Comms import Comms

c = Comms()
c.send("hot()")
print(c.receive())
# c.send("otp()")
# print(c.receive())
# c.send("otp(8)")
# print(c.receive())
# c.send('2 + 2')
# c.send('on()')
# c.send('off()')
c.close()
