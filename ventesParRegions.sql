SELECT 
	region, 
	SUM(prix * qte) AS ventesParRegion
FROM ventes
GROUP BY region;