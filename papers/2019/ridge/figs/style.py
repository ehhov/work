import ROOT

def CreateStyle():
	tmp = ROOT.TStyle("ATLAS","Atlas style");
	#// use plain black on white colors
	color = 0; 
	tmp.SetFrameFillColor(color);
	tmp.SetCanvasColor(color);
	tmp.SetPadColor(color);
	tmp.SetStatColor(color);
	#//tmp.SetFillColor(color); #// don't use: white fill color for *all* objects

	border = 0;
	tmp.SetCanvasBorderMode(border)
	tmp.SetFrameBorderMode(border)
	tmp.SetPadBorderMode(border)
	bordersz = 0
	tmp.SetCanvasBorderSize(bordersz)
	tmp.SetFrameBorderSize(bordersz)
	tmp.SetLegendBorderSize(bordersz)
	tmp.SetPadBorderSize(bordersz)
	tmp.SetStatBorderSize(bordersz)
	tmp.SetTitleBorderSize(bordersz)

	width_big = 2
	width_small = 1
	tmp.SetFrameLineWidth(width_small)
	tmp.SetHistLineWidth(width_big)

	tmp.SetStripDecimals(ROOT.kFALSE)
	
	#// set the paper & margin sizes
	tmp.SetPaperSize(26,26);

	#// set margin sizes
	tmp.SetPadTopMargin(0.05);
	tmp.SetPadRightMargin(0.05);
	tmp.SetPadBottomMargin(0.15);
	tmp.SetPadLeftMargin(0.15);

	#// set title offsets (for axis label)
	tmp.SetTitleXOffset(1.3);
	tmp.SetTitleYOffset(1.3);

	#// use large fonts
	#//Int_t font=72; #// Helvetica italics
	fonts = {'times': 132, 'times it': 12, 'times bold': 22, 'helvetica': 42, 'helvetica it': 52, 'helvetica bold': 62}
	font = fonts['times']
	tmp.SetTextFont(font)
	tmp.SetLegendFont(font)
	for axis in ['x', 'y', 'z']:
		tmp.SetLabelFont(font, axis);
		tmp.SetTitleFont(font, axis);

	tsize=0.05;
	incf = 1.1
	decf = .9
	tmp.SetTextSize(tsize);
	tmp.SetLegendTextSize(decf*tsize)
	for axis in ['x', 'y', 'z']:
		tmp.SetLabelSize(incf*tsize, axis);
		tmp.SetTitleSize(incf*tsize, axis);

	#// use bold lines and markers
	tmp.SetMarkerStyle(20);
	tmp.SetMarkerSize(1.5);
	tmp.SetHistLineWidth(2);
	tmp.SetLineStyleString(2,"[12 12]");

	# error bars hats
	tmp.SetEndErrorSize(2);

	#// do not display any of the standard histogram decorations
	tmp.SetOptTitle(0);
	#//tmp.SetOptStat(1111);
	tmp.SetOptStat(0);
	#//tmp.SetOptFit(1111);
	tmp.SetOptFit(0);

	#// put tick marks on top and RHS of plots
	tmp.SetPadTickX(1);
	tmp.SetPadTickY(1);

	return tmp;

def ApplyStyle():
	print('Applying ATLAS style settings...')
	this_style = CreateStyle()
	ROOT.gROOT.SetStyle('ATLAS')
	ROOT.gROOT.ForceStyle()
