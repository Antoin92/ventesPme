import plotly.express as px
import pandas as pd

# Chargement des données depuis Google Sheets (CSV)
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Calcul du chiffre d'affaires (CA)
données['ventes'] = données['prix'] * données['qte']

# Création du camembert : ventes par produit
figure = px.pie(
    données,
    values='ventes',
    names='produit',
    title="Chiffre d'affaires par produit"
)

# Export en HTML
figure.write_html('ventes-par-produit.html')

print("ventes-par-produit.html généré avec succès !")
