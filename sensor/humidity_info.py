from house_info import HouseInfo

class HumidityDate(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec)*100)
        return recs