import gpxpy 
import gpxpy.gpx 

gpx_file = open('E:\kuhkopfsteig-fv.gpx', 'r') 
gpx = gpxpy.parse(gpx_file) 
for track in gpx.tracks: 
 for segment in track.segments: 
  for point in segment.points: 
   print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation) 
for waypoint in gpx.waypoints: 
  print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude) 
for route in gpx.routes: 
 print 'Route:{0}'.format(route.name)