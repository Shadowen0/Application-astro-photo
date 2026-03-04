from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import os

class classRenderImage:
    def __init__(self, nom):
        self.nom = nom
        self.fichiers_fits = []
        self.get_bande()

    def get_bande(self):
        for f in os.listdir(self.nom):
            chemin_complet = os.path.join(self.nom, f)
            if f.endswith((".fit", ".fits")) and os.path.isfile(chemin_complet):
                self.fichiers_fits.append(chemin_complet)

    def render(self, couleurs):
        return np.dstack(couleurs)
    
    def affiche(self):
        images = []
        for bande in self.fichiers_fits:
            images.append(fits.getdata(bande))
        
        couleurs = []
        for img in images:
            
            img = np.nan_to_num(img, nan=0.0, posinf=0.0, neginf=0.0)
            
            min_val, max_val = np.percentile(img, [2, 98])
            normalisee = np.clip((img - min_val) / (max_val - min_val), 0, 1)
            couleurs.append(normalisee)

        if len(couleurs) == 2:
            self.image_rgb = np.dstack([couleurs[1], couleurs[0], couleurs[0]])
        else:
            self.image_rgb = self.render(couleurs)

    def affichage_image(self):
        plt.imshow(self.image_rgb, origin='lower')
        plt.title("Image Astro")
        plt.show()

if __name__ == "__main__":
    chemin_dossier = "Images_Astrales/Tarantula"

    render_image = classRenderImage(chemin_dossier)
    render_image.affiche()
    render_image.affichage_image()
