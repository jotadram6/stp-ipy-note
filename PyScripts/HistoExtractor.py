import ROOT
import numpy as np

ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()

def HistoExtractor(Files,tree,Variable,Hname,Binning,PDFFile,Cut = ""):
    """
    Extract from each file declared on Files list
    and from the selected tree the hisogram corresponding to
    variable with settings given in Binning.
    An overlay of the histograms is printed in the PDFFile.
    A cut can be applied passing it on the Cut argument.
    
    cosm: [FillColor, FillStyle, LineColor, LineWidth, LineStyle, MarkerStyle] per file
    
    """
    
    Rfile = ROOT.TFile(PDFFile.split(".")[0]+".root", "recreate")
        
    CMC=ROOT.TCut(Cut)
    Histos=[]
    for i in xrange(len(Files)):
        Chain=ROOT.TChain(tree)
        Chain.Add(Files[i])
        Chain.Draw(Variable+" >> "+Hname[i]+Binning,CMC)
        Histos.append(ROOT.gDirectory.Get(Hname[i]))
        #Histos[-1].Sumw2(); Histos[-1].Scale(weights[i])
        Histos[-1].Write()

    ROOT.gPad.Clear()
  
    del(Chain); del(Histos); del(CMC)

if __name__=='__main__':
    M600="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M600_PAT.root"
    M650="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M650_PAT.root"
    M700="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M700_PAT.root"
    M750="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M750_PAT.root"
    M800="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M800_PAT.root"
    M850="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M850_PAT.root"
    M900="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M900_PAT.root"
    M950="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M950_PAT.root"
    M1000="/gridgroup/cms/jruizalv/WA/CMSSW_5_3_18/src/Extractors/PatExtractor/SignalGENWidth/M1000_PAT.root"
    
    files=[M600,M650,M700,M750,M800,M850,M900,M950,M1000]

    Tree="Events"
    Var="recoGenParticles_genParticles__SIM.obj.mass()"
    HistoName=["M5J_600","M5J_650","M5J_700","M5J_750","M5J_800","M5J_850","M5J_900","M5J_950","M5J_1000"]
    bins="(1600,400,1200)"
    PDF="GEN_Mass_Widths.pdf"
    CutToApply="((recoGenParticles_genParticles__SIM.obj.pdgId()==6000006) || (recoGenParticles_genParticles__SIM.obj.pdgId()==-6000006)) && (recoGenParticles_genParticles__SIM.obj.status()==3)"
    
    HistoExtractor(files,Tree,Var,HistoName,bins,PDF,CutToApply)
