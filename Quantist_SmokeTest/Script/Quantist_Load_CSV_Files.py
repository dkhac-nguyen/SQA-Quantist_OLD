﻿def Load_CSV_Files():
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.MainWindowView
  quantist.MainWindowView.LoadButton.ClickButton()

#  str = ProjectSuite.Variables.SampleDataFolder + ProjectSuite.Variables.sample_csv_pm8800
#  quantist.dlgOpen.OpenFile(str, "Consumable Files (*.csv;*.quantist)")

#  progress = quantist.dlgOpen.WorkerW.ReBarWindow32.AddressBandRoot.progress
#  comboBox = progress.comboBox
#  Aliases.Quantist.dlgOpen.WorkerW.ReBarWindow32.AddressBandRoot.progress.BreadcrumbParent.toolbar.Ac
#  comboBox.SetText(ProjectSuite.Variables.SampleDataFolder)
#  comboBox.ComboBox.Edit.Keys("[Enter]")
    
  dlgOpen = quantist.dlgOpen
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.FLEX_csv
  UIItem.Keys("^a")

  dlgOpen.btnOpen.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)

  Aliases.Quantist.MainWindowView.ToggleShareView.ClickButton(cbChecked)  

  treeView = mainWindowView.RunTreeView
  treeView.ClickItem("|[0]|[0]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[1]|[1]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[2]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[3]|[3]")  

  Regions.Horizontal_ShareView.Check(Aliases.Quantist.MainWindowView.MainView)
  Aliases.Quantist.MainWindowView.ToggleVerticalButton.ClickButton(cbChecked)
  ProjectSuite.Variables.Short_Delay  
  Regions.Vertical_ShareView.Check(Aliases.Quantist.MainWindowView.MainView)  
  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.ToggleHorizontalPlane.ClickButton(cbUnchecked)   
  Regions.Horizontal_ShareView.Check(Aliases.Quantist.MainWindowView.MainView)
    
      
def Load_A_file():
  quantist = Aliases.Quantist
  quantist.MainWindowView.LoadButton.ClickButton()
  dlgOpen = quantist.dlgOpen
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.FLEX_csv

  UIItem.Name.Click(62, 10)
  dlgOpen.btnOpen.ClickButton()
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  

def double_Click_To_open_File():
  quantist_Wpf = Aliases.Quantist
  quantist_Wpf.MainWindowView.LoadButton.ClickButton()
  quantist_Wpf.dlgOpen.OpenFile("E:\\TestComplete\\Quantist\\SampleQuantistFiles\\PM6910.csv", "Consumable Files (*.csv;*.quantist)")

def ShareView():
  mainWindowView = Aliases.Quantist.MainWindowView
  #Aliases.Quantist.MainWindowView.Border

  border = mainWindowView.Border
  toggleButton = border.Togglebutton
  toggleButton.ClickButton(cbChecked)
  treeView = mainWindowView.RunTreeView
  treeView.ClickItem("|[1]|[0]")
  treeView.ClickItem("|[2]|[1]")
  treeView.ClickItem("|[3]|[2]")
  Regions.ShareView_Horizontal.Check(Aliases.Quantist.MainWindowView.Border2)
  border.Togglebutton2.ClickButton(cbChecked)
  Regions.ShareView_Vertical.Check(Aliases.Quantist.MainWindowView.Border2)
  toggleButton.ClickButton(cbUnchecked)
  Regions.SingleView_CVP2.Check(Aliases.Quantist.MainWindowView.Border2)

