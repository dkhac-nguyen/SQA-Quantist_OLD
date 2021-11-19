﻿def Expanding_CSV_Files():
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Aliases.Quantist.MainWindowView.CollapseButton.ClickButton()
  Regions.RunTreeView_Collapse.Check(Aliases.Quantist.MainWindowView.RunTreeView)
    
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)  
  Aliases.Quantist.MainWindowView.ExpandingButton.ClickButton()
  Regions.RunTreeView_Expand.Check(Aliases.Quantist.MainWindowView.RunTreeView)
   
  i = 1
  while (i < 6):
    if (Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem2.WPFObject("TreeViewItem", "", i).Exists):
      Log.Message("Visible? " + aqConvert.VarToStr(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem2.WPFObject("TreeViewItem", "", i).Visible))
      Log.Message("Item: " + aqConvert.VarToStr(i) + " is in the tree view") 
    else:
      Log.Message("Visible? " + aqConvert.VarToStr(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem2.WPFObject("TreeViewItem", "", i).Visible))
    i += 1
  
    
def Expanding_Old():
  mainWindowView = Aliases.Quantist.MainWindowView
  treeView = mainWindowView.RunTreeView
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  treeView.ExpandItem("|[0]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ExpandItem("|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ExpandItem("|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ExpandItem("|[3]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Togglebutton.ClickButton(cbChecked)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[0]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[1]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[2]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[3]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  mainWindowView.Togglebutton2.ClickButton(cbChecked)
  mainWindowView.Button2.ClickButton()
  #BuiltIn.ShowMessage("Successfully expanding Kit Results!")

