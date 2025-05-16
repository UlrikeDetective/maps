callData.py
This file is modular and contains functions for clipping, loading, preprocessing, snapping, and exporting data.

Run this first to generate all the necessary processed and intermediate files for Leipzig (or Berlin, if you switch back).
You can run the whole script or call its functions step by step in a Python shell or notebook.
redundantCode.py
This file contains a full script (with a __main__ block) that essentially repeats the workflow in a more linear, script-style fashion.

You can run this as a standalone script if you want to process everything in one go, or use it for testing/experimentation.
It is somewhat redundant with callData.py but can be used for end-to-end runs or as a template for further development.
Summary:

For modular, reusable processing: use callData.py first.
For a one-shot, script-style run: use redundantCode.py (after ensuring all Leipzig file paths are correct).
You do not need to run both unless you want to compare outputs or test both workflows. If you want a clean, stepwise process, start with callData.py. If you want a single script to do everything, use redundantCode.py.