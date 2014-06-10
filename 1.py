import arcpy
mxd = arcpy.mapping.MapDocument(r"E:\3.4 data\mxd测试文档\goal\测试专题3.mxd")
mxd.findAndReplaceWorkspacePaths(r"I:\mxd测试文档\goal", r"E:\3.4 data\mxd测试文档\goal", False)
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "SYS.roa_4m":
        lyr.replaceDataSource(r"E:\3.4 data\mxd测试文档\goal", "SHAPEFILE_WORKSPACE", "roa_4m",False)
        lyr.name = "中文"
mxd.saveACopy(r"E:\3.4 data\mxd测试文档\goal\X9.mxd")
del mxd
