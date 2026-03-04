from Query import classQuery
from RenderImage import classRenderImage

if __name__ == "__main__":
    
    continu = True 
    while continu :
        
        chemin_dossier = "Images_Astrales/"
        
        if str(input("Voulez vous entrer un nom d'astre ? (sinon ce sera une position astrale) ")) == "oui":
            zone = str(input("Votre astre : "))
            
            angle = str(input("Entrez un angle de prise de vue (ex : '5.0') : ")) + " deg"

            query = classQuery(zone,angle)
            
            query.download_images()
            
            chemin_dossier = chemin_dossier + zone
            
        else :
    
            pos_x = str(input("Entrez une position x : "))
            pos_y = str(input("entrez une position y : "))
            position_astrale = pos_x+ " " +pos_y
            
            angle = str(input("Entrez un angle de prise de vue (ex : '5.0') : ")) + " deg"

            query = classQuery(position_astrale,angle)
            
            query.download_images()
            
            chemin_dossier = chemin_dossier + pos_x + "_" + pos_y
            
        render_image = classRenderImage(chemin_dossier)
        render_image.affiche()
        render_image.affichage_image()
    
        if str(input("Voulez vous continuer ? (oui/non) "))=="non":
            continu = False
            
        print()
        print("-"*20)
        print()
            
    

    
 
    
    

    