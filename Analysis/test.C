void getrandomh() {
	TH1F *source = new TH1F("source","source hist",100,-3,3);
	source->FillRandom("gaus",100000);
	TH1F *final = new TH1F("final","final hist",100,-3,3);

	// continued...

	for (Int_t i=0;i<10000;i++) {
		final->Fill(source->GetRandom());
	}
	TCanvas *c1 = new TCanvas("c1","c1",800,1000);
	c1->Divide(1,2);
	c1->cd(1);
	source->Draw();
	c1->cd(2);
	final->Draw();
	c1->cd();
}

void test2() {
	TH2D* h2 = new TH2D("h","histogram",100,-1,1, 100,0,1);
	double x, y, tmp, deepness=0.02;
	for(int i=0; i<1e6; i++) {
		x = gRandom->Gaus(0,1);
		tmp = gRandom->Landau();
		y = x*x + tmp;
		h2->Fill(x,y);
	}
	h2->Sumw2();
	h2->SetStats(kTRUE);

	TCanvas * ok = new TCanvas("ok","OK",10,10);
	ok->cd();
	h2->Draw();
	return ;
}

void test1() {
	TH1D* h1 = new TH1D("h1", "one-dimentional histogram", 100,-2,2);
	for (int i=0; i<1e5; i++) {
		h1->Fill(gRandom->Gaus(0,.5),i/1e5);
	}
	h1->Sumw2();

	TCanvas* ok = new TCanvas("ok","ok");
	h1->Draw("h* B");
}

void graph_sedlo() {
	TGraph2D* g = new TGraph2D();
	g->SetTitle("Hyperbolic paraboloid");
	Int_t n = 100, m = 100;
	Double_t Beg=0, End=2*3.1416, times=1;
	for (Int_t i=0; i<n; i++) 
	for (Int_t j=0; j<m; j++) {
		g->SetPoint(i*m + j,\
			j*sin(Beg + (End-Beg)*times*i/n),\
			j*cos(Beg + (End-Beg)*times*i/n),\
			j*j*cos(2*(Beg + (End-Beg)*times*i/n)));
	}

	TCanvas* end = new TCanvas("end","end");
	g->SetLineColor(kRed);
	g->SetLineWidth(3);
	g->Draw("surfz");
}

void graph_ord() {
	TGraph* g = new TGraph();
	g->SetTitle("Example graph");
	Int_t n = 1000;
	Double_t beg=0, end=2*3.1416, times=1;
	for (Int_t i=0; i<=n; i++) {
		g->SetPoint(i, sin(beg+(end-beg)*times*i/n), cos(beg+(end-beg)*times*i/n));
	}

	TCanvas* End = new TCanvas("End","End");
	g->SetMarkerStyle(kFullDotSmall);
	g->Draw("ACP"); 
}

void graph_polar() {
	Int_t n = 1000;
	Double_t beg=0, end=2*3.1416, times=1;
	Double_t r[n], phi[n], d_r[n], d_phi[n];
	for (Int_t i=0; i<n; i++) {
		phi[i] = beg+(end-beg)*times*i/n;
		r[i] = 1;
		d_r[i] = 0;
		d_phi[i] = 0;
	}

	TGraphPolar* g = new TGraphPolar(n, phi, r, d_phi, d_r);
	g->SetTitle("This is an example");
	TCanvas* End = new TCanvas("End","This is a title");
	g->SetLineColor(2);
	g->SetLineWidth(2);
	g->Draw("AOC");

}

void graph_qq() {
	Int_t nx = 1e4, ny = 1e4;
	Double_t x[nx], y[ny];
	for (int i=0; i<nx; i++)
		x[i] = gRandom->Gaus(-10,10);
	for (int i=0; i<ny; i++)
		y[i] = gRandom->Poisson(20);
	
	TGraphQQ* g = new TGraphQQ(nx, x, ny, y);
	TCanvas* c = new TCanvas("End", "QQ example");
	c->SetGrid();
	g->SetMarkerStyle(kDot);
	g->Draw("AP");
}

void graph_multi() {
	Int_t n = 1000;
	Double_t beg=0, end=2*3.1416, times=1;
	Double_t r[n], phi[n], d_r[n], d_phi[n], x, y;
	for (Int_t i=0; i<n; i++) {
		phi[i] = beg+(end-beg)*times*i/(n-1);
		r[i] = 1.1;
		d_r[i] = 0.5;
		d_phi[i] = 0.5;
	}
	TGraphErrors* g1 = new TGraphErrors(n, phi, r, d_phi, d_r);
	g1->SetTitle("This is an example polar graph");
	g1->SetLineColor(kRed);
	g1->SetLineWidth(2);

	TGraph* g2 = new TGraph();
	g2->SetTitle("This is an example ordinary graph");
	for (Int_t i=0; i<n; i++) {
		x = cos(phi[i]);
		y = cos(phi[i]);
		g2->SetPoint(i, x, y);
	}
	g2->SetLineColor(kBlue);
	g2->SetLineWidth(1);

	TMultiGraph* mg = new TMultiGraph();
	mg->Add(g1);
	mg->Add(g2);

	TCanvas* End = new TCanvas("End","This is a title");
	mg->Draw("AC");
}

void hist_forfit() {
	Int_t n = 1000;
	TH1* h = new TH1F("h", "histogram", n, -.1, 100);
	for (Int_t i=0; i<n; i++)
		h->Fill(gRandom->Poisson(10));

	TCanvas* c = new TCanvas("c", "Canvas");
	h->Draw("");
}

void hist_fit() {
	TF1* f = new TF1("f","[0]*([1]+x)", 0, 1);
	f->SetParNames("factor", "translation");
	f->SetParLimits(1, -1, 1);
	TH1F* h = new TH1F("h", "line", 100, 0, 1);
	for(int i=0; i<10; i++)
		for(int j=0; j<i; j++)
			h->Fill(0.1*i);
	
	TCanvas* c = new TCanvas("c", "Canvas");
	h->Fit(f, "wmf", NULL, 0, 1);
	//h->Draw();
}

void graph_fit() {
	TF1* f = new TF1("f", "[0]*([1]+x)", 0, 1);
	f->SetParNames("factor", "shift");
	TGraph* g = new TGraph();
	g->SetTitle("Linear graph. Fitting test");
	for(int i=0; i<=10; i++)
		g->SetPoint(i, 0.1*i, 0.1*i);
	g->SetPoint(10, 1, 1.1);
	
	TCanvas* c = new TCanvas("c", "Canvas");
	g->Draw();
	g->Fit(f, "mrsw", "ab", 0, 1);
}

void gaus_fit() {
	TH1D* h = new TH1D("h", "A histogram for fitting", 500, -10, 10);
	for(int i=0; i<1e6; i++) 
		h->Fill(gRandom->Gaus(.1, 30));
	
	//TCanvas* c = new TCanvas("c", "Canvas");
	gStyle->SetOptFit(1111);
	h->Fit("gaus", "0L", "", -10, 10);
}

void hist_fit_new() {
	TH1* h = new TH1D("h", "A sample histogram", 100, -10, 10);
	for (int i=0; i<1e6; i++) 
		h->Fill(gRandom->Gaus(0,1));
	
	h->Fit("gaus");
}

Double_t func_gaus3(Double_t* x, Double_t* p) {
	if (x[0]>0)
		return p[0]*TMath::Exp(-(x[0]-p[1])*(x[0]-p[1])/2/p[2]/p[2]) + \
		p[3]*TMath::Exp(-(x[0]-p[4])*(x[0]-p[4])/2/p[5]/p[5]);
	else
		return p[6]*TMath::Exp(-(x[0]-p[7])*(x[0]-p[7])/2/p[8]/p[8]);
}

void fit_two1() {
	TH1* h = new TH1D("h","hist", 100, -10, 10);
	for(int i=0; i<1e6; i++)
		h->Fill(gRandom->Gaus(0,5));
	for(int i=0; i<0.5*1e6; i++)
		h->Fill(gRandom->Gaus(0,5) + gRandom->Poisson(7));

	TF1* f0 = new TF1("f0", func_gaus3, -10, 10, 9);

	f0->SetParNames("Const", "Mean", "Sigma", "+const", "+mean", "+sigma", "-const", "-mean", "-sigma");
	f0->SetParLimits(0,0, 1e10);
	f0->SetParLimits(3,0, 1e10);
	f0->SetParLimits(6,0, 1e10);
	f0->SetParLimits(1,-10, 10);
	f0->SetParLimits(4,-10, 10);
	f0->SetParLimits(7,-10, 10);
	f0->SetParLimits(2,0.001,10);
	f0->SetParLimits(5,0.001,10);
	f0->SetParLimits(8,0.001,10);
	
	h->Fit("f0");
}

Double_t func_two2(Double_t* x, Double_t* p) {
	int a = x[0];
	if (x[0]>0 && x[0] <= a+20.1/100)
		return p[0]/TMath::Sqrt(2*3.1415926)/p[2]*TMath::Exp(-(x[0]-p[1])*(x[0]-p[1])/2/p[2]/p[2]) + \
		p[3]*TMath::Power(p[4], x[0])/ROOT::Math::tgamma(x[0]+1)*TMath::Exp(-p[4]);
	else 
		return p[0]/TMath::Sqrt(2*3.1415926)/p[2]*TMath::Exp(-(x[0]-p[1])*(x[0]-p[1])/2/p[2]/p[2]);
}

void fit_two2() {
	double NG = 1e6, NP = 1e6;
	TH1* h = new TH1D("h","hist", 100, -10, 10);
	for(int i=0; i<NG; i++)
		h->Fill(gRandom->Gaus(0,5));
	for(int i=0; i<NP; i++)
		h->Fill(gRandom->Poisson(7));
	
	TF1* f = new TF1("f", func_two2, -10, 10, 5);

	f->SetParNames("GausEv", "Mean", "Sigma", "PoissEv", "Lambda");
	f->SetParameters(10, 10, 10, 10, 10);

	//ROOT::Math::MinimizerOptions::SetDefaultMinimizer("Minuit2");
	h->Fit(f);
}

double func_poisson(double* x, double* p) {
	return p[0]*TMath::Power(p[1], x[0])/ROOT::Math::tgamma(x[0]+1)*TMath::Exp(-p[1]);
}

void fit_poisson() {
	TH1* h = new TH1D("h", "Histogram", 100, 0, 10);
	for(int i=0; i<1e6; i++)
		h->Fill(gRandom->Poisson(4));
	TF1* f = new TF1("f", func_poisson, 0, 10, 2);
	f->SetParNames("Const", "Lambda");
	f->SetParLimits(0, 0, 1e10);
	f->SetParLimits(1, 0.001, 100);
	f->SetParameters(1e4, 10);
	h->Fit("gaus", "I");
}

/*void fit_class() {
	ROOT::Fit::DataOptions opt;
	ROOT::Fit::DataRange range(-10, 10);
	ROOT::Fit::BinData data(opt, range);

	TH1* h = new TH1D("h", "hist", 1000, -10, 10);
	for(int i=0; i<1e6; i++)
		h->Fill(gRandom->Gaus(0,5));
	for(int i=0; i<1e6; i++)
		h->Fill(gRandom->Gaus(3, 1));
	ROOT::Fit::FillData(data, h);

	TF1* f = new TF1("f", "gaus(0)+gaus(3)");
	ROOT::Math::WrappedMultiTF1 fitf(*f, 1);
	ROOT::Fit::Fitter fitter; 
	fitter.SetFunction(fitf, false);
	fitter.Fit(data);
	ROOT::Fit::FitResult result = fitter.Result();
	result.Print(std::cout, false);
	//That does not work, library troubles
}*/

Double_t func_gaus(Double_t* x, Double_t* p) {
	return p[0]/TMath::Sqrt(2*3.1415926)/p[2]*TMath::Exp(-(x[0]-p[1])*(x[0]-p[1])/2/p[2]/p[2]);
}

void fit_gaus() {
	TH1* h = new TH1D("h", "hist", 1000, -1, 10);
	for(int i=0; i<1e6; i++)
		h->Fill(gRandom->Gaus(1, 8));
	TF1* f = new TF1("f", func_gaus, -10, 10, 3);
	f->SetParNames("Events", "Mean", "Sigma");
	f->SetParameters(1e6, 1, 8);
	h->Fit(f);
}

void plot_rho() {
	double r, rho;
	const double rmax=5, N=1e3;
	const double x1s=2.0, x1p=4.0/3, x2s=1.0/12;
	TGraph* g1s = new TGraph();
	g1s->SetTitle("1s"); g1s->SetLineColor(kBlack);
	TGraph* g1p = new TGraph();
	g1p->SetTitle("1p"); g1p->SetLineColor(kBlue);
	TGraph* g2s = new TGraph();
	g2s->SetTitle("2s"); g2s->SetLineColor(kRed);
	for(int i=0; i<N; i++) {
		r = rmax/N*i;
		rho = r*r*TMath::Exp(-r*r);
		g1s->SetPoint(i, r, rho*x1s);
		rho = r*r*r*r*TMath::Exp(-r*r);
		g1p->SetPoint(i, r, rho*x1p);
		rho = r*r*(4*r*r-6)*(4*r*r-6)*TMath::Exp(-r*r);
		g2s->SetPoint(i, r, rho*x2s);
	}
	
	TCanvas* c = new TCanvas();
	TMultiGraph* mg = new TMultiGraph();
	mg->SetTitle("Probability density for a first few states.");
	mg->Add(g1s);
	mg->Add(g1p);
	mg->Add(g2s);
	mg->Draw("acp");
	c->BuildLegend();
}

class MyTClass: public TObject {
private:
	double Myf;
public:
	MyTClass() {Myf = 3.1416;}
	~MyTClass() {;}
};

void test() {
	plot_rho();
}
