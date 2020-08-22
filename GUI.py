from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from DataHandling import dataHandle
from sodapy import Socrata
from DataHandling import dataHandle


class ContentNavigationDrawer(BoxLayout):
    pass

class CovidApp(MDApp):
    def build(self):
        return Builder.load_file("widgets.kv")

    def setResult(self):
        # get the client, call on the API
        handler = dataHandle()
        townName = str(self.root.ids.input.text)
        try:
            townVals = handler.getTownInfo(townName)
        except:
            self.root.ids.date.text = 'Date'
            self.root.ids.town.text = 'Town'
            self.root.ids.cases.text = 'Confirmed Cases'
            return None
        results = handler.sendValues(townVals)
        for key in results.keys():
            if key == 'Update Date':
                parts = (results[key]).split('T')
                dateValue = parts[0] + ' ' + parts[1]
                self.root.ids.date.text = str(key + ': ' + '\n' + dateValue)
            elif key == 'Confirmed Cases':
                self.root.ids.cases.text = str(key + ': ' + results[key])
            elif key == 'Case Rate':
                self.root.ids.caserate.text = str(key + ': ' + str(results[key]))
        # Set the title
        self.root.ids.screen_manager.current = "results"
        self.root.ids.townTitle.text = results['Town']


        
if __name__=="__main__":
    CovidApp().run()