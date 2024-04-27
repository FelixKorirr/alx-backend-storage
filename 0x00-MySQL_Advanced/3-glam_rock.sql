-- Lists all bands with glam rock as their main style
SELECT band_name, (COALESCE(split, '2020') - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC
