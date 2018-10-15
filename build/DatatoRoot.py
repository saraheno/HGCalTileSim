import sys, string, os
from ROOT import TFile, TNtuple
ifn = os.path.expandvars("FinalShallow.csv")
ofn = 'FinalShallow.root'
print ('opening file'), ifn, '...'
infile = open( ifn, 'r' )
lines  = infile.read().splitlines()
title  = "Mean Detected Photons Per Muon"
labels = lines[0].split(",")
print ('writing file'), ofn, '...'
outfile = TFile( ofn, 'RECREATE', 'ROOT file with an NTuple' )
ntuple  = TNtuple( 'ntuple', title, string.join( labels, ':') )
for line in lines[1:]:
    words = line.split(",")
    row = map( float, words )
    apply( ntuple.Fill, row )
outfile.Write()
print(labels)
print ('done')
#TH2F* h3 = new TH2F("Ndetect", "Mean Detected Photons Per Muon", 20, -2 , 2, 20, -2, 2) use this to define a 2d histogram with 20 bins in x and y axis (range -6 to 6)
#ntuple->Draw("x:y>>Ndetect","det","SURF3") use this to fill the histogram using the ntuple created in this .py, using 'avg' as n for the histogram, SURF3 is a draw option
#make sure in the fill function above, the arguments (x,y,avg in this case) match the printed 'labels', otherwise the histogram will not fill correctly
