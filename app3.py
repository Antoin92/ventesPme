import plotly.express as px
import pandas as pd

# Chargement des données depuis Google Sheets (CSV)
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Calcul du chiffre d'affaires
données['ventes'] = données['prix'] * données['qte']

# Agréger les ventes par produit
ventes_par_produit = données.groupby('produit', as_index=False)['ventes'].sum()

# Créer un graphique en barres
figure = px.bar(
    ventes_par_produit,
    x='produit',
    y='ventes',
    title="Chiffre d'affaires par produit",
    text='ventes',
    labels={'produit': 'Produit', 'ventes': 'Chiffre d\'affaires (€)'}
)

# Enregistrer le graphique dans un fichier HTML
figure.write_html('ventes-par-produit.html')

print("ventes-par-produit.html généré avec succès !")
