from HistoExtractor import *

M600="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM600_5318_Full_analyzed.root"
M650="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM650_5318_Full_analyzed.root"
M700="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM700_5318_Full_analyzed.root"
M750="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM750_5318_Full_analyzed.root"
M800="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM800_5318_Full_analyzed.root"
M850="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM850_5318_Full_analyzed.root"
M900="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM900_5318_Full_analyzed.root"
M950="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM950_5318_Full_analyzed.root"
M1000="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM1000_5318_Full_analyzed.root"

files=[M600,M650,M700,M750,M800,M850,M900,M950,M1000]

Tree="stp"

PtVar=["First_Higgs_Jet.Pt()","Second_Higgs_Jet.Pt()","First_W_Jet.Pt()","Second_W_Jet.Pt()","Top_Jet.Pt()","Jet6th.Pt()","Reconstructed_Higgs.Pt()","Reconstructed_W.Pt()","Reconstructed_Top.Pt()","Reconstructed_Tprime.Pt()"]
EtaVar=["First_Higgs_Jet.Eta()","Second_Higgs_Jet.Eta()","First_W_Jet.Eta()","Second_W_Jet.Eta()","Top_Jet.Eta()","Jet6th.Eta()","Reconstructed_Higgs.Eta()","Reconstructed_W.Eta()","Reconstructed_Top.Eta()","Reconstructed_Tprime.Eta()"]
MVar=["Reconstructed_Higgs.M()","Reconstructed_W.M()","Reconstructed_Top.M()","Reconstructed_Tprime.M()"]

HistoName=["_600","_650","_700","_750","_800","_850","_900","_950","_1000"]
Ptbins="(149,10,1500)"
Etabins="(120,-6,6)"
Mbins=["(24,60,180)","(16,40,120)","(28,100,240)","(120,400,1600)"]
PDF="_Signal.pdf"
CutToApply=""

for i in xrange(len(PtVar)):
    Histos=[]
    for j in HistoName: Histos.append(PtVar[i].replace(".","_")[:-2]+j)
    HistoExtractor(files,Tree,PtVar[i],Histos,Ptbins,PtVar[i].replace(".","_")[:-2]+PDF,CutToApply)

for i in xrange(len(EtaVar)):
    Histos=[]
    for j in HistoName: Histos.append(EtaVar[i].replace(".","_")[:-2]+j)
    HistoExtractor(files,Tree,EtaVar[i],Histos,Etabins,EtaVar[i].replace(".","_")[:-2]+PDF,CutToApply)

for i in xrange(len(MVar)):
    Histos=[]
    for j in HistoName: Histos.append(MVar[i].replace(".","_")[:-2]+j)
    HistoExtractor(files,Tree,MVar[i],Histos,Mbins[i],MVar[i].replace(".","_")[:-2]+PDF,CutToApply)
