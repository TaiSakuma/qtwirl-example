#!/usr/bin/env python
# Tai Sakuma <tai.sakuma@gmail.com>
from __future__ import print_function
import logging
import socket

import alphatwirl
from qtwirl import qtwirl

##__________________________________________________________________||
# to suppress ROOT warnings like
# "TClass::Init:0: RuntimeWarning: no dictionary for class ..."
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

##__________________________________________________________________||
def configure_logger(level='INFO'):

    level = logging.getLevelName(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    names = ['qtwirl', 'alphatwirl']
    for n in names:
        logger = logging.getLogger(n)
        logger.setLevel(level)
        logger.handlers[:] = [ ]
        logger.addHandler(handler)
        logger.propagate = False # log shown twice in multiprocessing if True

configure_logger()

##__________________________________________________________________||
pfn_top = '/Users/sakuma/work/cms/c180306_sample_nanoaod/'
hostname = socket.gethostname()
if 'soolin' in hostname:
    pfn_top = '/hdfs/dpm/phy.bris.ac.uk/home/cms/'

##__________________________________________________________________||
input_lfns = [
    'store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/445F90F0-DE12-E811-9889-00259021A0E2.root',
    'store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/40898EE0-DE12-E811-BE6D-00226406A18A.root',
]

input_files = [pfn_top + p for p in input_lfns]

RoundLog = alphatwirl.binning.RoundLog

reader_cfg = [dict(
    key_name=('Jet_pt', ),
    key_binning=(RoundLog(0.1, 100), ),
    key_out_name=('jet_pt', )
)]

results = qtwirl(
    data=input_files,
    reader_cfg=reader_cfg,
    tree_name='Events',
    # parallel_mode='htcondor',
    dispatcher_options=dict(
        job_desc_dict={
            '+SingularityImage': '"/cvmfs/singularity.opensciencegrid.org/kreczko/workernode:centos6"',
        }),
    process=16, quiet=False,
    max_events_per_process=25000
)

print(str(results))
expected = """
[         jet_pt      n   nvar
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
21  1995.262315      0      0]
"""[1:-1]
import difflib
diff = difflib.unified_diff(expected, str(results))
print(expected == str(results))
print('\n'.join(list(diff)))

##__________________________________________________________________||
