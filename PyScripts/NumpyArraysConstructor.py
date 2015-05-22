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

TreeStructureA="THT:M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym:NTI:weight"
TreeStructure="THT:M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym"

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

#Control Sample
TntupleE = ROOT.TNtuple("TntupleE","TntupleE",TreeStructure)
Q500ntupleE = ROOT.TNtuple("Q500ntupleE","Q500ntupleE",TreeStructure)
Q1000ntupleE = ROOT.TNtuple("Q1000ntupleE","Q1000ntupleE",TreeStructure)
QntuplesE=[Q500ntupleE,Q1000ntupleE]
S600ntupleE = ROOT.TNtuple("S600ntupleE","S600ntupleE",TreeStructure)
S650ntupleE = ROOT.TNtuple("S650ntupleE","S650ntupleE",TreeStructure)
S700ntupleE = ROOT.TNtuple("S700ntupleE","S700ntupleE",TreeStructure)
S750ntupleE = ROOT.TNtuple("S750ntupleE","S750ntupleE",TreeStructure)
S800ntupleE = ROOT.TNtuple("S800ntupleE","S800ntupleE",TreeStructure)
S850ntupleE = ROOT.TNtuple("S850ntupleE","S850ntupleE",TreeStructure)
S900ntupleE = ROOT.TNtuple("S900ntupleE","S900ntupleE",TreeStructure)
S950ntupleE = ROOT.TNtuple("S950ntupleE","S950ntupleE",TreeStructure)
S1000ntupleE = ROOT.TNtuple("S1000ntupleE","S1000ntupleE",TreeStructure)
NMassPointsE=[S600ntupleE,S650ntupleE,S700ntupleE,S750ntupleE,S800ntupleE,S850ntupleE,S900ntupleE,S950ntupleE,S1000ntupleE]
ListTreesNamesE=["S600ntupleE","S650ntupleE","S700ntupleE","S750ntupleE","S800ntupleE","S850ntupleE","S900ntupleE","S950ntupleE","S1000ntupleE","TntupleE","Q500ntupleE","Q1000ntupleE"]

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
            if tree=="stp":
                HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs.X(),CutsChain.Reconstructed_Higgs.Y(),CutsChain.Reconstructed_Higgs.Z(),CutsChain.Reconstructed_Higgs.T())
                Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet.X(),CutsChain.Second_Higgs_Jet.Y(),CutsChain.Second_Higgs_Jet.Z(),CutsChain.Second_Higgs_Jet.T())
                J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
                TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime.X(),CutsChain.Reconstructed_Tprime.Y(),CutsChain.Reconstructed_Tprime.Z(),CutsChain.Reconstructed_Tprime.T())
                Top2=HiggsV+J6thV
                W2=Higgs2ndJV+J6thV
                TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet.X(),CutsChain.Top_Jet.Y(),CutsChain.Top_Jet.Z(),CutsChain.Top_Jet.T())
                ListOfVariables = [CutsChain.THT,
                                   CutsChain.Reconstructed_Tprime.M(),
                                   CutsChain.DeltaR_of_Higgs_Jets,
                                   CutsChain.DeltaR_of_W_Higgs,
                                   CutsChain.Relative_THT,
                                   ((Top2.M()+W2.M())/CutsChain.Reconstructed_Higgs.M()),
                                   TprimeV.DeltaR(J6thV),
                                   CutsChain.Reconstructed_Higgs.M(),
                                   (CutsChain.HiggsChi2+CutsChain.TopChi2),
                                   ((CutsChain.Reconstructed_Top.M()-CutsChain.Reconstructed_Higgs.M())/(CutsChain.Reconstructed_Top.M()+CutsChain.Reconstructed_Higgs.M())),
                                   CutsChain.Number_True_Interactions,
                                   CutsChain.weight]
            elif tree=="stp3LNC":
                HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs3L.X(),CutsChain.Reconstructed_Higgs3L.Y(),CutsChain.Reconstructed_Higgs3L.Z(),CutsChain.Reconstructed_Higgs3L.T())
                Higgs1stJV=ROOT.TLorentzVector(CutsChain.First_Higgs_Jet3L.X(),CutsChain.First_Higgs_Jet3L.Y(),CutsChain.First_Higgs_Jet3L.Z(),CutsChain.First_Higgs_Jet3L.T())
                Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet3L.X(),CutsChain.Second_Higgs_Jet3L.Y(),CutsChain.Second_Higgs_Jet3L.Z(),CutsChain.Second_Higgs_Jet3L.T())
                J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
                TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime3L.X(),CutsChain.Reconstructed_Tprime3L.Y(),CutsChain.Reconstructed_Tprime3L.Z(),CutsChain.Reconstructed_Tprime3L.T())
                W1V=ROOT.TLorentzVector(CutsChain.Reconstructed_W3L.X(),CutsChain.Reconstructed_W3L.Y(),CutsChain.Reconstructed_W3L.Z(),CutsChain.Reconstructed_W3L.T())
                Top2=HiggsV+J6thV
                W2=Higgs2ndJV+J6thV
                TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet3L.X(),CutsChain.Top_Jet3L.Y(),CutsChain.Top_Jet3L.Z(),CutsChain.Top_Jet3L.T())
                ListOfVariables = [CutsChain.THT,
                                   CutsChain.Reconstructed_Tprime3L.M(),
                                   Higgs1stJV.DeltaR(Higgs2ndJV),
                                   HiggsV.DeltaR(W1V),
                                   (CutsChain.Reconstructed_Higgs3L.Pt()+CutsChain.Reconstructed_Top3L.Pt())/CutsChain.THT,
                                   (Top2.M()+W2.M())/CutsChain.Reconstructed_Higgs3L.M(),
                                   TprimeV.DeltaR(J6thV),
                                   CutsChain.Reconstructed_Higgs3L.M(),
                                   (CutsChain.HiggsChi2+CutsChain.TopChi2),
                                   (CutsChain.Reconstructed_Top3L.M()-CutsChain.Reconstructed_Higgs3L.M())/(CutsChain.Reconstructed_Top3L.M()+CutsChain.Reconstructed_Higgs3L.M())]
            TempTree.Fill(array('f',ListOfVariables))
        AllSamples.append(TempTree)
        del(TempTree)
    AllSamples=np.array(AllSamples)
    np.save(SampleFile,AllSamples)
    del(AllSamples)

def ExtractingTTbarInfoFromTree(files,tree,ListTreesNames,TreeStructureT,SampleFile,EntDiv,WhichPart):
    AllSamples=[]
    for f in files:
        CutsChain=ROOT.TChain(tree)
        CutsChain.Add(f)
        entries = CutsChain.GetEntries()
        if WhichPart<EntDiv-1: Entries=entries/EntDiv
        else: Entries=entries-(entries/EntDiv)*(EntDiv-1)
        if files.index(f)>=0 and files.index(f)<=NsignalFiles-1: print "Filling signal..."
        elif files.index(f)>0: print "Filling bkgs..."
        print "Entries for file ", f, " are: ", entries
        TempTree= ROOT.TNtuple(ListTreesNames[files.index(f)],ListTreesNames[files.index(f)],TreeStructureT)
        for i in xrange(Entries):
            if WhichPart==0: CutsChain.GetEntry(i)
            else: CutsChain.GetEntry(((entries/EntDiv)*WhichPart)+i)
            if CutsChain.THT<600: continue
            #M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym
            if tree=="stp":
                HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs.X(),CutsChain.Reconstructed_Higgs.Y(),CutsChain.Reconstructed_Higgs.Z(),CutsChain.Reconstructed_Higgs.T())
                Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet.X(),CutsChain.Second_Higgs_Jet.Y(),CutsChain.Second_Higgs_Jet.Z(),CutsChain.Second_Higgs_Jet.T())
                J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
                TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime.X(),CutsChain.Reconstructed_Tprime.Y(),CutsChain.Reconstructed_Tprime.Z(),CutsChain.Reconstructed_Tprime.T())
                Top2=HiggsV+J6thV
                W2=Higgs2ndJV+J6thV
                TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet.X(),CutsChain.Top_Jet.Y(),CutsChain.Top_Jet.Z(),CutsChain.Top_Jet.T())
                ListOfVariables = [CutsChain.THT,
                                   CutsChain.Reconstructed_Tprime.M(),
                                   CutsChain.DeltaR_of_Higgs_Jets,
                                   CutsChain.DeltaR_of_W_Higgs,
                                   CutsChain.Relative_THT,
                                   ((Top2.M()+W2.M())/CutsChain.Reconstructed_Higgs.M()),
                                   TprimeV.DeltaR(J6thV),
                                   CutsChain.Reconstructed_Higgs.M(),
                                   (CutsChain.HiggsChi2+CutsChain.TopChi2),
                                   ((CutsChain.Reconstructed_Top.M()-CutsChain.Reconstructed_Higgs.M())/(CutsChain.Reconstructed_Top.M()+CutsChain.Reconstructed_Higgs.M())),
                                   CutsChain.Number_True_Interactions,
                                   CutsChain.weight]
            elif tree=="stp3LNC":
                HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs3L.X(),CutsChain.Reconstructed_Higgs3L.Y(),CutsChain.Reconstructed_Higgs3L.Z(),CutsChain.Reconstructed_Higgs3L.T())
                Higgs1stJV=ROOT.TLorentzVector(CutsChain.First_Higgs_Jet3L.X(),CutsChain.First_Higgs_Jet3L.Y(),CutsChain.First_Higgs_Jet3L.Z(),CutsChain.First_Higgs_Jet3L.T())
                Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet3L.X(),CutsChain.Second_Higgs_Jet3L.Y(),CutsChain.Second_Higgs_Jet3L.Z(),CutsChain.Second_Higgs_Jet3L.T())
                J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
                TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime3L.X(),CutsChain.Reconstructed_Tprime3L.Y(),CutsChain.Reconstructed_Tprime3L.Z(),CutsChain.Reconstructed_Tprime3L.T())
                W1V=ROOT.TLorentzVector(CutsChain.Reconstructed_W3L.X(),CutsChain.Reconstructed_W3L.Y(),CutsChain.Reconstructed_W3L.Z(),CutsChain.Reconstructed_W3L.T())
                Top2=HiggsV+J6thV
                W2=Higgs2ndJV+J6thV
                TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet3L.X(),CutsChain.Top_Jet3L.Y(),CutsChain.Top_Jet3L.Z(),CutsChain.Top_Jet3L.T())
                ListOfVariables = [CutsChain.THT,
                                   CutsChain.Reconstructed_Tprime3L.M(),
                                   Higgs1stJV.DeltaR(Higgs2ndJV),
                                   HiggsV.DeltaR(W1V),
                                   (CutsChain.Reconstructed_Higgs3L.Pt()+CutsChain.Reconstructed_Top3L.Pt())/CutsChain.THT,
                                   (Top2.M()+W2.M())/CutsChain.Reconstructed_Higgs3L.M(),
                                   TprimeV.DeltaR(J6thV),
                                   CutsChain.Reconstructed_Higgs3L.M(),
                                   (CutsChain.HiggsChi2+CutsChain.TopChi2),
                                   (CutsChain.Reconstructed_Top3L.M()-CutsChain.Reconstructed_Higgs3L.M())/(CutsChain.Reconstructed_Top3L.M()+CutsChain.Reconstructed_Higgs3L.M())]
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
        if tree=="stp":
            HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs.X(),CutsChain.Reconstructed_Higgs.Y(),CutsChain.Reconstructed_Higgs.Z(),CutsChain.Reconstructed_Higgs.T())
            Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet.X(),CutsChain.Second_Higgs_Jet.Y(),CutsChain.Second_Higgs_Jet.Z(),CutsChain.Second_Higgs_Jet.T())
            J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
            TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime.X(),CutsChain.Reconstructed_Tprime.Y(),CutsChain.Reconstructed_Tprime.Z(),CutsChain.Reconstructed_Tprime.T())
            Top2=HiggsV+J6thV
            W2=Higgs2ndJV+J6thV
            TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet.X(),CutsChain.Top_Jet.Y(),CutsChain.Top_Jet.Z(),CutsChain.Top_Jet.T())            
            ListOfVariables = [CutsChain.THT,
                               CutsChain.Reconstructed_Tprime.M(),
                               CutsChain.DeltaR_of_Higgs_Jets,
                               CutsChain.DeltaR_of_W_Higgs,
                               CutsChain.Relative_THT,
                               ((Top2.M()+W2.M())/CutsChain.Reconstructed_Higgs.M()),
                               TprimeV.DeltaR(J6thV),
                               CutsChain.Reconstructed_Higgs.M(),
                               (CutsChain.HiggsChi2+CutsChain.TopChi2),
                               ((CutsChain.Reconstructed_Top.M()-CutsChain.Reconstructed_Higgs.M())/(CutsChain.Reconstructed_Top.M()+CutsChain.Reconstructed_Higgs.M()))]
        elif tree=="stp3LNC":
            HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs3L.X(),CutsChain.Reconstructed_Higgs3L.Y(),CutsChain.Reconstructed_Higgs3L.Z(),CutsChain.Reconstructed_Higgs3L.T())
            Higgs1stJV=ROOT.TLorentzVector(CutsChain.First_Higgs_Jet3L.X(),CutsChain.First_Higgs_Jet3L.Y(),CutsChain.First_Higgs_Jet3L.Z(),CutsChain.First_Higgs_Jet3L.T())
            Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet3L.X(),CutsChain.Second_Higgs_Jet3L.Y(),CutsChain.Second_Higgs_Jet3L.Z(),CutsChain.Second_Higgs_Jet3L.T())
            J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
            TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime3L.X(),CutsChain.Reconstructed_Tprime3L.Y(),CutsChain.Reconstructed_Tprime3L.Z(),CutsChain.Reconstructed_Tprime3L.T())
            W1V=ROOT.TLorentzVector(CutsChain.Reconstructed_W3L.X(),CutsChain.Reconstructed_W3L.Y(),CutsChain.Reconstructed_W3L.Z(),CutsChain.Reconstructed_W3L.T())
            Top2=HiggsV+J6thV
            W2=Higgs2ndJV+J6thV
            TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet3L.X(),CutsChain.Top_Jet3L.Y(),CutsChain.Top_Jet3L.Z(),CutsChain.Top_Jet3L.T())
            ListOfVariables = [CutsChain.THT,
                               CutsChain.Reconstructed_Tprime3L.M(),
                               Higgs1stJV.DeltaR(Higgs2ndJV),
                               HiggsV.DeltaR(W1V),
                               (CutsChain.Reconstructed_Higgs3L.Pt()+CutsChain.Reconstructed_Top3L.Pt())/CutsChain.THT,
                               (Top2.M()+W2.M())/CutsChain.Reconstructed_Higgs3L.M(),
                               TprimeV.DeltaR(J6thV),
                               CutsChain.Reconstructed_Higgs3L.M(),
                               (CutsChain.HiggsChi2+CutsChain.TopChi2),
                               (CutsChain.Reconstructed_Top3L.M()-CutsChain.Reconstructed_Higgs3L.M())/(CutsChain.Reconstructed_Top3L.M()+CutsChain.Reconstructed_Higgs3L.M())]
        TempTree.Fill(array('f',ListOfVariables))
    AllSamples=np.array([TempTree])
    np.save(SampleFile,AllSamples)
    del(TempTree); del(AllSamples)

""" A=31
    for j in xrange(10):
    if j<9: B=A/10
    else: B=A-((A/10)*j)
    for i in xrange(B):
        if j==0: print i
        else: print ((A/10)*j)+i"""

if __name__ == '__main__':
    VersionToProcess="V1/"
    MCFiles=[]
    DATAFiles=Base+VersionToProcess+DATA_F
    for i in files: MCFiles.append(Base+VersionToProcess+i)

    #ExtractingMCInfoFromTree(MCFiles,"stp",ListTreesNamesA,TreeStructureA,"SignalSample_"+VersionToProcess[:-1])
    #ExtractingDATAInfoFromTree(DATAFiles,"stp","DatantupleA",TreeStructureA,"DataA_"+VersionToProcess[:-1],1,0)

    #ExtractingMCInfoFromTree(MCFiles[:9],"stp3LNC",ListTreesNamesE,TreeStructure,"ControlSample_SignalMassPoints_"+VersionToProcess[:-1])
    #ExtractingMCInfoFromTree(MCFiles[9:10],"stp3LNC",ListTreesNamesE,TreeStructure,"ControlSample_TTJets_"+VersionToProcess[:-1])
    #ExtractingMCInfoFromTree(MCFiles[10:],"stp3LNC",ListTreesNamesE,TreeStructure,"ControlSample_QCDHT_"+VersionToProcess[:-1])
    
    N=20
    for i in xrange(N):
#	if i<12: continue
        ExtractingTTbarInfoFromTree(MCFiles[9:10],"stp3LNC",ListTreesNamesE,TreeStructure,"ControlSample_TTJets_"+str(i)+"_"+VersionToProcess[:-1],N,i)

    #for i in xrange(N):
#	if i<12: continue
#        ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE"+str(i)+"_"+VersionToProcess[:-1],N,i)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE1_"+VersionToProcess[:-1],10,0)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE2_"+VersionToProcess[:-1],10,1)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE3_"+VersionToProcess[:-1],10,2)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE4_"+VersionToProcess[:-1],10,3)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE5_"+VersionToProcess[:-1],10,4)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE6_"+VersionToProcess[:-1],10,5)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE7_"+VersionToProcess[:-1],10,6)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE8_"+VersionToProcess[:-1],10,7)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE9_"+VersionToProcess[:-1],10,8)
    #ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE10_"+VersionToProcess[:-1],10,9)

