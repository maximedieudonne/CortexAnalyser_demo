from cortexanalyser.core.curvature import compute_curvature
from cortexanalyser.core.voronoi import generate_voronoi


EXPORTED_FUNCTIONS = {
    "compute_curvature": {
        "function": compute_curvature,
        "label": "Calcul de courbure",
        "description": "Courbure moyenne du maillage."
    },
    "generate_voronoi": {
        "function": generate_voronoi,
        "label": "Diagramme de Voronoï",
        "description": "Partitionne la surface par Voronoï."
    }
}