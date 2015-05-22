import ROOT
import numpy as np
from array import array

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
         "QCD_HT_1000_Inf_5318_Full_analyzed.root"]

TreeStructureA="Nvtcs:NTI:weight:j1pt:j2pt:j3pt:j4pt:j5pt:j6pt:j1eta:j2eta:j3eta:j4eta:j5eta:j6eta:HT:NCSVM"
TreeStructure="Nvtcs:j1pt:j2pt:j3pt:j4pt:j5pt:j6pt:j1eta:j2eta:j3eta:j4eta:j5eta:j6eta:HT:NCSVM"

#Signal Sample
TntupleA = ROOT.TNtuple("TntupleA","TntupleA",TreeStructureA)
Q500ntupleA = ROOT.TNtuple("Q500ntupleA","Q500ntupleA",TreeStructureA)
Q1000ntupleA = ROOT.TNtuple("Q1000ntupleA","Q1000ntupleA",TreeStructureA)
QntuplesA=[Q500ntupleA,Q1000ntupleA]
S600ntupleA = ROOT.TNtuple("S600ntupleA","S600ntupleA",TreeStructureA)
S650ntupleA = ROOT.TNtuple("S650ntupleA","S650ntupleA",TreeStructureA)
S700ntupleA = ROOT.TNtuple("S700ntupleA","S700ntupleA",TreeStructureA)
S750ntupleA = ROOT.TNtuple("S750ntupleA","S750ntupleA",TreeStructureA)
S800ntupleA = ROOT.TNtuple("S800ntupleA","S800ntupleA",TreeStructureA)
S850ntupleA = ROOT.TNtuple("S850ntupleA","S850ntupleA",TreeStructureA)
S900ntupleA = ROOT.TNtuple("S900ntupleA","S900ntupleA",TreeStructureA)
S950ntupleA = ROOT.TNtuple("S950ntupleA","S950ntupleA",TreeStructureA)
S1000ntupleA = ROOT.TNtuple("S1000ntupleA","S1000ntupleA",TreeStructureA)
NMassPointsA=[S600ntupleA,S650ntupleA,S700ntupleA,S750ntupleA,S800ntupleA,S850ntupleA,S900ntupleA,S950ntupleA,S1000ntupleA]
ListTreesNamesA=["S600ntupleA","S650ntupleA","S700ntupleA","S750ntupleA","S800ntupleA","S850ntupleA","S900ntupleA","S950ntupleA","S1000ntupleA","TntupleA","Q500ntupleA","Q1000ntupleA"]

#Sntuple.Print()
#"M5J:DRHJ:DRWH:RelHT:Eta6thJ:M2HP:DRTp6thJ:HM:chi2:MTHAsym"
#Cut1 = ROOT.TCut("chi2<140")
CutHT = ROOT.TCut("THT>500")
CutDRbb = ROOT.TCut("DRHJ<=1.2")
CutDRWH = ROOT.TCut("DRWH>=1.6 && DRWH<=4.0")
CutHM = ROOT.TCut("HM>=105 && HM<=145")
CutM2HP = ROOT.TCut("M2HP>7.0")
CutRelHT = ROOT.TCut("RelHT>=0.67")
CutDRTp6thJ = ROOT.TCut("DRTp6thJ>4.7")
CutMTHAsym = ROOT.TCut("MTHAsym>=0.08 && MTHAsym<=0.28")

#Building MC and arrays
def ExtractingMCInfoFromTree(files,tree,ListTreesNames,TreeStructureT,SampleFile):
    AllSamples=[]
    for f in files:
        CutsChain=ROOT.TChain(tree)
        CutsChain.Add(f)
        entries = CutsChain.GetEntries()
        if files.index(f)>=0 and files.index(f)<=NsignalFiles-1: print "Filling signal..."
        elif files.index(f)>0: print "Filling bkgs..."
        print "Entries for file ", f, " are: ", entries
        TempTree= ROOT.TNtuple(ListTreesNames[files.index(f)],ListTreesNames[files.index(f)],TreeStructureT)
        for i in xrange(entries):
            CutsChain.GetEntry(i)
            if CutsChain.THT<600: continue
            #M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym
            if tree=="cuts":
                ListOfVariables = [CutsChain.Vertices,
                        CutsChain.Number_True_Interactions,
                        CutsChain.weight,
                        CutsChain.jet1_pt,
                        CutsChain.jet2_pt,
                        CutsChain.jet3_pt,
                        CutsChain.jet4_pt,
                        CutsChain.jet5_pt,
                        CutsChain.jet6_pt,
                        CutsChain.jet1_eta,
                        CutsChain.jet2_eta,
                        CutsChain.jet3_eta,
                        CutsChain.jet4_eta,
                        CutsChain.jet5_eta,
                        CutsChain.jet6_eta,
                        CutsChain.THT,
                        CutsChain.Number_CSVMbtagged_jets]
            TempTree.Fill(array('f',ListOfVariables))
        AllSamples.append(TempTree)
        del(TempTree)
    AllSamples=np.array(AllSamples)
    np.save(SampleFile,AllSamples)
    del(AllSamples)

def ExtractingDATAInfoFromTree(File,tree,ListTreesNames,TreeStructureT,SampleFile,EntDiv,WhichPart):
    CutsChain=ROOT.TChain(tree)
    CutsChain.Add(File)
    entries = CutsChain.GetEntries()
    if WhichPart<EntDiv-1: Entries=entries/EntDiv
    else: Entries=entries-(entries/EntDiv)*(EntDiv-1)
    print "Entries for file ", File, " are: ", entries
    TempTree= ROOT.TNtuple(ListTreesNames,ListTreesNames,TreeStructureT)
    for i in xrange(Entries):
        if WhichPart==0: CutsChain.GetEntry(i)
	else: CutsChain.GetEntry(((entries/EntDiv)*WhichPart)+i)
        if CutsChain.THT<600: continue
        #M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym
        if tree=="cuts":
            ListOfVariables = [CutsChain.Vertices,
                        CutsChain.jet1_pt,
                        CutsChain.jet2_pt,
                        CutsChain.jet3_pt,
                        CutsChain.jet4_pt,
                        CutsChain.jet5_pt,
                        CutsChain.jet6_pt,
                        CutsChain.jet1_eta,
                        CutsChain.jet2_eta,
                        CutsChain.jet3_eta,
                        CutsChain.jet4_eta,
                        CutsChain.jet5_eta,
                        CutsChain.jet6_eta,
                        CutsChain.THT,
                        CutsChain.Number_CSVMbtagged_jets]
        TempTree.Fill(array('f',ListOfVariables))
    AllSamples=np.array([TempTree])
    np.save(SampleFile,AllSamples)
    del(TempTree); del(AllSamples)

if __name__ == '__main__':
    VersionToProcess="V1/"
    MCFiles=[]
    DATAFiles=Base+VersionToProcess+DATA_F
    for i in files: MCFiles.append(Base+VersionToProcess+i)

    ExtractingMCInfoFromTree(MCFiles,"cuts",ListTreesNamesA,TreeStructureA,"SignalSample_preselection"+VersionToProcess[:-1])

    N=40
    #for i in xrange(N):
	#if i<12: continue
     #   ExtractingDATAInfoFromTree(DATAFiles,"cuts","DatantupleA",TreeStructure,"Data_preselection"+str(i)+"_"+VersionToProcess[:-1],N,i)

