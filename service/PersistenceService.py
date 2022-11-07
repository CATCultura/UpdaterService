from service.Persistence.PersistenceManager import PersistenceManager


class PersistenceService:

    def __init__(self):
        self.repo = PersistenceManager()

    def save(self, data: list) -> None:
        self.repo.save(data)
