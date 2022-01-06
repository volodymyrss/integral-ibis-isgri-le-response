
import numpy as np
def produce_e_morph(t1, t2):
    if (t2 - t1) > 60:
        raise RuntimeError('too long to patch rmf!')

    from astropy.time import Time

    # need to read from IC, per spectrum, in oda/osa
    # https://gitlab.astro.unige.ch/integral/cc-workflows/cc-global-summary
    def offset_approximation(ijd):
        z1 = 2000
        z2 = 6000
        p1 = -1.5
        p2 = -4
        return (z1 - ijd) * (z2 + (z2-z1) - ijd) / (z1-z2)**2 * (-p2+p1) + p1


    def e_morph_family(E, lebias=4):
        off60 = 0
        E0 = 50
        s = 4 + lebias
        #r = E - E / ( 1 + (E/18)**2 )
        r = E - (lebias )/(1 + np.exp(((E)/E0)**s))*(1 + np.exp(((27)/E0)**s))  + off60
        return r

    offset_approx = -offset_approximation((t1+t2)/2.)
    e_morph = lambda en: e_morph_family(en, offset_approx)

    return e_morph, dict(offset_approx=offset_approx)