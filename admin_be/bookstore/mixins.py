import logging

class BookstoreMixin:
    """Custom mixins for bookstore module"""
    
    def apply_discount(self,price,discounted_price):
        """Apply a percentage discount to the book's price."""
        if discounted_price < 0 or discounted_price > 100:
            raise ValueError("Discount price must be between 1 to 100 ")
        discounted_price = price * (1 - discounted_price / 100)
        return round(discounted_price, 2)

    def log_action(self, action, book_title):
        """Log an action related to a book (like create, update, or delete)."""
        logger = logging.getLogger(__name__)
        logger.info(f"Action: {action} | Book: {book_title}")
