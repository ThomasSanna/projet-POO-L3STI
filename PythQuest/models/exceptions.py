class InsufficientFundsError(Exception):
    pass

class InventoryFullError(Exception):
    pass

class NoSuchItemError(Exception):
    pass

class QuestAlreadyAcceptedError(Exception):
    pass

class NoActiveQuestError(Exception):
    pass