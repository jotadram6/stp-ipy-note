import ROOT
import numpy as np
from array import array
from BTagSFtoWeigths import *

Base="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/"

DATA_F="Full_Data.root"

#Declaring samples, tree structure, and ntuples
NsignalFiles=9

files = ["TpJetM600_5318_Full_analyzed.root",
         "TpJetM650_5318_Full_analyzed.root",
         "TpJetM700_5318_Full_analyzed.root",
         "TpJetM750_5318_Full_analyzed.root",
         "TpJetM800_5318_Full_analyzed.root",
         "TpJetM850_5318_Full_analyzed.root",
         "TpJetM900_5318_Full_analyzed.root",
         "TpJetM950_5318_Full_analyzed.root",
         "TpJetM1000_5318_Full_analyzed.root",
         "TTJetsF_5318_Full_analyzed.root",
         "QCD_HT_500_1000_5318_Full_analyzed.root",
         "QCD_HT_1000_Inf_5318_Full_analyzed.root",
         "T-s_5318_Full_analyzed.root",
         "T-t_5318_Full_analyzed.root",
         "T-tw_5318_Full_analyzed.root",
         "Tbar-s_5318_Full_analyzed.root",
         "Tbar-t_5318_Full_analyzed.root",
         "Tbar-tw_5318_Full_analyzed.root",
         "WW_5318_Full_analyzed.root",
         "WZ_5318_Full_analyzed.root",
         "ZZ_5318_Full_analyzed.root",
         "DYToBB_5318_Full_analyzed.root",
         "DYToCC_5318_Full_analyzed.root",
         "QCD_PT_120_170-v3_Full_analyzed.root",
         "QCD_PT_170_300_5318_Full_analyzed.root",
         "QCD_PT_300_470_5318_Full_analyzed.root",
         "QCD_PT_470_600_5318_Full_analyzed.root",
         "QCD_PT_600_800_5318_Full_analyzed.root",
         "QCD_PT_800_1000_5318_Full_analyzed.root"]

TreeStructureA="NTI:j1pt:HT:NCSVM:SFW"

#Building MC and arrays
def ExtractingMCSFInfoFromTree(files,tree,ListTreesNames,TreeStructureT,SampleFile):
    AllSamples=[]
    for f in files:
        CutsChain=ROOT.TChain(tree)
        CutsChain.Add(f)
        entries = CutsChain.GetEntries()
        if files.index(f)>=0 and files.index(f)<=NsignalFiles-1: print "Filling signal..."
        elif files.index(f)>0: print "Filling bkgs..."
        print "Entries for file ", f, " are: ", entries
        TempTree= ROOT.TNtuple(ListTreesNames[files.index(f)].split(".")[0],ListTreesNames[files.index(f)].split(".")[0],TreeStructureT)
        for i in xrange(entries):
            CutsChain.GetEntry(i)
            if CutsChain.THT<600 or CutsChain.jet1_pt<150 or CutsChain.Number_CSVMbtagged_jets<=2: continue
            if tree=="cuts":
                SFValues=[]
                for i in xrange(CutsChain.JetScaleFactor.size()):
                    SFValues.append(CutsChain.JetScaleFactor.at(i))
                ListOfVariables = [CutsChain.Number_True_Interactions,
                        CutsChain.jet1_pt,
                        CutsChain.THT,
                        CutsChain.Number_CSVMbtagged_jets,
                        TotalW(SFValues)]
            TempTree.Fill(array('f',ListOfVariables))
        AllSamples.append(TempTree)
        del(TempTree)
    AllSamples=np.array(AllSamples)
    np.save(SampleFile,AllSamples)
    del(AllSamples)

if __name__ == '__main__':
    VersionToProcess="V1/"
    MCFiles=[]
    DATAFiles=Base+VersionToProcess+DATA_F
    for i in files: MCFiles.append(Base+VersionToProcess+i)

    ExtractingMCSFInfoFromTree(MCFiles,"cuts",files,TreeStructureA,"SignalSample_preselection_SFminimalTest_"+VersionToProcess[:-1])

    N=40
    #for i in xrange(N):
	#if i<12: continue
     #   ExtractingDATAInfoFromTree(DATAFiles,"cuts","DatantupleA",TreeStructure,"Data_preselection"+str(i)+"_"+VersionToProcess[:-1],N,i)

