# -*- coding: utf-8 -*-
import arcpy,os
from arcpy import env
#将数据添加到mxd文件中去：1.将数据导出一个lyr文件；2.将全部lyr文件添加到mxd文件中去  
def CheckAll(folder,guidemap,serviceName):  
    print "检查文件夹路径……"  
    if os.path.isdir(folder) == False:  
        print "输入的文件夹路径无效！"  
        return  
    print "遍历文件夹……"  
    files = os.listdir(folder)  
    for f in files:  
        if f.endswith(".tif"):  
            tifPath = os.path.join(folder, f)  
            print "Add: " + f  
            LayerTif(tifPath)  
        else:  
            continue
    del f,files
    SelLayer(folder,serviceName,guidemap)

def LayerTif(tifPath):  
    #检查文件是否存在  
    print "路径有效！正在检查文件夹是否存在TIF数据……"  
    if os.path.exists(tifPath) == False:  
        print "指定路径的tif数据不存在！"  
        return       
    # 创建.lyr文件  
    try:
        print "构建影像金字塔"
        arcpy.BuildPyramids_management(tifPath)
#        print "我去年买了表"
#        arcpy.env.cellSize = tifPath
#        print arcpy.env.cellSize         
        name, ext = os.path.splitext(tifPath)
        RDlyr = name +".lyr"
        arcpy.MakeRasterLayer_management(tifPath,name,"","","")  
        arcpy.SaveToLayerFile_management(name, RDlyr, "RELATIVE")
    except Exception, e:  
        print "error: ", e  
        return  
    else:
        del name,ext
        print "layer文件创建成功……" 


#获取文件夹内所有的.lyr文件
def SelLayer(folder,serviceName,guidemap):
    # 需要在该文件夹内建立一个引导文件。
    mxd = arcpy.mapping.MapDocument(guidemap)
    # 获得data frame
    df = arcpy.mapping.ListDataFrames(mxd,"*")[0]    
    files = os.listdir(folder)  
    for f in files:  
        if f.endswith(".lyr"):  
            lyrPath = os.path.join(folder, f)  
            print "AddLayer: " + f  
            AddLayer(lyrPath,df)
        if f.endswith(".shp"):  
            shpPath = os.path.join(folder, f)  
            print "AddLayer: " + f  
            Addshp(shpPath,df)        
        else:  
            continue
    mxd.saveACopy(serviceName)
    del mxd,df,f,files
    print "为毛老纸不能显示"    
        
def AddLayer(lyrPath,df):  
      
    # 将lyr添加到mxd中 
    try:  
        newlayer = arcpy.mapping.Layer(lyrPath)
        arcpy.mapping.AddLayer(df,newlayer,"AUTO_ARRANGE")
    except Exception, e:  
        print "error: ", e  
        return  
    else:
        del newlayer
        print "成功添加一个"
        
def Addshp(shpPath,df):  
      
    # 将shp添加到mxd中 
    try:  
        newlayer = arcpy.mapping.Layer(shpPath)
        arcpy.mapping.AddLayer(df,newlayer,"AUTO_ARRANGE")
    except Exception, e:  
        print "error: ", e  
        return  
    else:
        del newlayer
        print "成功添加一个"





  
