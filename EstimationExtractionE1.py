from Generic import *

TreeStructure="M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym"

#datafiles = ["/home/jruizalv/Version121/Full_Data.root"]

DataE = ROOT.TNtuple("DatantupleE","DatantupleE",TreeStructure)

CutsChain=ROOT.TChain("stp3LNC")
CutsChain.Add(datafiles[1])
entries = CutsChain.GetEntries()
print "Entries for file ", datafiles[1], " are: ", entries
Entries=entries
for i in xrange(Entries):
    CutsChain.GetEntry(i)
    HiggsV=ROOT.TLorentzVector(CutsChain.Reconstructed_Higgs3L.X(),CutsChain.Reconstructed_Higgs3L.Y(),CutsChain.Reconstructed_Higgs3L.Z(),CutsChain.Reconstructed_Higgs3L.T())
    Higgs1stJV=ROOT.TLorentzVector(CutsChain.First_Higgs_Jet3L.X(),CutsChain.First_Higgs_Jet3L.Y(),CutsChain.First_Higgs_Jet3L.Z(),CutsChain.First_Higgs_Jet3L.T())
    Higgs2ndJV=ROOT.TLorentzVector(CutsChain.Second_Higgs_Jet3L.X(),CutsChain.Second_Higgs_Jet3L.Y(),CutsChain.Second_Higgs_Jet3L.Z(),CutsChain.Second_Higgs_Jet3L.T())
    J6thV=ROOT.TLorentzVector(CutsChain.Jet6th.X(),CutsChain.Jet6th.Y(),CutsChain.Jet6th.Z(),CutsChain.Jet6th.T())
    TprimeV=ROOT.TLorentzVector(CutsChain.Reconstructed_Tprime3L.X(),CutsChain.Reconstructed_Tprime3L.Y(),CutsChain.Reconstructed_Tprime3L.Z(),CutsChain.Reconstructed_Tprime3L.T())
    W1V=ROOT.TLorentzVector(CutsChain.Reconstructed_W3L.X(),CutsChain.Reconstructed_W3L.Y(),CutsChain.Reconstructed_W3L.Z(),CutsChain.Reconstructed_W3L.T())
    Top2=HiggsV+J6thV
    W2=Higgs2ndJV+J6thV
    TopJV=ROOT.TLorentzVector(CutsChain.Top_Jet3L.X(),CutsChain.Top_Jet3L.Y(),CutsChain.Top_Jet3L.Z(),CutsChain.Top_Jet3L.T())
    #M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym
    ListOfVariables = [CutsChain.Reconstructed_Tprime3L.M(),
                        Higgs1stJV.DeltaR(Higgs2ndJV),
                        HiggsV.DeltaR(W1V),
                        (CutsChain.Reconstructed_Higgs3L.Pt()+CutsChain.Reconstructed_Top3L.Pt())/CutsChain.THT,
                        (Top2.M()+W2.M())/CutsChain.Reconstructed_Higgs3L.M(),
                        TprimeV.DeltaR(J6thV),
                        CutsChain.Reconstructed_Higgs3L.M(),
                        (CutsChain.HiggsChi2+CutsChain.TopChi2),
                        (CutsChain.Reconstructed_Top3L.M()-CutsChain.Reconstructed_Higgs3L.M())/(CutsChain.Reconstructed_Top3L.M()+CutsChain.Reconstructed_Higgs3L.M())]
    DataE.Fill(array('f',ListOfVariables))

DataEArray=np.array([DataE]); DataESampleFile="DataE1"+InclusiveVersions[1][:-1]
np.save(DataESampleFile,DataEArray)

