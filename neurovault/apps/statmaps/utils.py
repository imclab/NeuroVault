import os
import tempfile
import subprocess
def split_filename(fname):
    """Split a filename into parts: path, base filename and extension.

    Parameters
    ----------
    fname : str
        file or path name

    Returns
    -------
    pth : str
        base path from fname
    fname : str
        filename from fname, without extension
    ext : str
        file extension from fname

    Examples
    --------
    >>> from nipype.utils.filemanip import split_filename
    >>> pth, fname, ext = split_filename('/home/data/subject.nii.gz')
    >>> pth
    '/home/data'

    >>> fname
    'subject'

    >>> ext
    '.nii.gz'

    """

    special_extensions = [".nii.gz", ".tar.gz"]

    if fname and fname.endswith(os.path.sep):
        fname = fname[:-1]

    pth, fname = os.path.split(fname)

    ext = None
    for special_ext in special_extensions:
        ext_len = len(special_ext)
        if (len(fname) > ext_len) and \
                (fname[-ext_len:].lower() == special_ext.lower()):
            ext = fname[-ext_len:]
            fname = fname[:-ext_len]
            break
    if not ext:
        fname, ext = os.path.splitext(fname)

    return pth, fname, ext

    
def generate_pycortex_dir(nifti_file, output_dir):
    import cortex
    outfilename = tempfile.mktemp(".nii")
    try:
        exit_code = subprocess.call(["mri_vol2vol", 
                         "--mov", 
                         nifti_file,
                         "--targ",
                         os.path.join(os.environ['FREESURFER_HOME'], 'subjects', 'fsaverage', 'mri', 'brain.mgz'),
                         "--o",
                         outfilename,
                         "--mni152reg",
                         "--no-save-reg"])
        if exit_code:
            raise RuntimeError("mri_vol2vol exited with status %d"%exit_code)
        dv = cortex.DataView((outfilename, "fsaverage", "identity"))
        cortex.webgl.make_static(output_dir, dv)
    finally:
        if os.path.exists(outfilename):
            os.remove(outfilename)