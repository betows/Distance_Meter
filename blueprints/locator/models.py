import csv 
import requests
from datetime import datetime

class DistanceResult(object):
    
    def __init__(self, lat_orig=None, lng_orig=None, lat_dest=None, lng_dest=None, orig_addresses=None, dest_addresses=None, distance=None, duration=None, timestamp=None):
        """Class responsible for managing the results of the distance between the two points
        Calculate the distance, save the history and be able to consult the history 

        Args:
            lat_orig: Origin latitude. Defaults to None.
            lng_orig: Origin longitude. Defaults to None.
            lat_dest: Destiny latitude. Defaults to None.
            lng_dest: Destiny longitude. Defaults to None.
            orig_addresses: Origin addresses. Defaults to None.
            dest_addresses: Destiny addresses. Defaults to None.
            distance: Distance text beetween points. Defaults to None.
            duration: Duration text beetween points. Defaults to None.
            timestamp: Timestamp of consult. Defaults to None.
        """        
        if (lat_orig and lng_orig and lat_dest and lng_dest): 
            self.lat_orig = lat_orig
            self.lng_orig = lng_orig
            self.lat_dest = lat_dest
            self.lng_dest = lng_dest

            if (orig_addresses or dest_addresses or distance or duration or timestamp):
                self.orig_addresses = orig_addresses
                self.dest_addresses = dest_addresses
                self.distance = distance
                self.duration = duration
                self.timestamp = timestamp
            else:
                self.__get_distance_results()
    
    def __get_distance_results(self):
        """
        Function that queries the googlemaps api and returns the distance information between the two informed coordinates
        """
        
        key = "AIzaSyCXt-eENymUYzhr8TAqhnpwx1p5y9swyW0"

        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        url += f"origins={self.lat_orig},{self.lng_orig}"
        url += f"&destinations={self.lat_dest},{self.lng_dest}"

        url += f"&key={key}"        
        results = requests.get(url).json()         

        print(results)

        
        self.orig_addresses = ",".join(results['origin_addresses'])
        self.dest_addresses = ",".join(results['destination_addresses'])

        if results['rows'][0]['elements'][0]["status"] == "ZERO_RESULTS":
            self.distance = "Invalid location"
            self.duration = "Invalid location"
        else:
            self.distance = results['rows'][0]['elements'][0]['distance']['text']
            self.duration = results['rows'][0]['elements'][0]['duration']['text']
                
        self.timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')  
        
    
    def save_history(self, filename="history.csv"):
        """Function responsible for saving the query in the history file 

        Args:
            filename: Log filename. Defaults to "history.csv".
        """        
        with open(filename, 'a', encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.lat_orig, self.lng_orig, self.lat_dest, self.lng_dest, self.orig_addresses, self.dest_addresses, self.distance, self.duration, self.timestamp]) 

    def load_history(filename="history.csv"):
        """Function responsible for consulting the results that are saved in the log file 

        Args:
            filename: Log filename. Defaults to "history.csv".

        Returns:
            list[DistanceResult]: List with DistanceResult objects saved on log file
        """        
        result = []
        with open(filename,'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')        
            for row in csv_reader:                
                result.append(DistanceResult(row[0], row[1], row[2], row[3], row[4],row[5], row[6], row[7], row[8]))
        return result 

# convert load_history() to static method
DistanceResult.load_history = staticmethod(DistanceResult.load_history)