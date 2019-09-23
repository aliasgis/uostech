import pynmea2
msg = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
print(msg)
print('{0} is {1}'.format('latitude', msg.latitude))
print('{0} is {1}'.format('longitude', msg.longitude))
print('{0} is {1}'.format('satelitenum', msg.num_sats))
print('{0} is {1}'.format('time', msg.timestamp))
