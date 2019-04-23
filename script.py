#The Thin Veneer of Viability

class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year

    def __repr__(self):
        return '{artist}. \"{title}\". {year}, {medium}.'.format(artist = self.artist, title = self.title, year = self.year, medium = self.medium)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910)
#print(girl_with_mandolin)

#The Marketplace of Artistic Ideas

class Marketplace:
    def __init__(self):
        self.listings = []
    def __iter__(self):
        return iter(self.listings)
    def add_listing(self, new_listing):
        self.listings.append(new_listing)
    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)
    def show_listings(self):
        for listing in self.listings:
            print(listing)

#marketplace = Marketplace()
#marketplace.add_listing(girl_with_mandolin)
#marketplace.show_listings()

veneer = Marketplace()
veneer.show_listings()