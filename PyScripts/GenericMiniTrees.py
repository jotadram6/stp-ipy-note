import ROOT
import numpy as np
from array import array
from BTagEfficiencies import *

Base="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/"

DATA_F="Full_Data.root"

TreeStructureA="THT:M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym:NTI:weight:M2ndT:NCSVM"
TreeStructure="THT:M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym:M2ndT:NCSVM"

TreeStructureANm1="Nvtcs:NTI:weight:j1pt:j2pt:j3pt:j4pt:j5pt:j6pt:j1eta:j2eta:j3eta:j4eta:j5eta:j6eta:HT:NCSVM"
TreeStructureNm1="Nvtcs:j1pt:j2pt:j3pt:j4pt:j5pt:j6pt:j1eta:j2eta:j3eta:j4eta:j5eta:j6eta:HT:NCSVM"

NsignalFiles=9

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
        if CutsChain.THT<500: continue
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
                               Top2.M(),
                               CutsChain.Number_CSVMbtagged_jets]
        elif tree=="stp3LNC":
            if CutsChain.First_W_Jet3L.Pt()<20 or CutsChain.Second_W_Jet3L.Pt()<20: continue
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
        elif tree=="cuts":
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

def BtagWeight(JetsPT,JetsETA,JetsID,JetsCSV,FileIndex,EffMatrix):
    mcTag = 1.; mcNoTag = 1.; dataTag = 1.; dataNoTag = 1.; errTag = 0.; errNoTag = 0.
    err1 = 0; err2 = 0; err3 = 0; err4 = 0;
    for j in xrange(JetsPT.size()):
        eta=JetsETA.at(j)
        pt=JetsPT.at(j)
        ID=JetsID.at(j)
        if pt<30 or fabs(eta)>=2.4: continue
        SF=get_SF_btag(pt,eta,ID)
        eff=EffMatrix[FileIndex][getptbin_for_btag(pt),get_eta_bin_jet(eta),get_flav_bin_jet(ID)]
        if CSVM(JetsCSV.at(j),JetsETA.at(j)):
            mcTag *= eff
            dataTag *= eff*SF[0]
            
            if abs(ID)==5 or abs(ID)==4:  err1 += SF[1]/SF[0] #correlated for b/c
            else: err3 += SF[1]/SF[0] #correlated for light
        else:
            mcNoTag *= (1- eff)
            dataNoTag *= (1- eff*SF[0]) 
            
            if abs(ID)==5 or abs(ID)==4: err2 += (-eff*SF[1])/(1-eff*SF[0]) #correlated for b/c
            else: err4 +=  (-eff*SF[1])/(1-eff*SF[0]) #correlated for light
    if (mcNoTag*mcTag)!=0: wtbtag = ( dataNoTag * dataTag ) / ( mcNoTag * mcTag )
    else: wtbtag=0.
    wtbtagErr = np.sqrt( ((err1+err2)**2) + ((err3 + err4)**2) ) * wtbtag #un-correlated for b/c and light
    return wtbtag

def ExtractingMCMethod1aInfoFromTree(files,tree,ListTreesNames,TreeStructureT,SampleFile,EntDiv,WhichPart,EfficiencyFile):
    AllSamples=[]
    Eff=np.load(EfficiencyFile)
    for f in files:
        CutsChain=ROOT.TChain(tree)
        CutsChain.Add(f)
        entries = CutsChain.GetEntries()
        if WhichPart<EntDiv-1: Entries=entries/EntDiv
        else: Entries=entries-(entries/EntDiv)*(EntDiv-1)
        if files.index(f)>=0 and files.index(f)<=NsignalFiles-1: print "Filling signal..."
        elif files.index(f)>0: print "Filling bkgs..."
        print "Entries for file ", f, " are: ", Entries
        TempTree= ROOT.TNtuple(ListTreesNames[files.index(f)],ListTreesNames[files.index(f)],TreeStructureT)
        for i in xrange(Entries):
            if WhichPart==0: CutsChain.GetEntry(i)
            else: CutsChain.GetEntry(((entries/EntDiv)*WhichPart)+i)
            #CutsChain.GetEntry(i)
            if CutsChain.THT<550: continue
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
                                   BtagWeight(CutsChain.JetsPT,CutsChain.JetsETA,CutsChain.Flavor,CutsChain.JetsCSV,files.index(f),Eff),
                                   Top2.M(),
                                   CutsChain.Number_CSVMbtagged_jets]
            elif tree=="stp3LNC":
                if CutsChain.First_W_Jet3L.Pt()<20 or CutsChain.Second_W_Jet3L.Pt()<20: continue
                HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs3L.X(),CutsChain.Reconstructed_Higgs3L.Y(),CutsChain.Reconstructed_Higgs3L.Z(),CutsChain.Reconstructed_Higgs3L.T())
                Higgs1stJV=ROOT.TLorentzVector(CutsChain.First_Higgs_Jet3L.X(),CutsChain.First_Higgs_Jet3L.Y(),CutsChain.First_Higgs_Jet3L.Z(),CutsChain.First_Higgs_Jet3L.T())
                Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet3L.X(),CutsChain.Second_Higgs_Jet3L.Y(),CutsChain.Second_Higgs_Jet3L.Z(),CutsChain.Second_Higgs_Jet3L.T())
                J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
                TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime3L.X(),CutsChain.Reconstructed_Tprime3L.Y(),CutsChain.Reconstructed_Tprime3L.Z(),CutsChain.Reconstructed_Tprime3L.T())
                W1V=ROOT.TLorentzVector(CutsChain.Reconstructed_W3L.X(),CutsChain.Reconstructed_W3L.Y(),CutsChain.Reconstructed_W3L.Z(),CutsChain.Reconstructed_W3L.T())
                Top2=HiggsV+J6thV
                W2=Higgs2ndJV+J6thV
                TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet3L.X(),CutsChain.Top_Jet3L.Y(),CutsChain.Top_Jet3L.Z(),CutsChain.Top_Jet3L.T())
                if Higgs1stJV.DeltaR(Higgs2ndJV)>1.2: continue
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
            elif tree=="cuts":
               ListOfVariables = [CutsChain.Vertices,
                                  CutsChain.Number_True_Interactions,
                                  BtagWeight(CutsChain.JetsPT,CutsChain.JetsETA,CutsChain.Flavor,CutsChain.JetsCSV,files.index(f),Eff),                        
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

def ExtractingInfoFromTree_VectorVersion(File,tree,ListTreesNames,TreeStructureT,SampleFile,EntDiv,WhichPart):
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
        if CutsChain.THT<550: continue
        if tree=="stp3LNC":
            Chi2=[]
            NCombinations=0
            #print "Event", i, "Number of combination:", CutsChain.Jet6thX.size()
            for j in xrange(CutsChain.Jet6thX.size()):
                FirstWJ=ROOT.TLorentzVector(CutsChain.First_W_Jet3LX.at(j),CutsChain.First_W_Jet3LY.at(j),CutsChain.First_W_Jet3LZ.at(j),CutsChain.First_W_Jet3LT.at(j))
                SecondWJ=ROOT.TLorentzVector(CutsChain.Second_W_Jet3LX.at(j),CutsChain.Second_W_Jet3LY.at(j),CutsChain.Second_W_Jet3LZ.at(j),CutsChain.Second_W_Jet3LT.at(j))
                #print FirstWJ.Pt(), SecondWJ.Pt()
                if FirstWJ.Pt()<20 or SecondWJ.Pt()<20: continue
                NCombinations+=1
                Chi2.append(CutsChain.HiggsChi2.at(j)+CutsChain.TopChi2.at(j))
            if NCombinations==0: continue
            MCI=Chi2.index(min(Chi2))

            HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs3LX.at(MCI),CutsChain.Reconstructed_Higgs3LY.at(MCI),CutsChain.Reconstructed_Higgs3LZ.at(MCI),CutsChain.Reconstructed_Higgs3LT.at(MCI))
            Higgs1stJV=ROOT.TLorentzVector(CutsChain.First_Higgs_Jet3LX.at(MCI),CutsChain.First_Higgs_Jet3LY.at(MCI),CutsChain.First_Higgs_Jet3LZ.at(MCI),CutsChain.First_Higgs_Jet3LT.at(MCI))
            Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet3LX.at(MCI),CutsChain.Second_Higgs_Jet3LY.at(MCI),CutsChain.Second_Higgs_Jet3LZ.at(MCI),CutsChain.Second_Higgs_Jet3LT.at(MCI))
            J6thV=ROOT.TLorentzVector(CutsChain.Jet6thX.at(MCI),CutsChain.Jet6thY.at(MCI),CutsChain.Jet6thZ.at(MCI),CutsChain.Jet6thT.at(MCI))
            TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime3LX.at(MCI),CutsChain.Reconstructed_Tprime3LY.at(MCI),CutsChain.Reconstructed_Tprime3LZ.at(MCI),CutsChain.Reconstructed_Tprime3LT.at(MCI))
            W1V=ROOT.TLorentzVector(CutsChain.Reconstructed_W3LX.at(MCI),CutsChain.Reconstructed_W3LY.at(MCI),CutsChain.Reconstructed_W3LZ.at(MCI),CutsChain.Reconstructed_W3LT.at(MCI))
            Top2=HiggsV+J6thV
            W2=Higgs2ndJV+J6thV
            #TopJV=ROOT.TLorentzVector(CutsChain.ReconstructedTop3LNCX.at(MCI),CutsChain.ReconstructedTop3LNCY.at(MCI),CutsChain.ReconstructedTop3LNCZ.at(MCI),CutsChain.ReconstructedTop3LNCT.at(MCI))
            TopV=ROOT.TLorentzVector(CutsChain.Reconstructed_Top3LX.at(MCI),CutsChain.Reconstructed_Top3LY.at(MCI),CutsChain.Reconstructed_Top3LZ.at(MCI),CutsChain.Reconstructed_Top3LT.at(MCI))
            ListOfVariables = [CutsChain.THT,
                               TprimeV.M(),
                               Higgs1stJV.DeltaR(Higgs2ndJV),
                               HiggsV.DeltaR(W1V),
                               (HiggsV.Pt()+TopV.Pt())/CutsChain.THT,
                               (Top2.M()+W2.M())/HiggsV.M(),
                               TprimeV.DeltaR(J6thV),
                               HiggsV.M(),
                               min(Chi2),
                               (TopV.M()-HiggsV.M())/(TopV.M()+HiggsV.M()),
                               NCombinations]

        TempTree.Fill(array('f',ListOfVariables))
    AllSamples=np.array([TempTree])
    np.save(SampleFile,AllSamples)
    del(TempTree); del(AllSamples)

def ExtractingMCInfoFromTree_VectorVersion(files,tree,ListTreesNames,TreeStructureT,SampleFile,EntDiv,WhichPart):
    AllSamples=[]
    for f in files:
        CutsChain=ROOT.TChain(tree)
        CutsChain.Add(f)
        entries = CutsChain.GetEntries()
        if WhichPart<EntDiv-1: Entries=entries/EntDiv
        else: Entries=entries-(entries/EntDiv)*(EntDiv-1)
        if files.index(f)>=0 and files.index(f)<=NsignalFiles-1: print "Filling signal..."
        elif files.index(f)>0: print "Filling bkgs..."
        print "Entries for file ", f, " are: ", Entries
        TempTree= ROOT.TNtuple(ListTreesNames[files.index(f)],ListTreesNames[files.index(f)],TreeStructureT)
        for i in xrange(Entries):
            if WhichPart==0: CutsChain.GetEntry(i)
            else: CutsChain.GetEntry(((entries/EntDiv)*WhichPart)+i)
            if CutsChain.THT<550: continue
            if tree=="stp3LNC":
                Chi2=[]
                NCombinations=0
                #print "Event", i, "Number of combination:", CutsChain.Jet6thX.size()
                for j in xrange(CutsChain.Jet6thX.size()):
                    FirstWJ=ROOT.TLorentzVector(CutsChain.First_W_Jet3LX.at(j),CutsChain.First_W_Jet3LY.at(j),CutsChain.First_W_Jet3LZ.at(j),CutsChain.First_W_Jet3LT.at(j))
                    SecondWJ=ROOT.TLorentzVector(CutsChain.Second_W_Jet3LX.at(j),CutsChain.Second_W_Jet3LY.at(j),CutsChain.Second_W_Jet3LZ.at(j),CutsChain.Second_W_Jet3LT.at(j))
                    #print FirstWJ.Pt(), SecondWJ.Pt()
                    if FirstWJ.Pt()<20 or SecondWJ.Pt()<20: continue
                    NCombinations+=1
                    Chi2.append(CutsChain.HiggsChi2.at(j)+CutsChain.TopChi2.at(j))
                if NCombinations==0: continue
                MCI=Chi2.index(min(Chi2))

                HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs3LX.at(MCI),CutsChain.Reconstructed_Higgs3LY.at(MCI),CutsChain.Reconstructed_Higgs3LZ.at(MCI),CutsChain.Reconstructed_Higgs3LT.at(MCI))
                Higgs1stJV=ROOT.TLorentzVector(CutsChain.First_Higgs_Jet3LX.at(MCI),CutsChain.First_Higgs_Jet3LY.at(MCI),CutsChain.First_Higgs_Jet3LZ.at(MCI),CutsChain.First_Higgs_Jet3LT.at(MCI))
                Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet3LX.at(MCI),CutsChain.Second_Higgs_Jet3LY.at(MCI),CutsChain.Second_Higgs_Jet3LZ.at(MCI),CutsChain.Second_Higgs_Jet3LT.at(MCI))
                J6thV=ROOT.TLorentzVector(CutsChain.Jet6thX.at(MCI),CutsChain.Jet6thY.at(MCI),CutsChain.Jet6thZ.at(MCI),CutsChain.Jet6thT.at(MCI))
                TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime3LX.at(MCI),CutsChain.Reconstructed_Tprime3LY.at(MCI),CutsChain.Reconstructed_Tprime3LZ.at(MCI),CutsChain.Reconstructed_Tprime3LT.at(MCI))
                W1V=ROOT.TLorentzVector(CutsChain.Reconstructed_W3LX.at(MCI),CutsChain.Reconstructed_W3LY.at(MCI),CutsChain.Reconstructed_W3LZ.at(MCI),CutsChain.Reconstructed_W3LT.at(MCI))
                Top2=HiggsV+J6thV
                W2=Higgs2ndJV+J6thV
                #TopJV=ROOT.TLorentzVector(CutsChain.ReconstructedTop3LNCX.at(MCI),CutsChain.ReconstructedTop3LNCY.at(MCI),CutsChain.ReconstructedTop3LNCZ.at(MCI),CutsChain.ReconstructedTop3LNCT.at(MCI))
                TopV=ROOT.TLorentzVector(CutsChain.Reconstructed_Top3LX.at(MCI),CutsChain.Reconstructed_Top3LY.at(MCI),CutsChain.Reconstructed_Top3LZ.at(MCI),CutsChain.Reconstructed_Top3LT.at(MCI))
                ListOfVariables = [CutsChain.THT,
                                   TprimeV.M(),
                                   Higgs1stJV.DeltaR(Higgs2ndJV),
                                   HiggsV.DeltaR(W1V),
                                   (HiggsV.Pt()+TopV.Pt())/CutsChain.THT,
                                   (Top2.M()+W2.M())/HiggsV.M(),
                                   TprimeV.DeltaR(J6thV),
                                   HiggsV.M(),
                                   min(Chi2),
                                   (TopV.M()-HiggsV.M())/(TopV.M()+HiggsV.M()),
                                   NCombinations]

                TempTree.Fill(array('f',ListOfVariables))
            AllSamples.append(TempTree)
        del(TempTree)
    AllSamples=np.array(AllSamples)
    np.save(SampleFile,AllSamples)
    del(AllSamples)

"""def ExtractingCombinationsInfoFromTree(File,ListTreesNames,TreeStructureT,SampleFile,EntDiv,WhichPart):
    
    CutsChain=ROOT.TChain("stp")
    CutsChain.Add(File)
    entries = CutsChain.GetEntries()
    if WhichPart<EntDiv-1: Entries=entries/EntDiv
    else: Entries=entries-(entries/EntDiv)*(EntDiv-1)
    print "Entries for file ", File, " are: ", entries
    TempTree= ROOT.TNtuple(ListTreesNames,ListTreesNames,TreeStructureT)
    
    for i in xrange(Entries):
        if WhichPart==0: CutsChain.GetEntry(i)
        else: CutsChain.GetEntry(((entries/EntDiv)*WhichPart)+i)
        if CutsChain.THT<500: continue
        #M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym
        
        elif tree=="cuts":
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
    del(TempTree); del(AllSamples)"""

if __name__ == '__main__':

    VersionToProcess="V_QCDEstim/"
    N=40 #Subdivisions to process TTbar and Data control sample

    ######
    #DATA#
    ######
    DATAFiles=Base+VersionToProcess+DATA_F
    
    DoSSData=False; DoCSData=False; DoNm1Data=False
    if DoSSData: ExtractingDATAInfoFromTree(DATAFiles,"stp","DatantupleA",TreeStructure,"DataA_2ndTopMass_NCSVM_"+VersionToProcess[:-1],1,0)
    if DoCSData or DoNm1Data:
        for i in xrange(N):
            #if i<1: continue
            if DoCSData: ExtractingDATAInfoFromTree(DATAFiles,"stp3LNC","DatantupleE",TreeStructure,"DataE"+str(i)+"_"+VersionToProcess[:-1],N,i)
            if DoNm1Data: ExtractingDATAInfoFromTree(DATAFiles,"cuts","DatantupleA",TreeStructureNm1,"Data_preselection"+str(i)+"_"+VersionToProcess[:-1],N,i)

    ####
    #MC#\\\\\\...____...//////
    ####
    MC_files = ["TpJetM600_5318_Full_analyzed.root",
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

    MCFiles=[]
    for i in MC_files: MCFiles.append(Base+VersionToProcess+i)
    
    BaseEff="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/PyScripts/"
    EffFile=BaseEff+"BTaggingEff_PerMCSample_30MinJetPT_V8.npy"
    
    ListTreesNamesA=["S600ntupleA","S650ntupleA","S700ntupleA","S750ntupleA","S800ntupleA","S850ntupleA","S900ntupleA","S950ntupleA","S1000ntupleA","TntupleA","Q500ntupleA","Q1000ntupleA",
                     "TsA","TtA","TtwA","TbarsA","TbartA","TbartwA","WWA","WZA","ZZA","DYBBA","DYCCA","QCD120A","QCD170A","QCD300A","QCD470A","QCD600A","QCD800A"]

    DoSSMC=False; DoCSMC=False; DoCSTTMC=False; DoNm1MC=False
    if DoSSMC: ExtractingMCMethod1aInfoFromTree(MCFiles,"stp",ListTreesNamesA,TreeStructureA,"SignalSample_2ndTopMass_NCSVM_"+VersionToProcess[:-1],1,0,EffFile)
    if DoCSMC:
        ExtractingMCMethod1aInfoFromTree(MCFiles[:9],"stp3LNC",ListTreesNamesA[:9],TreeStructure,"ControlSample_SignalMassPoints_"+VersionToProcess[:-1],1,0,EffFile)
        ExtractingMCMethod1aInfoFromTree(MCFiles[10:12],"stp3LNC",ListTreesNamesA[10:12],TreeStructure,"ControlSample_QCDHT_"+VersionToProcess[:-1],1,0,EffFile)
        ExtractingMCMethod1aInfoFromTree(MCFiles[12:],"stp3LNC",ListTreesNamesA[12:],TreeStructure,"ControlSample_SubBKGMC_"+VersionToProcess[:-1],1,0,EffFile)
    if DoCSTTMC:
        for i in xrange(N):
            #if i<12: continue
            ExtractingMCMethod1aInfoFromTree(MCFiles[9:10],"stp3LNC",ListTreesNamesA[9:10],TreeStructure,"ControlSample_TTJets_DRleq1p2_"+str(i)+"_"+VersionToProcess[:-1],N,i,EffFile)
    if DoNm1MC: ExtractingMCMethod1aInfoFromTree(MCFiles,"cuts",ListTreesNamesA,TreeStructureANm1,"SignalSample_preselection_"+VersionToProcess[:-1],1,0,EffFile)

    ##################################
    #Control sample in vector version#
    ##################################
    
    VectorVersion="V8_VectorControlSample/"
    N=40
    TreeStructureVV="THT:M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym:M2ndT:NCSVM:NComb"

    #Data
    VVDATAFiles=Base+VectorVersion+DATA_F

    #for i in xrange(N):
        #if i<1: continue
        #ExtractingInfoFromTree_VectorVersion(VVDATAFiles,"stp3LNC","DatantupleE",TreeStructureVV,"DataE"+str(i)+"_"+VectorVersion[:-1],N,i)

    #MC
    VVMCFiles=[]
    for i in MC_files: VVMCFiles.append(Base+VectorVersion+i)

    ExtractingMCInfoFromTree_VectorVersion(VVMCFiles[:9],"stp3LNC",ListTreesNamesA[:9],TreeStructureVV,"ControlSample_SignalMassPoints_"+VectorVersion[:-1],1,0)
    ExtractingMCInfoFromTree_VectorVersion(VVMCFiles[10:12],"stp3LNC",ListTreesNamesA[10:12],TreeStructureVV,"ControlSample_QCDHT_"+VectorVersion[:-1],1,0)
    ExtractingMCInfoFromTree_VectorVersion(VVMCFiles[12:],"stp3LNC",ListTreesNamesA[12:],TreeStructureVV,"ControlSample_SubBKGMC_"+VectorVersion[:-1],1,0)
    for i in xrange(N):
        #if i<1: continue
        ExtractingMCInfoFromTree_VectorVersion(VVMCFiles[9:10],"stp3LNC",ListTreesNamesA[9:10],TreeStructureVV,"ControlSample_TTJets_"+str(i)+"_"+VectorVersion[:-1],N,i)
