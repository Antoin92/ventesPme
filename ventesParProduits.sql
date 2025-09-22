SELECT 
	produit, 
    SUM(prix * qte) AS ventesParProduit
FROM ventes
GROUP BY produit;

