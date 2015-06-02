from Generic import *

def HistoOverDrawer(Files,Hname,ReBin,PDFFile,weights,Normalized,Units,XaxisT,stats,cosm,LOG,leg,YRange,XRange):
    Histos=[]
    Maxima=[]
    F=[]
    Titles=[]
    for i in xrange(len(Files)):
        if isinstance(Files[i],str):
            F.append(ROOT.TFile(Files[i]))
            for j in xrange(len(Hname[0])):
                Histos.append(F[-1].Get(Hname[i][j])); Titles.append(Hname[i][j])
                Histos[-1].Sumw2(); Histos[-1].Scale(weights[j]); Histos[-1].Rebin(ReBin) #Apllying weight and rebining for the histo
                Maxima.append(Histos[-1].GetMaximum())
                print "Entries for ", Hname[i][j], "in ", Files[i], ":", Histos[-1].GetEntries()
        elif isinstance(Files[i],list):
            for k in xrange(len(Files[i])):
                F.append(ROOT.TFile(Files[i][k]))
                H=[]; M=[]; T=[]
                for j in xrange(len(Hname[0])):
                    H.append(F[-1].Get(Hname[k][j])); T.append(Hname[k][j])
                    H[-1].Sumw2(); H[-1].Scale(weights[j]); H[-1].Rebin(ReBin) #Apllying weight and rebining for the histo
                    M.append(H[-1].GetMaximum())
                    print "Entries for ", Hname[k][j], "in ", Files[i][k], ":", H[-1].GetEntries()
                Titles.append(T)
                Maxima.append(M)
                Histos.append(H)
        else: print "Error setting files!"

    print len(Histos)
    for i in Histos: print len(i)
    
    for j in xrange(len(Histos[0])):
        CurCanv1 = rootnotes.canvas("MyPlot", (600, 800))
        CurCanv1.cd(1)
        Pad1=ROOT.TPad("pad1","pad1",0,0,1,1)
        Pad1.SetBottomMargin(0.16)
        Pad1.SetLeftMargin(0.16)
        Pad1.Draw()
        Pad1.cd()
    
        LEG=ROOT.TLegend(0.55,0.6,0.89,0.89)
        LEG.SetFillColor(0)
        """
        if isinstance(Files[i],str):
            print "Plotting Histo:", i
            if not stats: Histos[i].SetStats(ROOT.kFALSE)
            Width=Histos[i].GetBinWidth(1)
            if not Normalized: Histos[i].SetTitle(";"+XaxisT[i]+" "+Units+";Events/{0:.2f} ".format(Width)+Units)
            else: Histos[i].SetTitle(";"+XaxisT[i]+" "+Units+";A.U.")
            SetAxis(Histos[i],'Y',1.45,0.05,0.007,0.05,510)
            SetCos(Histos[i], cosm[i][0], cosm[i][1], cosm[i][2], cosm[i][3], cosm[i][4], cosm[i][5])
            if len(YRange)==2: 
                Histos[i].GetYaxis().SetRangeUser(YRange[0],YRange[1])
            LEG.AddEntry(Histos[i], leg[i], "l")
            if not Normalized: 
                if len(YRange)!=2: Histos[i].SetMaximum(max(Maxima)*1.05)
                Histos[i].Draw("hist")
            else:
                Histos[i].DrawNormalized("hist")
            LEG.Draw()
            if LOG: Pad1.SetLogy(); Pad1.RedrawAxis()
            CurCanv1.SaveAs(PDFFile[:-4]+"_"+Titles[i]+".C")
            if i==0: CurCanv1.Print(PDFFile+"(","Title:"+Titles[i])
            elif i!=0 and i!=(len(Histos)-1): CurCanv1.Print(PDFFile,"Title:"+Titles[i])
            else: CurCanv1.Print(PDFFile+")","Title:"+Titles[i])
            del(Pad1); del(CurCanv1)
            """
        if isinstance(Files[0],list):
            for i in xrange(len(Files[0])):
                print "Plotting Histo:", i, j
                if not stats: Histos[i][j].SetStats(ROOT.kFALSE)
                Width=Histos[i][j].GetBinWidth(1)
                if not Normalized: Histos[i][j].SetTitle(";"+XaxisT[i]+" "+Units+";Events/{0:.2f} ".format(Width)+Units)
                else: Histos[i][j].SetTitle(";"+XaxisT[i]+" "+Units+";A.U.")
                SetAxis(Histos[i][j],'Y',1.45,0.05,0.007,0.05,510)
                SetCos(Histos[i][j], cosm[i][0], cosm[i][1], cosm[i][2], cosm[i][3], cosm[i][4], cosm[i][5])
                if len(YRange)==2: Histos[i][j].GetYaxis().SetRangeUser(YRange[0],YRange[1])
                if len(XRange[j])==2: Histos[i][j].GetXaxis().SetRangeUser(XRange[j][0],XRange[j][1])
                LEG.AddEntry(Histos[i][j], leg[i][j], "l"); LEG.AddEntry(ROOT.TObject(), GetMR(Histos[i][j]), ""); LEG.AddEntry(ROOT.TObject(), GetEWI(Histos[i][j]), "")
                if not Normalized:
                    if len(YRange)!=2: Histos[i][j].SetMaximum(max(Maxima[i])*1.05)
                    if i==0: Histos[i][j].Draw("hist")
                    else: Histos[i][j].Draw("hist same")
                else:
                    if i==0: Histos[i][j].DrawNormalized("hist")
                    else: Histos[i][j].DrawNormalized("hist same")
                LEG.Draw()
                if LOG: Pad1.SetLogy(); Pad1.RedrawAxis()
            #CurCanv1.SaveAs(PDFFile[:-4]+"_"+Titles[i][j]+".C")
            if j==0: CurCanv1.Print(PDFFile+"(","Title:"+Titles[i][j])
            elif j!=0 and j!=(len(Histos[0])-1): CurCanv1.Print(PDFFile,"Title:"+Titles[i][j])
            else: CurCanv1.Print(PDFFile+")","Title:"+Titles[i][j])
            del(Pad1); del(CurCanv1)
        
    for i in F: i.Close()
    del(Histos)#; del(CurCanv1); del(LEG); del(Maxima); del(F)

if __name__=='__main__':
    Base="/home/jruizalv/OutOfDropbox/CutsOptimization/PyScripts/"

    F1=[["GEN_Mass_Widths.root","Tp_Mass_Widths_Decay_From_Matching.root","Reconstructed_Tprime_M_Signal.root"]]
    
    files=[]
    for i in F1: files.append(Base+i)

    Masses=["600","650","700","750","800","850","900","950","1000"]
    GEN=["M5J_600","M5J_650","M5J_700","M5J_750","M5J_800","M5J_850","M5J_900","M5J_900","M5J_1000"]
    Reco=["Reconstructed_Tprime_M_600","Reconstructed_Tprime_M_650","Reconstructed_Tprime_M_700","Reconstructed_Tprime_M_750","Reconstructed_Tprime_M_800","Reconstructed_Tprime_M_850","Reconstructed_Tprime_M_900","Reconstructed_Tprime_M_950","Reconstructed_Tprime_M_1000"]
    HistoName=[GEN,GEN,Reco]
    Rebin=2
    PDF="M_Widths_Signal.pdf"
    weights=[1.0]
    Nor=True
    Uni=""
    XT=["M(T')"]
    ST=False
    
    Cos1=[ROOT.kWhite,0,ROOT.kBlack,2,1,1]
    Cos2=[ROOT.kWhite,0,ROOT.kBlue,2,1,1]
    Cos3=[ROOT.kWhite,0,ROOT.kRed,2,1,1]
    Cosmetics=[Cos1,Cos2,Cos3]
    
    logari=False
    Leg=[["M^{GEN}(T') = 600 GeV/c^2", "M^{GEN}(T') = 650 GeV/c^2", "M^{GEN}(T') = 700 GeV/c^2", "M^{GEN}(T') = 750 GeV/c^2", "M^{GEN}(T') = 800 GeV/c^2", "M^{GEN}(T') = 850 GeV/c^2", "M^{GEN}(T') = 900 GeV/c^2", "M^{GEN}(T') = 950 GeV/c^2", "M^{GEN}(T') = 1000 GeV/c^2"],
         ["M^{PY}(T') = 600 GeV/c^2", "M^{PY}(T') = 650 GeV/c^2", "M^{PY}(T') = 700 GeV/c^2", "M^{PY}(T') = 750 GeV/c^2", "M^{PY}(T') = 800 GeV/c^2", "M^{PY}(T') = 850 GeV/c^2", "M^{PY}(T') = 900 GeV/c^2", "M^{PY}(T') = 950 GeV/c^2", "M^{PY}(T') = 1000 GeV/c^2"],
         ["M^{RECO}(T') = 600 GeV/c^2", "M^{RECO}(T') = 650 GeV/c^2", "M^{RECO}(T') = 700 GeV/c^2", "M^{RECO}(T') = 750 GeV/c^2", "M^{RECO}(T') = 800 GeV/c^2", "M^{RECO}(T') = 850 GeV/c^2", "M^{RECO}(T') = 900 GeV/c^2", "M^{RECO}(T') = 950 GeV/c^2", "M^{RECO}(T') = 1000 GeV/c^2"]]

    yrange=[]
    Xran=[[550,650],[600,700],[650,750],[700,800],[750,850],[800,900],[820,980],[870,1030],[900,1100]]
    
    HistoOverDrawer(files,HistoName,bins,PDF,weights,Nor,Uni,XT,ST,Cosmetics,logari,Leg,yrange,Xran)
