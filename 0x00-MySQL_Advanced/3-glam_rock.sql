-- Lists all bands with glam rock as their main style
SELECT band_name, coalesce(split, 2020) - formed AS lifespan
from metal_bands
WHERE find_in_set('Glam rock', style)
ORDER BY lifespan DESC
