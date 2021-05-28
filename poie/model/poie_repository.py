import poie.model.results


class PoieDao:

    def __init__(self, database, session):
        self.database = database
        self.session = session

    def save(self, wave_file):
        result = poie.model.results.Results(str(wave_file))
        self.session.add(result)
        self.session.commit()