# work

My work and studies related files that I don't want to lose.

## ROOT

To get a working PyROOT installation, you have to place python2 at `/usr/bin/python` and `/usr/bin/env python`. You can also use the script `other/funcs.sh` to force the use of `/bin/*python2` instead of `python`. 

You can find the latest release at https://root.cern.ch/.
Root at GitHub: https://github.com/root-project/root. Be careful as it can contain critical changes compared to older verified versions. 

Root documentation https://root.cern.ch/documentation 

- Reference guide is a full discription of all classes and other. You can download it  and read offline (~3.6 GB). https://root.cern.ch/guides/reference-guide
- User guide is a small explanation of root concepts. https://root.cern.ch/root/htmldoc/guides/users-guide/ROOTUsersGuide.html

## Ostap

[Ostap](https://github.com/OstapHEP/ostap) requires a ROOT installation with the following options: 

- `Core`, `GenVector`, `Hist`, `MathCore`, `MathMore`, `Matrix`, `Minuit2`, `PyROOT`, `RIO`, `RooFit`, `RooFitCore`, `Smatrix`, `TMVA`, `Thread`, `Tree`, `TreePlayer`
- Carefully check`MathMore`, `Minuit2`, `PyROOT`; `CMAKE_CXX_STANDARD 14+`

Supplementary Python modules include 

- future, numpy, scipy
- terminaltables
- pathos, dill, multiprocess, ppt

Ostap worked well with ROOT version 6.18/04.

## Step-by-step ROOT, PyROOT, and Ostap installation

Download the latest stable ROOT release at https://root.cern.ch/releases 
```bash 
tar xzf root*.tar.gz && cd root
~/work/other/funcs.sh # and run all the *py_to_2 functions 
mkdir ../rootbuild && cd ../rootbuild 
ccmake ../root # check all Ostap dependencies listed above 
               # and don't forget the /opt/root prefix
make -j8 # now wait... 
su # and make install 
```
Download and install Ostap
```bash
git clone https://github.com/OstapHEP/ostap.git && cd ostap 
~/work/other/funcs.sh # and run all the *py_to_2 functions 
mkdir ../ostapbuild && cd ../ostapbuild
ccmake ../ostap # set the /opt/ostap prefix
make -j8 
su # and make install 
```

## CVMFS

`source /cvmfs/lhcb.cern.ch/group_login.sh`
`lb-run Bender/latest ostap`
`lb-run root root`

## Programming guides

- Python: https://www.w3schools.com/python/ 
- Bash: https://bash.cyberciti.biz/guide/Main_Page 
- Advanced Bash https://tldp.org/LDP/abs/html/
- Analysis scripting: https://lhcb.github.io/analysis-essentials/  




# Notes 
## Font size conversion between typefaces
This section helps you convert strange requirements in some places to LaTeX acceptable format. 

| Times New Roman | Computer Modern Roman |
|-----------------|-----------------------|
| 12 pt, 1.5 spacing | {12}{17} with onehalfspace |
|                    | {12}{20.7} without any packages |
| 14 pt, 1.5 spacing | {14}{20} with onehalfspace |
|                    | {14}{24.2} without any packages |

Newer and more adequate solution: documentclass[a4paper, 14pt]{extarticle}, linespread{1.43}. But it doesn't affect math script size fonts, so good luck typing math!
