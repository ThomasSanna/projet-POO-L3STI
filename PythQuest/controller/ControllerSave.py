from models.Combattant import Combattant
from models.Arme import Arme
from view.ViewSave import ViewSave

class ControllerSave:
  
  def __init__(self, combattant: Combattant):
    """
    Initialise le contrôleur de sauvegarde avec un combattant.
    
    :param combattant: Instance de la classe Combattant à sauvegarder.
    """
    self.view = ViewSave()
    self.combattant = combattant
    
  def saveAll(self):
    """
    Enregistre toutes les informations du combattant dans la base de données.
    
    :param combattant: Dictionnaire contenant les informations du combattant
    """
    try:
      self.combattant.save()
      for arme in Arme.getAllArmes():
        if self.combattant.armeDansInventaire(arme) or arme == self.combattant.getArmeEquipee():
          arme.save(self.combattant)
    except Exception as e:
      self.view.putErrorBox("Erreur de sauvegarde", f"Une erreur est survenue lors de la sauvegarde : {str(e)}")
  
  def saveCombattant(self):
    """
    Enregistre les informations d'un combattant dans la base de données.
    
    :param combattant: Dictionnaire contenant les informations du combattant
    """
    try:
      self.combattant.save()
    except Exception as e:
      raise e