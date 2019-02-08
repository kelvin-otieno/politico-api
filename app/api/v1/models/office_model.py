"""Political Office Model"""


class PoliticalOffice():
    """Political Office Class Model"""
    political_offices = []

    id = 0
    office_type = ""
    name = ""

    def __init__(self):
        self.political_offices = [
            {
                'id': 1,
                'type': 'Legislative',
                'name': 'President'
            },
            {
                'id': 2,
                'type': 'Local Government',
                'name': 'Governor'
            },
            {
                'id': 3,
                'type': 'Legislative',
                'name': 'Senator'
            },
            {
                'id': 4,
                'type': 'Local Government',
                'name': 'Women Representative'
            }
        ]

    def create_office(self):
        """method to create a new office"""
        office = {
            'id': len(self.political_offices) + 1,
            'type': self.office_type,
            'name': self.name
        }

        self.political_offices.append(office)
        return dict(status=201, data=self.political_offices)

    def get_offices(self):
        """method to get all offices"""
        if self.political_offices:
            return dict(status=200, data=self.political_offices)
        else:
            return dict(status=404, data={"error": "Not found"})

    def get_office(self, id):
        """method to get a specific office"""
        exists = False

        if self.political_offices:
            for office in self.political_offices:
                if office['id'] == id:
                    exists = True
                    return dict(status=200, data=office)

        if not exists:
            return dict(status=400, data={"error": "Bad Request"})
