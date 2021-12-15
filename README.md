# integral-ibis-isgri-le-response

|||
|:--:|:--:|
|see also| [Doc on ISGRI charge loss model](https://www.overleaf.com/read/ntmxzrhqbjfp)|
|see also| [note on low-energy response through OSA versions](https://redmine.astro.unige.ch/projects/isgri-calibration/wiki/Low_energy_response_of_ISGRI) |

OSA11 charge loss model is fitted to lines at ~60 keV and 511 keV.
Trivial extrapolation of the evolution to 20 keV would lead to clear mismatch with ground calibration lines (applicable early mission) and cross-calibration obsevations (applicable late mission).

At ~22 keV there is a Cd line complex ([see](https://xdb.lbl.gov/Section1/Table_1-2.pdf)), but it's hard to use it due to several effects:
* low energy cut-off by pixel threshold. This effect appears as shift to high energy
* energy resolution. Since since the broadened line is cutoff at low energy, it unequally broadens to high energy, learing

Charge loss model, in principle, contains prescription to how low-energy part evolves.
