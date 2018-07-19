#!/usr/bin/env python
# Tai Sakuma <tai.sakuma@gmail.com>
import alphatwirl
from qtwirl import qtwirl

##__________________________________________________________________||
# to suppress ROOT warnings like
# "TClass::Init:0: RuntimeWarning: no dictionary for class ..."
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

##__________________________________________________________________||
input_files = [
    '/Users/sakuma/work/cms/c180306_sample_nanoaod/store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/445F90F0-DE12-E811-9889-00259021A0E2.root',
    '/Users/sakuma/work/cms/c180306_sample_nanoaod/store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/40898EE0-DE12-E811-BE6D-00226406A18A.root',
]

RoundLog = alphatwirl.binning.RoundLog

reader_cfg = dict(
    summarizer=dict(
        keyAttrNames=('Jet_pt', ),
        binnings=(RoundLog(0.1, 100), ),
        keyOutColumnNames=('jet_pt', )
    )
)

results = qtwirl(
    file=input_files,
    reader_cfg=reader_cfg,
    process=8,
    max_events_per_process=50000
)

print str(results)
expected = """
[[         jet_pt      n   nvar
0     15.848932      3      3
1     19.952623     12     12
2     25.118864     74     74
3     31.622777    645    645
4     39.810717   3463   3463
5     50.118723  14656  14656
6     63.095734  36508  36508
7     79.432823  54088  54088
8    100.000000  53242  53242
9    125.892541  39633  39633
10   158.489319  24000  24000
11   199.526231  12620  12620
12   251.188643   6061   6061
13   316.227766   2880   2880
14   398.107171   1371   1371
15   501.187234    642    642
16   630.957344    234    234
17   794.328235     84     84
18  1000.000000     26     26
19  1258.925412      6      6
20  1584.893192      2      2
21  1995.262315      0      0]]
"""[1:-1]
import difflib
diff = difflib.unified_diff(expected, str(results))
print expected == str(results)
print '\n'.join(list(diff))

##__________________________________________________________________||
