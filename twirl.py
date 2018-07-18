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

print results

##__________________________________________________________________||
