# This class is responsible for talking to the Flight Search API.

class FlightSearch:

    def __init__(self):
        self.results=[]
    pass

    def getinfo(self,json):
        for x in json["data"]:
            for itinerary in x["itineraries"]:
                segments = itinerary["segments"]
                for segment in segments:
                    result = {
                        "lastTicketingDate": x.get("lastTicketingDate"),
                        "lastTicketingDateTime": x.get("lastTicketingDateTime"),
                        "grandPrice": x["price"].get("grandTotal"),
                        "departureIATA": segment["departure"].get("iataCode"),
                        "departureTime": segment["departure"].get("at"),
                        "arrivalIATA": segment["arrival"].get("iataCode")}
                    self.results.append(result)
        return self.results






