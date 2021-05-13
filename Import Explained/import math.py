import math # The math module is imported to the code
print(math.pi) # When you run the code it will execute the pi value from the math module
# Note that math acts as a namespace that containes all values associated with the module together.

from math import pi
print(pi) #the following code imports only the pi value from math module when executed

#You can also rename modules as they are being imported
import math as w
print(w.pi) # Note that the namespace for math has been rewritten to a single letter word

from math import pi as applePi
print(applePi) # Here we renamed pi as applePi while it was imported 
