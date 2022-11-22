from Comms import Comms

c = Comms()

# Toss a coin
c.send("hot()")
print(c.receive())

# Generate OTP
# c.send("otp()")
# print(c.receive())

# Close connection to serial
c.close()
