import ROOT
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from array import array
import rootnotes
ROOT.gROOT.LoadMacro('tdrStyle.C')
ROOT.gROOT.LoadMacro('PUR.C')
def DPHI(x):
    if x>=np.pi: return x-2*np.pi
    elif x<-np.pi: return x+2*np.pi
    else: return x
VersionProc="V121"
Base="/home/jruizalv/"
InclusiveVersions=["Version121/","Version122/","Version123/"]

DATA_F="Full_Data.root"

datafiles = [Base+InclusiveVersions[0]+DATA_F,Base+InclusiveVersions[1]+DATA_F,Base+InclusiveVersions[2]+DATA_F]

#Style functions
def SetAxis(Histo,Axis,TOffset,TSize,LOffset,LSize,Ndiv):
    """Sets offset and size of an axis in the histogram. Axis must be 'X' or 'Y', and Histo should be a valid root histogram"""
    if Axis=='X':
        Histo.GetXaxis().SetTitleSize(TSize)
        Histo.GetXaxis().SetTitleOffset(TOffset)
        Histo.GetXaxis().SetLabelSize(LSize)
        Histo.GetXaxis().SetLabelOffset(LOffset)
        Histo.GetXaxis().SetNdivisions(Ndiv)
    elif Axis=='Y':
        Histo.GetYaxis().SetTitleSize(TSize)
        Histo.GetYaxis().SetTitleOffset(TOffset)
        Histo.GetYaxis().SetLabelSize(LSize)
        Histo.GetYaxis().SetLabelOffset(LOffset)
        Histo.GetYaxis().SetNdivisions(Ndiv)
    else: print "Please correct axis selection: Valid values are 'X' or 'Y'"
def SetCos(Hist,FillColor,FillStyle,LineColor,LineWidth,LineStyle,MarkerStyle):
    """Hist, FillColor, FillStyle, LineColor, LineWidth, LineStyle, MarkerStyle"""
    Hist.SetLineStyle(LineStyle); Hist.SetLineWidth(LineWidth); Hist.SetLineColor(LineColor)
    Hist.SetFillStyle(FillStyle); Hist.SetFillColor(FillColor)
    Hist.SetMarkerStyle(MarkerStyle)

#Corrections
PU_weight=[0.0, 0.283904, 0.223747, 0.155297, 0.26765, 0.298877, 0.723858, 0.544046, 0.536757, 0.733619, 1.0669, 1.48245, 1.80291, 1.80134, 1.58708, 1.34094, 1.15851, 1.0611, 1.02807, 1.04437, 1.08871, 1.12881, 1.15127, 1.15997, 1.15499, 1.12965, 1.07905, 1.00491, 0.914114, 0.813124, 0.707008, 0.599841, 0.495265, 0.39636, 0.306662, 0.22925, 0.166144, 0.118378, 0.0850749, 0.063948, 0.0523125, 0.0476093, 0.0478425, 0.0516782, 0.0583517, 0.0676538, 0.0795915, 0.0944514, 0.112777, 0.135238, 0.162647, 0.196085, 0.236688, 0.286083, 0.34616, 0.418813, 0.506749, 0.612955, 0.741067, 0.894819, 2.26873]
def PUR_function(TI):
  if (TI>=61) or (TI<0): return 1
  else: return PU_weight[TI]

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

TreeStructureA="M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym:NTI:weight"
TreeStructure="M5J:DRHJ:DRWH:RelHT:M2HP:DRTp6thJ:HM:chi2:MTHAsym"

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
CutHT = ROOT.TCut("THT>550")
Cut1 = ROOT.TCut("chi2<820")
CutDRbb = ROOT.TCut("DRHJ<=1.2")
CutDRWH = ROOT.TCut("DRWH>=1.6 && DRWH<=4.0")
CutHM = ROOT.TCut("HM>=105 && HM<=145")
CutM2HP = ROOT.TCut("M2HP>8.0")
CutRelHT = ROOT.TCut("RelHT>=0.69")
CutDRTp6thJ = ROOT.TCut("DRTp6thJ>4.7")
CutMTHAsym = ROOT.TCut("MTHAsym>=0.1 && MTHAsym<=0.3")

Lumi=19694.513

SWeight=Lumi*(0.577/0.94)*0.1437/99464
TWeight=Lumi*247.74/61941200
Q500Weight=Lumi*8426.0/29019521
Q1000Weight=Lumi*204.0/13438527
QWeights=[Q500Weight,Q1000Weight]
NevtsMassPoints=[95167.,98817.,99464.,99375.,95801.,99257.,99174.,95960.,99078.]
XSNevtsMassPoints=[0.2154,0.1778,0.1437,0.1186,0.1,0.0843,0.0726,0.0626,0.0539]
NWeights=Lumi*(0.577/0.94)*np.array(XSNevtsMassPoints)/np.array(NevtsMassPoints)

#Propagation of error functions
def DivE(x,y,dx,dy):
    return (x/y)*((dx/x)+(dy/y))

def MulE(x,y,dx,dy):
    return (x*y)*((dx/x)+(dy/y))

def SqrtE(x,dx):
    return np.sqrt(x)*0.5*(dx/x)

def EffE(eff,N):
    return np.sqrt((eff*(1-eff))/N)

#Getting Info strings
def GetMR(Histo):
    return "Mean={0:.2f}".format(Histo.GetMean())+"#pm{0:.2f}".format(Histo.GetMeanError())+" RMS={0:.2f}".format(Histo.GetRMS())+"#pm{0:.2f}".format(Histo.GetRMSError())

def GetEWI(Histo):
    INT=Histo.Integral(0,Histo.GetNbinsX()+1)
    ENT=Histo.GetEntries()
    W=INT/ENT
    #return "Entries={0:.2f}".format(ENT)+" W={0:.2f}".format(W)+" Int={0:.2f}".format(INT)+"+-{0:.2f}".format(W*np.sqrt(ENT))
    return "Entries={0:.2f}".format(ENT)+" Int={0:.2f}".format(INT)+"#pm{0:.2f}".format(W*np.sqrt(ENT))
