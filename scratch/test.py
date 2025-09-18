import tcg_research_desk

from collections import Counter

import pandas as pd
import numpy as np
import holoviews as hv
import panel as pn

import param

pn.extension(
    'tabulator', 
    sizing_mode="stretch_width", 
    throttled=True, 
    js_files={'hover': 'hover.js'},
)
hv.extension('bokeh')

import scipy
import sklearn
import bokeh

print(f"""
{tcg_research_desk.__version__=}
{pd.__version__=}
{np.__version__=}
{hv.__version__=}
{pn.__version__=}
{param.__version__=}
{scipy.__version__=}
{sklearn.__version__=}
{bokeh.__version__=}
""")

pn.pane.Markdown("test").servable()