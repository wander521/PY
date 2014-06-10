import arcpy
mxd = arcpy.mapping.MapDocument(r"E:\3.4 data\mxd�����ĵ�\goal\����ר��3.mxd")
mxd.findAndReplaceWorkspacePaths(r"I:\mxd�����ĵ�\goal", r"E:\3.4 data\mxd�����ĵ�\goal", False)
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "SYS.roa_4m":
        lyr.replaceDataSource(r"E:\3.4 data\mxd�����ĵ�\goal", "SHAPEFILE_WORKSPACE", "roa_4m",False)
        lyr.name = "����"
mxd.saveACopy(r"E:\3.4 data\mxd�����ĵ�\goal\X9.mxd")
del mxd
