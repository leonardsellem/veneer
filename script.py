#The Thin Veneer of Viability

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return '{artist}. \"{title}\". {year}, {medium}. {owner}, {location}.'.format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner = self.owner.name, location = self.owner.location)

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

veneer = Marketplace()
veneer.show_listings()

#We Need Clients

class Client():
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum
    def sell_artwork(self, artwork, price):
        if self != artwork.owner:
            pass
        else:
            veneer.add_listing(Listing(artwork, price, self))
    def buy_artwork(self, artwork):
        self.artwork = artwork
        if self.artwork.owner == self:
            pass
        else:
            for listing in veneer.listings:
                if listing.art == self.artwork:
                    art_listing = listing
                    self.artwork.owner = self
                    veneer.remove_listing(art_listing)
        

edytta = Client('Edytta Halpirt', 'Private Collection', False)
moma = Client('The MOMA', 'New York', True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
#print(girl_with_mandolin)

'''
marketplace = Marketplace()
marketplace.add_listing(girl_with_mandolin)
marketplace.show_listings()
marketplace.remove_listing(girl_with_mandolin)
marketplace.show_listings()
'''

#Don't Be Listless

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller
    def __repr__(self):
        return '{name} : USD {price}.'.format(name = self.art.title, price = self.price)
    

edytta.sell_artwork(girl_with_mandolin, 6000000)
print(girl_with_mandolin)

#Buy Low, Sell High
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()