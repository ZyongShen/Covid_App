from sodapy import Socrata

class dataHandle():

    def __init__(self):
        client = Socrata("data.ct.gov", None)
        self.results = client.get("28fr-iqnx", limit=2000)

    def getTownInfo(self, town):
        results = self.results
        townData = []
        for i in range(len(results)):
            if str(results[i]['town']).lower() == town.lower():
                townData.append(results[i])
        return townData[0]

    def sendValues(self, townData):
        results = {
            'Update Date': None,
            'Town': None,
            'Confirmed Cases': None,
            'Case Rate': None
        }
        results['Update Date'] = townData['lastupdatedate']
        results['Town'] = townData['town']
        results['Confirmed Cases'] = townData['townconfirmedcases']
        results['Case Rate'] = float(townData['towncaserate'])/100000
        return results

handler = dataHandle()
results = handler.getTownInfo('Wethersfield')
print(results)


    

