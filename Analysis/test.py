import ostap.fitting.models as Models

x = ROOT.RooRealVar('x', '#it{x}', 0, 1)
dataset = ROOT.RooDataSet('dataset', 'Sample dataset', ROOT.RooArgSet(x))

for i in range(10000):
	tmp = ROOT.gRandom.Gaus(.5, .1)
	if tmp>0 and tmp<1: 
		x.value = tmp
		dataset.add(ROOT.RooArgSet(x))
for i in range(1000000):
	tmp = ROOT.gRandom.Gaus(1, 1)
	if tmp>0 and tmp<1: 
		x.value = tmp
		dataset.add(ROOT.RooArgSet(x))

signal = Models.Gauss_pdf('Signal', x, #
  mean = ROOT.RooRealVar('mean', '', 0, 1), #
	sigma = ROOT.RooRealVar('sigma', '', .01, 10) #
)
background = Models.PolyPos_pdf('Background', x, power = 2)
model = Models.Fit1D( #
  signal = signal, #
	background = background #
)

result, frame = model.fitTo(dataset, draw = True)
print 'The fit is done, now making these Toys'

import ostap.fitting.toys as Toys 

result, stats = Toys.make_toys(model, 1000, [x], {'nEvents': 5000})

h = {}; c = {}
for i in result:
	h[i] = ROOT.TH1D('h_'+i, 'The distribution of the variable '+i, 100, stats[i].min(), stats[i].max())
	for j in result[i]:
		h[i].Fill(j.value(), 1/j.error())
for i in h:
	c[i] = ROOT.TCanvas('c_'+i, 'The Canvas for the variable '+i, 500, 500)
	c[i].cd()
	h[i].Draw()


