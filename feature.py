import osgeo.ogr
shapefile = osgeo.ogr.Open("GP_ETC.shp")
layer = shapefile.GetLayer(0)
for i in range(layer.GetFeatureCount()):
feature =layer.GetFeature(i)
geometry = feature.GetGeometryRef()
geometry_type = geometry.GetGeometryName(()
print 'geometry ({0},{1}'.format(i, geometry_type)