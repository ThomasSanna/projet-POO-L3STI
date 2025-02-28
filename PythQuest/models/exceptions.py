class InsufficientFundsError(Exception):
    """
    Exception levée lorsqu'il n'y a pas assez de fonds pour effectuer une action.

    Cette exception est utilisée pour indiquer qu'une tentative d'effectuer une action
    nécessitant des fonds a échoué en raison de fonds insuffisants.

    Attributes:
        message (str): Message d'erreur décrivant la situation.
    """
    pass

class InventoryFullError(Exception):
    """
    Exception levée lorsque l'inventaire est plein.

    Cette exception est utilisée pour indiquer qu'une tentative d'ajouter un objet
    à un inventaire plein a été effectuée.

    Attributes:
        message (str): Message d'erreur décrivant la situation.
    """
    pass

class NoSuchItemError(Exception):
    """
    Exception levée lorsqu'un objet n'existe pas dans l'inventaire.
    
    Cette exception est utilisée pour indiquer qu'une tentative d'accéder à un objet
    qui n'existe pas dans l'inventaire a été effectuée.
    
    Attributes:
        message (str): Message d'erreur décrivant la situation.
    """
    pass

class QuestAlreadyAcceptedError(Exception):
    """
    Exception levée lorsque la quête a déjà été acceptée.

    Cette exception est utilisée pour indiquer qu'une tentative d'accepter une quête
    qui a déjà été acceptée a été effectuée.

    Attributes:
        message (str): Message d'erreur décrivant la situation.
    """
    pass

class NoActiveQuestError(Exception):
    """
    Exception levée lorsqu'il n'y a pas de quête active.

    Cette exception est utilisée pour indiquer qu'une tentative d'interagir avec une quête
    alors qu'aucune quête n'est active a été effectuée.

    Attributes:
        message (str): Message d'erreur décrivant la situation.
    """
    pass