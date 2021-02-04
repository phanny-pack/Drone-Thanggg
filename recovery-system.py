# Process Starts after x minutes of flight

# With GGA Output
# If (int(GPS Altitude) == Previous State)
#    if (Timer == 20 seconds)
#       Stop other functions();
#       Start Sending Data Through XBee();
#       break from loops
#    else
#       continue;
# Else
#    Previous State = GPS Altitude % 10
#    Reset Timer


# With RMC Output
# If (Velocity == 0)
#     Stop other functions
#     Start Sending Data Through XBee
#     break from loop
# Else
#    continue checking




#Reporting GPS to Terminal
import gps
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        if report['class'] == 'TPV':
            if hasattr(report, 'speed'):
                print(report.speed)
            if hasattr(report, 'lon'):
                print(report.lon)
            if hasattr(report, 'lat'):
                print(report.lat)
            if hasattr(report, 'alt'):
                print(report.alt)
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")


