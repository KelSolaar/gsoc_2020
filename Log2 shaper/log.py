#
"""
Log2 Shaper Implementation
==========================

Defines the *Log2 shaper* log encodings:

-   :func:`colour.models.log_encoding_Log2`
-   :func:`colour.models.log_decoding_Log2`

References
----------

"""

import numpy as np
from colour.utilities import from_range_1, to_domain_1

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['log_encoding_Log2', 'log_decoding_Log2']


def log_encoding_Log2(lin, middle_grey=0.18, min_exposure=0.18*2**-6.5, max_exposure=0.18*2**6.5):
    """
    Defines the *Log2 shaper* log encoding function. 

    Parameters
    ----------
    lin : numeric or array_like
          Linear data to undergo encoding. 
    middle_grey : numeric, optional
                  'Middle Grey' exposure value.
    min_exposure : numeric, optional
                   Minimum exposure level.
    max_exposure : numeric, optional
                   Maximum exposure level.

    Returns
    -------
    numeric or ndarray
        Non-linear *Log2 shaper* encoded data

    Notes
    -----

    References
    ----------

    Examples
    --------
    Linear numeric input gets encoded as follows:

    >>> log_encoding_Log2(18)
    0.40773288970434662

    Linear array-like input gets encoded as follows:

    >>> log_encoding_Log2(np.linspace(1, 2, 3))
    array([ 0.15174832,  0.18765817,  0.21313661])
    """

    lin = to_domain_1(lin)

    lg2 = np.log2(lin / middle_grey)
    log_norm = (lg2 - min_exposure) / (max_exposure - min_exposure)
    
    return from_range_1(log_norm)


def log_decoding_Log2(log_norm, middle_grey=0.18, min_exposure=0.18*2**-6.5, max_exposure=0.18*2**6.5):
    """
    Defines the *Log2 shaper* log decoding function. 

    Parameters
    ----------
    log_norm : numeric or array_like
               Logarithmic data to undergo decoding.
    middle_grey : numeric, optional
                  'Middle Grey' exposure value.
    min_exposure : numeric, optional
                   Minimum exposure level.
    max_exposure : numeric, optional
                   Maximum exposure level.

    Returns
    -------
    numeric or ndarray
        Linear *Log2 shaper* decoded data

    Notes
    -----

    References
    ----------

    Examples
    --------
    Logarithmic input gets decoded as follows:

    >>> log_decoding_Log2(0.40773288970434662)
    17.999999999999993

    Linear array-like input gets encoded as follows:

    >>> log_decoding_Log2(np.linspace(0, 1, 4))
    array([  1.80248299e-01,   7.77032379e+00,   3.34970882e+02,
             1.44402595e+04])
    """

    log_norm = to_domain_1(log_norm)

    lg2 = log_norm * (max_exposure - min_exposure) + min_exposure
    lin = (2 ** lg2) * middle_grey

    return from_range_1(lin)


