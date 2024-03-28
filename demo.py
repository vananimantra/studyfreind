class AuctionItem:
    def __init__(self, name, starting_price):
        self.name = name
        self.starting_price = starting_price
        self.current_bid = starting_price
        self.bidder = None

    def place_bid(self, bidder, bid_amount):
        if bid_amount > self.current_bid:
            self.current_bid = bid_amount
            self.bidder = bidder
            print(f"{bidder} has placed a bid of {bid_amount} on {self.name}.")
        else:
            print("Bid amount must be greater than the current bid.")

class Auction:
    def __init__(self, item):
        self.item = item

    def start_auction(self):
        print(f"Auction for {self.item.name} has started with a starting price of {self.item.starting_price}.")
        while True:
            bidder = input("Enter your name (or 'quit' to end the auction): ")
            if bidder.lower() == 'quit':
                break
            bid_amount = float(input("Enter your bid amount: "))
            self.item.place_bid(bidder, bid_amount)
        print(f"The auction for {self.item.name} has ended.")
        if self.item.bidder:
            print(f"{self.item.bidder} won the auction with a bid of {self.item.current_bid}.")
        else:
            print("No bids were placed on the item.")

# Example usage
item_name = input("Enter the name of the item: ")
starting_price = float(input("Enter the starting price of the item: "))
item = AuctionItem(item_name, starting_price)
auction = Auction(item)
auction.start_auction()

