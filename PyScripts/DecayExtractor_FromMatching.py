from HistoExtractor import *
import commands

CentralPath="/sps/cms/ruizalva/SL6/CMSSW_5_3_18/src/Extractors/PatExtractor/bin/MergedAnalysisResults/V1_MC_Matched/"

def ExtractingTp_STP(Files,tree,ROP,HistosN):

    Rfile = ROOT.TFile(ROP+".root", "recreate")
    for i in xrange(len(Files)):
        Chain=ROOT.TChain(tree)
        #RootFiles=commands.getoutput("ls "+CentralPath+Files[i])
        #RootFiles=RootFiles.split("\n")
        #for j in RootFiles: Chain.Add(CentralPath+Files[i]+j)
        Chain.Add(CentralPath+Files[i])
        Entries = Chain.GetEntries()
        print "Processing", Entries, "events..."
        H1=ROOT.TH1F(HistosN[i],HistosN[i],2400,400,1600)
        for j in xrange(Entries):
            Chain.GetEntry(j)
            H_B1=ROOT.TLorentzVector(Chain.First_True_Higgs_Jet.X(),Chain.First_True_Higgs_Jet.Y(),Chain.First_True_Higgs_Jet.Z(),Chain.First_True_Higgs_Jet.T())
            H_B2=ROOT.TLorentzVector(Chain.Second_True_Higgs_Jet.X(),Chain.Second_True_Higgs_Jet.Y(),Chain.Second_True_Higgs_Jet.Z(),Chain.Second_True_Higgs_Jet.T())
            W_Q1=ROOT.TLorentzVector(Chain.First_True_W_Jet.X(),Chain.First_True_W_Jet.Y(),Chain.First_True_W_Jet.Z(),Chain.First_True_W_Jet.T())
            W_Q2=ROOT.TLorentzVector(Chain.Second_True_W_Jet.X(),Chain.Second_True_W_Jet.Y(),Chain.Second_True_W_Jet.Z(),Chain.Second_True_W_Jet.T())
            T_J=ROOT.TLorentzVector(Chain.True_Top_Jet.X(),Chain.True_Top_Jet.Y(),Chain.True_Top_Jet.Z(),Chain.True_Top_Jet.T())
            Tp=H_B1+H_B2+W_Q1+W_Q2+T_J
            #print T.M()
            H1.Fill(Tp.M())
        H1.Write()
        del(H1); del(Chain)
            

if __name__=='__main__':
    M600="TpJetM600_5318_Full_analyzed.root"
    M650="TpJetM650_5318_Full_analyzed.root"
    M700="TpJetM700_5318_Full_analyzed.root"
    M750="TpJetM750_5318_Full_analyzed.root"
    M800="TpJetM800_5318_Full_analyzed.root"
    M850="TpJetM850_5318_Full_analyzed.root"
    M900="TpJetM900_5318_Full_analyzed.root"
    M950="TpJetM950_5318_Full_analyzed.root"
    M1000="TpJetM1000_5318_Full_analyzed.root"
    
    files=[M600,M650,M700,M750,M800,M850,M900,M950,M1000]

    Tree="stp"
    HistoName=["M5J_600","M5J_650","M5J_700","M5J_750","M5J_800","M5J_850","M5J_900","M5J_950","M5J_1000"]
    DecayFile="Tp_Mass_Widths_Decay_From_Matching"

    ExtractingTp_STP(files,Tree,DecayFile,HistoName)
