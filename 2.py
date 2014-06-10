import arcpy,os
mxd = arcpy.mapping.MapDocument(r"E:\newdata\CZT\水利设施图.mxd")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyr in arcpy.mapping.ListLayers(mxd, "", df):
        if lyr.isBroken == True:
            print lyr.name
        if lyr.visible == False:
            print lyr.name

