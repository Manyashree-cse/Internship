class RoyalMessenger:
    def deliver(self, message):
        return f"Delivered: {message}"

class UrgentMessenger(RoyalMessenger):
    def deliver(self, message):
        return f"URGENT: Delivered: {message}"

# Example usage
royal = RoyalMessenger()
urgent = UrgentMessenger()
royal.deliver("Meeting at noon.")
urgent.deliver("Dragon sighted near village!")
