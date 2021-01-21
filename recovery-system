Process Starts after x minutes of flight

With GGA Output
If (GPS Altitude % 10 == Previous State)
   if (Timer == 20 seconds)
      Stop other functions();
      Start Sending Data Through XBee();
      break from loops
   else
      continue;
Else
   Previous State = GPS Altitude % 10
   Reset Timer


With RMC Output
If (Velocity == 0)
    Stop other functions
    Start Sending Data Through XBee
    break from loop
Else
   continue checking
