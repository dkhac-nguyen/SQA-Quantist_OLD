﻿import Load_CSV_File 
import Quantist_Removing_Files

def Remove_Outliers():
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.delete_Button
  
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files()
  
  if (not treeView.HasItems):
    Load_CSV_File.Import_Data_File(ProjectSuite.Variables.SampleDataFolder, "TestData.csv")

    ProjectSuite.Variables.Short_Delay    
    Regions.DataPoints_B7_H1_5PL_1Ysq_80_120.Check(Aliases.Quantist.MainWindowView.MainView.ListControl)

    # DataPoints - Clicked on current Curve Remove Outliers Recovery Range 90-110% 
    border = Aliases.Quantist.MainWindowView.MainView
    border.RecoveryRangeBox.ClickItem("From90To110")
    border.RemoveOutlier_CurrentCurve_Btn.ClickButton()
    Regions.DataPoints_B7_H1_5PL_1Ysq_90_110_RemoveOutliers.Check(Aliases.Quantist.MainWindowView.MainView.ListControl)

    # Reset Include Standard button should bring back DataPoints as before Remove Outliers
    ProjectSuite.Variables.Short_Delay    
    border = Aliases.Quantist.MainWindowView.MainView
    border.ButtonStandards.ClickButton()
    border.RecoveryRangeBox.ClickItem("From80To120")
    Regions.DataPoints_B7_H1_5PL_1Ysq_80_120.Check(Aliases.Quantist.MainWindowView.MainView.ListControl)
          


