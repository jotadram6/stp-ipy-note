import ROOT
import numpy as np
from array import array

Base="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/"

InclusiveVersions=["V1/","V2/","V3/"]

DATA_F="Full_Data.root"

#Declaring samples, tree structure, and ntuples

Ffiles = ["T-s_5318_Full_analyzed.root",
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

TreeStructureA="M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym:NTI:weight"
TreeStructure="M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym"

#Signal Sample
TsA=ROOT.TNtuple("TsA","TsA",TreeStructureA)
TtA=ROOT.TNtuple("TtA","TtA",TreeStructureA)
TtwA=ROOT.TNtuple("TtwA","TtwA",TreeStructureA)
TbarsA=ROOT.TNtuple("TbarsA","TbarsA",TreeStructureA)
TbartA=ROOT.TNtuple("TbartA","TbartA",TreeStructureA)
TbartwA=ROOT.TNtuple("TbartwA","TbartwA",TreeStructureA)
TsinglentuplesA=[TsA,TtA,TtwA,TbarsA,TbartA,TbartwA]

WWA=ROOT.TNtuple("WWA","WWA",TreeStructureA)
WZA=ROOT.TNtuple("WZA","WZA",TreeStructureA)
ZZA=ROOT.TNtuple("ZZA","ZZA",TreeStructureA)
DibosonntupleA=[WWA,WZA,ZZA]

DYBBA=ROOT.TNtuple("DYBBA","DYBBA",TreeStructureA)
DYCCA=ROOT.TNtuple("DYCCA","DYCCA",TreeStructureA)
DYntupleA=[DYBBA,DYCCA]

QCD120A=ROOT.TNtuple("QCD120A","QCD120A",TreeStructureA)
QCD170A=ROOT.TNtuple("QCD170A","QCD170A",TreeStructureA)
QCD300A=ROOT.TNtuple("QCD300A","QCD300A",TreeStructureA)
QCD470A=ROOT.TNtuple("QCD470A","QCD470A",TreeStructureA)
QCD600A=ROOT.TNtuple("QCD600A","QCD600A",TreeStructureA)
QCD800A=ROOT.TNtuple("QCD800A","QCD800A",TreeStructureA)
QCDPTntupleA=[QCD120A,QCD170A,QCD300A,QCD470A,QCD600A,QCD800A]

#Control Sample CSVL=[0.244,0.679)
TsE=ROOT.TNtuple("TsE","TsE",TreeStructure)
TtE=ROOT.TNtuple("TtE","TtE",TreeStructure)
TtwE=ROOT.TNtuple("TtwE","TtwE",TreeStructure)
TbarsE=ROOT.TNtuple("TbarsE","TbarsE",TreeStructure)
TbartE=ROOT.TNtuple("TbartE","TbartE",TreeStructure)
TbartwE=ROOT.TNtuple("TbartwE","TbartwE",TreeStructure)
TsinglentuplesE=[TsE,TtE,TtwE,TbarsE,TbartE,TbartwE]

WWE=ROOT.TNtuple("WWE","WWE",TreeStructure)
WZE=ROOT.TNtuple("WZE","WZE",TreeStructure)
ZZE=ROOT.TNtuple("ZZE","ZZE",TreeStructure)
DibosonntupleE=[WWE,WZE,ZZE]

DYBBE=ROOT.TNtuple("DYBBE","DYBBE",TreeStructure)
DYCCE=ROOT.TNtuple("DYCCE","DYCCE",TreeStructure)
DYntupleE=[DYBBE,DYCCE]

QCD120E=ROOT.TNtuple("QCD120E","QCD120E",TreeStructure)
QCD170E=ROOT.TNtuple("QCD170E","QCD170E",TreeStructure)
QCD300E=ROOT.TNtuple("QCD300E","QCD300E",TreeStructure)
QCD470E=ROOT.TNtuple("QCD470E","QCD470E",TreeStructure)
QCD600E=ROOT.TNtuple("QCD600E","QCD600E",TreeStructure)
QCD800E=ROOT.TNtuple("QCD800E","QCD800E",TreeStructure)
QCDPTntupleE=[QCD120E,QCD170E,QCD300E,QCD470E,QCD600E,QCD800E]

#Control Sample CSVL=[0.389,0.679)
TsE1=ROOT.TNtuple("TsE1","TsE1",TreeStructure)
TtE1=ROOT.TNtuple("TtE1","TtE1",TreeStructure)
TtwE1=ROOT.TNtuple("TtwE1","TtwE1",TreeStructure)
TbarsE1=ROOT.TNtuple("TbarsE1","TbarsE1",TreeStructure)
TbartE1=ROOT.TNtuple("TbartE1","TbartE1",TreeStructure)
TbartwE1=ROOT.TNtuple("TbartwE1","TbartwE1",TreeStructure)
TsinglentuplesE1=[TsE1,TtE1,TtwE1,TbarsE1,TbartE1,TbartwE1]

WWE1=ROOT.TNtuple("WWE1","WWE1",TreeStructure)
WZE1=ROOT.TNtuple("WZE1","WZE1",TreeStructure)
ZZE1=ROOT.TNtuple("ZZE1","ZZE1",TreeStructure)
DibosonntupleE1=[WWE1,WZE1,ZZE1]

DYBBE1=ROOT.TNtuple("DYBBE1","DYBBE1",TreeStructure)
DYCCE1=ROOT.TNtuple("DYCCE1","DYCCE1",TreeStructure)
DYntupleE1=[DYBBE1,DYCCE1]

QCD120E1=ROOT.TNtuple("QCD120E1","QCD120E1",TreeStructure)
QCD170E1=ROOT.TNtuple("QCD170E1","QCD170E1",TreeStructure)
QCD300E1=ROOT.TNtuple("QCD300E1","QCD300E1",TreeStructure)
QCD470E1=ROOT.TNtuple("QCD470E1","QCD470E1",TreeStructure)
QCD600E1=ROOT.TNtuple("QCD600E1","QCD600E1",TreeStructure)
QCD800E1=ROOT.TNtuple("QCD800E1","QCD800E1",TreeStructure)
QCDPTntupleE1=[QCD120E1,QCD170E1,QCD300E1,QCD470E1,QCD600E1,QCD800E1]

#Control Sample CSVL=[0.534,0.679)
TsE2=ROOT.TNtuple("TsE2","TsE2",TreeStructure)
TtE2=ROOT.TNtuple("TtE2","TtE2",TreeStructure)
TtwE2=ROOT.TNtuple("TtwE2","TtwE2",TreeStructure)
TbarsE2=ROOT.TNtuple("TbarsE2","TbarsE2",TreeStructure)
TbartE2=ROOT.TNtuple("TbartE2","TbartE2",TreeStructure)
TbartwE2=ROOT.TNtuple("TbartwE2","TbartwE2",TreeStructure)
TsinglentuplesE2=[TsE2,TtE2,TtwE2,TbarsE2,TbartE2,TbartwE2]

WWE2=ROOT.TNtuple("WWE2","WWE2",TreeStructure)
WZE2=ROOT.TNtuple("WZE2","WZE2",TreeStructure)
ZZE2=ROOT.TNtuple("ZZE2","ZZE2",TreeStructure)
DibosonntupleE2=[WWE2,WZE2,ZZE2]

DYBBE2=ROOT.TNtuple("DYBBE2","DYBBE2",TreeStructure)
DYCCE2=ROOT.TNtuple("DYCCE2","DYCCE2",TreeStructure)
DYntupleE2=[DYBBE2,DYCCE2]

QCD120E2=ROOT.TNtuple("QCD120E2","QCD120E2",TreeStructure)
QCD170E2=ROOT.TNtuple("QCD170E2","QCD170E2",TreeStructure)
QCD300E2=ROOT.TNtuple("QCD300E2","QCD300E2",TreeStructure)
QCD470E2=ROOT.TNtuple("QCD470E2","QCD470E2",TreeStructure)
QCD600E2=ROOT.TNtuple("QCD600E2","QCD600E2",TreeStructure)
QCD800E2=ROOT.TNtuple("QCD800E2","QCD800E2",TreeStructure)
QCDPTntupleE2=[QCD120E2,QCD170E2,QCD300E2,QCD470E2,QCD600E2,QCD800E2]


#Building MC and arrays
def ExtractingMCInfoFromTree(files,tree,ListTreesNames,TreeStructureT,SampleFile):
    if tree=="stp":
        for f in files:
            CutsChain=ROOT.TChain(tree)
            CutsChain.Add(f)
            entries = CutsChain.GetEntries()
            #if files.index(f)>=0 and files.index(f)<=NsignalFiles-1: print "Filling signal..."
            #elif files.index(f)>0: print "Filling bkgs..."
            print "Entries for file ", f, " are: ", entries
            for i in xrange(entries):
                CutsChain.GetEntry(i)
                if CutsChain.THT<600: continue
                #M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym
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
                if files.index(f)>=0 and files.index(f)<=5:            
                    TsinglentuplesA[files.index(f)].Fill(array('f',ListOfVariables))
                elif files.index(f)>=6 and files.index(f)<=8:
                    DibosonntupleA[files.index(f)-6].Fill(array('f',ListOfVariables))
                elif files.index(f)>=9 and files.index(f)<=10:
                    DYntupleA[files.index(f)-9].Fill(array('f',ListOfVariables))
                elif files.index(f)>=11 and files.index(f)<=(len(files)-1):
                    QCDPTntupleA[files.index(f)-11].Fill(array('f',ListOfVariables))

    elif tree=="stp3LNC":
        for V in InclusiveVersions:
            for f in Ffiles:
                CutsChain=ROOT.TChain(tree)
                CutsChain.Add(Base+V+f)
                entries = CutsChain.GetEntries()
                print "Entries for file ", f, " are: ", entries
                for i in xrange(entries):
                    CutsChain.GetEntry(i)
                    if CutsChain.THT<600: continue
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
                    if Ffiles.index(f)>=0 and Ffiles.index(f)<=5:            
                        if InclusiveVersions.index(V)==0: TsinglentuplesE[Ffiles.index(f)].Fill(array('f',ListOfVariables))
                        elif InclusiveVersions.index(V)==1: TsinglentuplesE1[Ffiles.index(f)].Fill(array('f',ListOfVariables))
                        elif InclusiveVersions.index(V)==2: TsinglentuplesE2[Ffiles.index(f)].Fill(array('f',ListOfVariables))
                    elif Ffiles.index(f)>=6 and Ffiles.index(f)<=8:
                        if InclusiveVersions.index(V)==0: DibosonntupleE[Ffiles.index(f)-6].Fill(array('f',ListOfVariables))
                        elif InclusiveVersions.index(V)==1: DibosonntupleE1[Ffiles.index(f)-6].Fill(array('f',ListOfVariables))
                        elif InclusiveVersions.index(V)==2: DibosonntupleE2[Ffiles.index(f)-6].Fill(array('f',ListOfVariables))
                    elif Ffiles.index(f)>=9 and Ffiles.index(f)<=10:
                        if InclusiveVersions.index(V)==0: DYntupleE[Ffiles.index(f)-9].Fill(array('f',ListOfVariables))
                        if InclusiveVersions.index(V)==1: DYntupleE1[Ffiles.index(f)-9].Fill(array('f',ListOfVariables))
                        if InclusiveVersions.index(V)==2: DYntupleE2[Ffiles.index(f)-9].Fill(array('f',ListOfVariables))
                    elif Ffiles.index(f)>=11 and Ffiles.index(f)<=(len(Ffiles)-1):
                        if InclusiveVersions.index(V)==0: QCDPTntupleE[Ffiles.index(f)-11].Fill(array('f',ListOfVariables))
                        if InclusiveVersions.index(V)==1: QCDPTntupleE1[Ffiles.index(f)-11].Fill(array('f',ListOfVariables))
                        if InclusiveVersions.index(V)==2: QCDPTntupleE2[Ffiles.index(f)-11].Fill(array('f',ListOfVariables))

        SubBKGMCArray=np.array([[TsinglentuplesA,DibosonntupleA,DYntupleA,QCDPTntupleA],
                      [TsinglentuplesE,DibosonntupleE,DYntupleE,QCDPTntupleE],
                      [TsinglentuplesE1,DibosonntupleE1,DYntupleE1,QCDPTntupleE1],
                      [TsinglentuplesE2,DibosonntupleE2,DYntupleE2,QCDPTntupleE2]])
        #SubBKGMCSampleFile="SubBKGMC_inclusive_"+InclusiveVersions[0][:-1]+"_"+InclusiveVersions[1][:-1]+"_"+InclusiveVersions[2][:-1]
        np.save(SampleFile,SubBKGMCArray)
        del(SubBKGMCArray)

#For Nm1
Nm1files = ["T-s_5318_Full_analyzed.root",
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

TreeStructureA="Nvtcs:NTI:weight:j1pt:j2pt:j3pt:j4pt:j5pt:j6pt:j1eta:j2eta:j3eta:j4eta:j5eta:j6eta:HT:NCSVM"

#Signal Sample
TsA=ROOT.TNtuple("TsA","TsA",TreeStructureA)
TtA=ROOT.TNtuple("TtA","TtA",TreeStructureA)
TtwA=ROOT.TNtuple("TtwA","TtwA",TreeStructureA)
TbarsA=ROOT.TNtuple("TbarsA","TbarsA",TreeStructureA)
TbartA=ROOT.TNtuple("TbartA","TbartA",TreeStructureA)
TbartwA=ROOT.TNtuple("TbartwA","TbartwA",TreeStructureA)
TsinglentuplesA=[TsA,TtA,TtwA,TbarsA,TbartA,TbartwA]

WWA=ROOT.TNtuple("WWA","WWA",TreeStructureA)
WZA=ROOT.TNtuple("WZA","WZA",TreeStructureA)
ZZA=ROOT.TNtuple("ZZA","ZZA",TreeStructureA)
DibosonntupleA=[WWA,WZA,ZZA]

DYBBA=ROOT.TNtuple("DYBBA","DYBBA",TreeStructureA)
DYCCA=ROOT.TNtuple("DYCCA","DYCCA",TreeStructureA)
DYntupleA=[DYBBA,DYCCA]

QCD120A=ROOT.TNtuple("QCD120A","QCD120A",TreeStructureA)
QCD170A=ROOT.TNtuple("QCD170A","QCD170A",TreeStructureA)
QCD300A=ROOT.TNtuple("QCD300A","QCD300A",TreeStructureA)
QCD470A=ROOT.TNtuple("QCD470A","QCD470A",TreeStructureA)
QCD600A=ROOT.TNtuple("QCD600A","QCD600A",TreeStructureA)
QCD800A=ROOT.TNtuple("QCD800A","QCD800A",TreeStructureA)
QCDPTntupleA=[QCD120A,QCD170A,QCD300A,QCD470A,QCD600A,QCD800A]

def ExtractingMCNm1InfoFromTree(files,tree,ListTreesNames,TreeStructureT,SampleFile):
    for f in Nm1files:
        ff=Base+InclusiveVersions[0]+f
        CutsChain=ROOT.TChain(tree)
        CutsChain.Add(ff)
        entries = CutsChain.GetEntries()
        print "Entries for file ", f, " are: ", entries
        Entries=entries
        for i in xrange(Entries):
            CutsChain.GetEntry(i)
            #M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym
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
            if Nm1files.index(f)>=0 and Nm1files.index(f)<=5:
                TsinglentuplesA[Nm1files.index(f)].Fill(array('f',ListOfVariables))
            elif Nm1files.index(f)>=6 and Nm1files.index(f)<=8:
                DibosonntupleA[Nm1files.index(f)-6].Fill(array('f',ListOfVariables))
            elif Nm1files.index(f)>=9 and Nm1files.index(f)<=10:
                DYntupleA[Nm1files.index(f)-9].Fill(array('f',ListOfVariables))
            elif Nm1files.index(f)>=11 and Nm1files.index(f)<=(len(Nm1files)-1):
                QCDPTntupleA[Nm1files.index(f)-11].Fill(array('f',ListOfVariables))

    SubBKGMCArray=np.array([[TsinglentuplesA,DibosonntupleA,DYntupleA,QCDPTntupleA]])
    #SubBKGMCSampleFile="SubBKGMC_preselection_"+InclusiveVersions[0][:-1]

    np.save(SampleFile,SubBKGMCArray)



if __name__ == '__main__':
    VersionToProcess="V1/"
    MCFiles=[]
    for i in Ffiles: MCFiles.append(Base+VersionToProcess+i)

    #ExtractingMCInfoFromTree(MCFiles,"stp",[],[],"SubBKGMC_inclusive_"+InclusiveVersions[0][:-1]+"_"+InclusiveVersions[1][:-1]+"_"+InclusiveVersions[2][:-1])
    #ExtractingMCInfoFromTree(MCFiles,"stp3LNC",[],[],"SubBKGMC_inclusive_"+InclusiveVersions[0][:-1]+"_"+InclusiveVersions[1][:-1]+"_"+InclusiveVersions[2][:-1])
    ExtractingMCNm1InfoFromTree(MCFiles,"cuts",[],[],"SubBKGMC_preselection_"+InclusiveVersions[0][:-1])

