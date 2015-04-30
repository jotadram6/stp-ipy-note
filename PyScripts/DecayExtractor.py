from HistoExtractor import *
import commands

CentralPath="/sps/cms/ruizalva/PAT_prod/CMSSW_5_3_18/src/Extractors/Extracted_MC/WithJER/"

def ExtractingTp(Files,tree,ROP,HistosN):

    Rfile = ROOT.TFile(ROP+".root", "recreate")
    for i in xrange(len(Files)):
        Chain=ROOT.TChain(tree)
        RootFiles=commands.getoutput("ls "+CentralPath+Files[i])
        RootFiles=RootFiles.split("\n")
        for j in RootFiles: Chain.Add(CentralPath+Files[i]+j)
        Entries = Chain.GetEntries()
        print "Processing", Entries, "events..."
        H1=ROOT.TH1F(HistosN[i],HistosN[i],2400,400,1600)
        for j in xrange(Entries):
            Chain.GetEntry(j)
            PDGID=Chain.MC_type
            PX=Chain.MC_px
            PY=Chain.MC_py
            PZ=Chain.MC_pz
            E=Chain.MC_e
            H=ROOT.TLorentzVector(0.,0.,0.,0.)
            t=ROOT.TLorentzVector(0.,0.,0.,0.)
            for k in xrange(len(PDGID)):
                if PDGID[k]==25: H.SetPxPyPzE(PX[k],PY[k],PZ[k],E[k])
                elif np.abs(PDGID[k])==6: t.SetPxPyPzE(PX[k],PY[k],PZ[k],E[k])
            #print "Higgs:", H.Px(), H.Py(), H.Pz(), H.E()
            #print "top:", t.Px(), t.Py(), t.Pz(), t.E()
            T=H+t
            #print T.M()
            H1.Fill(T.M())
        H1.Write()
        del(H1); del(Chain); del(PDGID)
            

"""            for j in xrange(len(PDGID)):
                if PDGID[j]==5 and Chain.recoGenParticles_genParticles__SIM.obj.mother(0).pdgId()==25 and Chain.recoGenParticles_genParticles__SIM.obj.status()==3:
                    H_B=ROOT.TLorentzVector(0.,0.,0.,0.)
                    H_B.SetPxPyPzE(CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).px(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).py(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).pz(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).energy())
            elif PDGID==-5 and Chain.recoGenParticles_genParticles__SIM.obj.mother(0).pdgId()==25 and Chain.recoGenParticles_genParticles__SIM.obj.status()==3:
                H_Bbar=ROOT.TLorentzVector(0.,0.,0.,0.)
                H_Bbar.SetPxPyPzE(CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).px(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).py(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).pz(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).energy())
            elif np.abs(PDGID)==5 and np.abs(Chain.recoGenParticles_genParticles__SIM.obj.mother(0).pdgId())==6 and Chain.recoGenParticles_genParticles__SIM.obj.status()==3:
                t_B=ROOT.TLorentzVector(0.,0.,0.,0.)
                t_B.SetPxPyPzE(CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).px(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).py(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).pz(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).energy())
            elif (PDGID<=5 and PDGID>0) and np.abs(Chain.recoGenParticles_genParticles__SIM.obj.mother(0).pdgId())==24 and Chain.recoGenParticles_genParticles__SIM.obj.status()==3:
                W_q=ROOT.TLorentzVector(0.,0.,0.,0.)
                W_q.SetPxPyPzE(CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).px(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).py(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).pz(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).energy())
            elif (PDGID>=-5 and PDGID<0) and np.abs(Chain.recoGenParticles_genParticles__SIM.obj.mother(0).pdgId())==24 and Chain.recoGenParticles_genParticles__SIM.obj.status()==3:
                W_qbar=ROOT.TLorentzVector(0.,0.,0.,0.)
                W_qbar.SetPxPyPzE(CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).px(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).py(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).pz(),CutsChain.recoGenParticles_genParticles__SIM.obj.mother(0).energy())
            print "Higgs b:", H_B.Px(), H_B.Py(), H_B.Pz(), H_B.E()
            print "Higgs b bar:", H_Bbar.Px(), H_Bbar.Py(), H_Bbar.Pz(), H_Bbar.E()
            print "top b:", t_B.Px(), t_B.Py(), t_B.Pz(), t_B.E()
            print "W q:", W_q.Px(), W_q.Py(), W_q.Pz(), W_q.E()
            print "Q q bar:", W_qbar.Px(), W_qbar.Py(), W_qbar.Pz(), W_qbar.E()

        del(Chain)"""

if __name__=='__main__':
    M600="TpJetM600_5318/"
    M650="TpJetM650_5318/"
    M700="TpJetM700_5318/"
    M750="TpJetM750_5318/"
    M800="TpJetM800_5318/"
    M850="TpJetM850_5318/"
    M900="TpJetM900_5318/"
    M950="TpJetM950_5318/"
    M1000="TpJetM1000_5318/"
    
    files=[M600,M650,M700,M750,M800,M850,M900,M950,M1000]

    Tree="MC"
    Var="recoGenParticles_genParticles__SIM.obj.mass()"
    HistoName=["M5J_600","M5J_650","M5J_700","M5J_750","M5J_800","M5J_850","M5J_900","M5J_950","M5J_1000"]
    bins="(1600,400,1200)"
    PDF="GEN_Mass_Widths.pdf"
    CutToApply="((recoGenParticles_genParticles__SIM.obj.pdgId()==6000006) || (recoGenParticles_genParticles__SIM.obj.pdgId()==-6000006)) && (recoGenParticles_genParticles__SIM.obj.status()==3)"
    
    #HistoExtractor(files,Tree,Var,HistoName,bins,PDF,CutToApply)

    DecayFile="GEN_Mass_Widths_Decay"
    ExtractingTp(files,Tree,DecayFile,HistoName)

"""
import ROOT
Chain=ROOT.TChain("MC")
Chain.Add("/sps/cms/ruizalva/PAT_prod/CMSSW_5_3_18/src/Extractors/Extracted_MC/WithJER/TpJetM700_5318/extracted_mc_1_1_2Lm.root")
Entries = Chain.GetEntries()
Chain.GetEntry(0)
PDGID=Chain.MC_type
for i in PDGID: print i
"""
