import ROOT as r
import style
import math as m

style.ApplyStyle()

def Fourier(x, v2, v3, v4):
	return 1+v2*m.cos(2*x)+v3*m.cos(3*x)+v4*m.cos(4*x)

colors = {'lowpp': r.kRed, 'lowpPb': r.kBlue, 'highpPb': r.kViolet, 'highpp': r.kOrange-3}
titles = {'lowpp': 'low mul pp', 'highpp': 'high mul pp', 
					'lowpPb': 'low mul pPb', 'highpPb': 'high mul pPb'}
order = ['lowpp', 'highpp', 'lowpPb', 'highpPb']

v_pars = {'lowpp':  [.06, .0078, .014],
					'highpp': [.062, .0138, .0105],
					'lowpPb': [.065, .011, .0096],
					'highpPb':[.08, .026, .014] }
Phis = [0.1*x for x in range(64)]
Phis.append(2*m.pi)

# comment after the first run
canvas = r.TCanvas('c', 'Canvas')
legend = r.TLegend(.71, .77, 1, .96)
g = {}
for case in order:
	g[case] = r.TGraphPolar()
	for i in range(len(Phis)):
		g[case].SetPoint(i, Phis[i], Fourier(Phis[i], *v_pars[case]))
	g[case].SetLineWidth(4)
	g[case].SetLineColor(colors[case])
	g[case].SetMaxPolar()
	legend.AddEntry(g[case], titles[case], 'l')
graph = g[order[3]]
graph.Draw('Aol')
for case in order:
	g[case].Draw('l')
legend.SetTextFont(42)
legend.Draw()
canvas.SetGrid(0,0)
canvas.Update()
p = graph.GetPolargram()
p.SetTextSize(0)
p.SetTwoPi()
p.SetToRadian()
p.SetPolarLabelSize(0)
p.SetRadialLabelSize(0)
p.SetNdivPolar(204)
p.SetNdivRadial(404)
p.SetRangeRadial(0, 1.2)
#p.SetLineWidth(0)
p.SetLineColorAlpha(r.kBlack, .1)
canvas.Print('/tmp/ink/Y-polar.svg')
