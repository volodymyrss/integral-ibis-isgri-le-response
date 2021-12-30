import astropy.io.fits as fits
import os
import pandas as pd
from scipy.interpolate import interp1d

import iconfig

print(iconfig.settings.rep_base_prod)

cache={}

def read_nomex_norm(y=200, z=200, ebins=None):
    fn = os.path.join(iconfig.settings.rep_base_prod, "ic/ibis/mod/isgr_effi_mod_0011.fits")    

    e1, e2 = ebins
    
    if (y,z) not in cache:
        nomex = []
        for e in fits.open(fn)[2:-1]:
            nomex.append(dict(
                e1=e.header['E_MIN'],
                e2=e.header['E_MAX'],
                norm=e.data[y,z],
            ))
        nn=pd.DataFrame(nomex)
        cache[(y, z)]=pd.DataFrame()
        cache[(y, z)]['e1'] = e1
        cache[(y, z)]['e2'] = e2
        cache[(y, z)]['norm'] = interp1d((nn.e1 + nn.e2) * 0.5, nn.norm, bounds_error=False)((e1 + e2) * 0.5)

    return cache[(y,z)]
