def choose_winner(bidders):
    max_bidder = [(value, key) for key, value in bidders.items()]
    max_bidder = max(max_bidder)[1]
    return max_bidder