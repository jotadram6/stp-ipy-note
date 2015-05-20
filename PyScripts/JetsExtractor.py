from HistoExtractor import *

#M600="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM600_5318_Full_analyzed.root"
#M650="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM650_5318_Full_analyzed.root"
#M700="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM700_5318_Full_analyzed.root"
#M750="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM750_5318_Full_analyzed.root"
#M800="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM800_5318_Full_analyzed.root"
#M850="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM850_5318_Full_analyzed.root"
#M900="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM900_5318_Full_analyzed.root"
#M950="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM950_5318_Full_analyzed.root"
#M1000="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1/TpJetM1000_5318_Full_analyzed.root"

M600="/home/jruizalv/V1/TpJetM600_5318_Full_analyzed.root"
M650="/home/jruizalv/V1/TpJetM650_5318_Full_analyzed.root"
M700="/home/jruizalv/V1/TpJetM600_5318_Full_analyzed.root"
M750="/home/jruizalv/V1/TpJetM750_5318_Full_analyzed.root"
M800="/home/jruizalv/V1/TpJetM800_5318_Full_analyzed.root"
M850="/home/jruizalv/V1/TpJetM850_5318_Full_analyzed.root"
M900="/home/jruizalv/V1/TpJetM900_5318_Full_analyzed.root"
M950="/home/jruizalv/V1/TpJetM950_5318_Full_analyzed.root"
M1000="/home/jruizalv/V1/TpJetM1000_5318_Full_analyzed.root"

files=[M600,M650,M700,M750,M800,M850,M900,M950,M1000]

Tree="cuts"
Var=["jet1_pt","jet2_pt","jet3_pt","jet4_pt","jet5_pt","jet6_pt","jet1_eta","jet2_eta","jet3_eta","jet4_eta","jet5_eta","jet6_eta"]
HistoName=["_600","_650","_700","_750","_800","_850","_900","_950","_1000"]
bins=["(74,10,1500)","(48,-6,6)"]
PDF="_Signal_20GeVBins.pdf"
CutToApply=""

for i in xrange(len(Var)):
    Histos=[]
    for j in HistoName: Histos.append(Var[i]+j)
    if Var[i].split("_")[1]=="pt": HistoExtractor(files,Tree,Var[i],Histos,bins[0],Var[i]+PDF,CutToApply)
    else: HistoExtractor(files,Tree,Var[i],Histos,bins[1],Var[i]+PDF,CutToApply)
