# tools/curvature.py
import nibabel as nb
import numpy as np
import utils.texture as stex
import utils.parser as parser
from pathlib import Path

def compute_voronoi(mesh_path, output_path):
    # Exemple fictif 
    g = nb.load(mesh_path)
    coords = g.darrays[0].data
    n_vertices = coords.shape[0]

    voronoi = np.random.randn(n_vertices) * 0.05  # simulateur temporaire
    
    # Save
    parser.write_texture(stex.TextureND(darray=voronoi), output_path)
    
    return output_path