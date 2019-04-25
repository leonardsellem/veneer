class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner
    def __repr__(self):
        return '{artist}. \"{title}\". {year}, {medium}. {owner}, {location}.'.format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner = self.owner.name, location = self.owner.location)

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


class Client():
    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.location = location
        self.is_museum = is_museum
        self.wallet = wallet
    def __repr__(self):
        return "{name}, {location}. Has {wallet} in wallet.".format(name = self.name, location = self.location, wallet = self.wallet)
    def sell_artwork(self, artwork, price, marketplace):
        self.marketplace = marketplace
        if self != artwork.owner:
            pass
        else:
            self.marketplace.add_listing(Listing(artwork, price, self, marketplace))
    def buy_artwork(self, artwork, marketplace):
        self.artwork = artwork
        self.marketplace = marketplace
        if self.artwork.owner == self:
            print("{name} is already the proud owner of {artwork}".format(name = self.name, artwork = self.artwork.title))
        else:
            for listing in self.marketplace.listings:
                if listing.art == self.artwork:
                    if self.wallet >= listing.price:
                        art_listing = listing
                        self.artwork.owner.wallet += listing.price
                        self.artwork.owner = self
                        self.artwork.owner.wallet -= listing.price
                        self.marketplace.remove_listing(art_listing)
                    else:
                        print("{name} cannot afford to buy {artwork}. He needs to find USD {money_needed} more.".format(name = self.name, artwork = self.artwork.title, money_needed = listing.price - self.artwork.owner.wallet))
            try:
                art_listing
            except NameError:
                print("{artwork} is not for sale at the moment. Come back and check later.".format(artwork = self.artwork.title))
            
class Listing:
    def __init__(self, art, price, seller, marketplace):
        self.art = art
        self.price = price
        self.seller = seller
        self.marketplace = marketplace
    def __repr__(self):
        return '{name} : USD {price}.'.format(name = self.art.title, price = self.price)