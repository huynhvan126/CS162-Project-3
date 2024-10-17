# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/16/2024
# Description: Writing a Library simulator involving multiple classes.
class LibraryItem:
    """
    Represents an item in a library.
    """
    def __int__(self, library_item_id, title):
        """
        Initializes a LibraryItem object with its ID and title.
        """
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._data_checked_out = None

    def get_library_item_id(self):
        """
        Returns the ID of the library item.
        """
        return self._library_item_id

    def get_title(self):
        """
        Returns the title of the library item.
        """
        return self._title

    def get_location(self):
        """
        Returns the location of the library item.
        """
        return self._location

    def set_location(self, location):
        """
        Sets the location of the library item.
        """
        self._location = location

    def get_checked_out_by(self):
        """
        Returns the checked out by.
        """
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """
        Sets the checked out by.
        """
        self._checked_out_by = patron

    def get_requested_by(self):
        """
        Returns the requested by.
        """
        return self._requested_by

    def set_requested_by(self, patron):
        """
        Sets the requested by.
        """
        self._requested_by = patron

    def get_date_checked_out(self):
        """
        Returns the date checked out.
        """
        return self._date_checked_out

    def set_date_checked_out(self, date):
        """
        Sets the date checked out.
        """
        self._date_checked_out = date

class Book(LibraryItem):
    """
    Represents a LibraryItem in a book.
    """
    def __init__(self, library_item_id, title, author):
        """
        Initializes a Book object.
        """
        super().__int__(library_item_id, title)
        self._author = author

    def get_author(self):
       """
       Returns the author of the book.
       """
        return self._author

    def get_checked_out_length(self):
        """
        Returns the checked out length of the book.
        """
        return 21

class Album(LibraryItem):
    """
    Represents a LibraryItem in an album.
    """
    def __init__(self, library_item_id, title, artist):
        """
        Initializes a Album object.
        """
        super().__int__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """
        Returns the artist of the book.
        """
        return self._artist

    def get_checked_out_length(self):
        """
        Returns the checked out length of the book.
        """
        return 14

class Movie(LibraryItem):
    """
    Represents a LibraryItem in a movie.
    """
    def __init__(self, library_item_id, title, director):
        """
        Initializes a Movie object.
        """
        super().__int__(library_item_id, title)
        self._director = director

    def get_director(self):
        """
        Returns the director of the book.
        """
        return self._director

    def get_checked_out_length(self):
        """
        Returns the checked out length of the book.
        """
        return 7

class Patron:
    """
    Represents a LibraryItem in a patron.
    """
    def __init__(self, patron_id, name):
        """
        Initializes a Patron object.
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def get_patron_id(self):
        """
        Returns the patron ID.
        """
        return self._patron_id

    def get_name(self):
        """
        Returns the name of the patron.
        """
        return self._name

    def get_fine_amount(self):
        """
        Returns the fine_amount of the patron.
        """
        return self._fine_amount

    def add_library_item(self, item)
        """
        Adds a library item to the patron.
        """
        self._checked_out_items.append(item)

    def remove_library_item(self, item)
        """
        Removes a library item from the patron.
        """
        self._checked_out_items.remove(item)

    def amend_fine(self, amount):
        """
        Amends the fine_amount of the patron.
        """
        self._fine_amount += amount

class Library:
    """
    Represents a Library object.
    """
    def __init__(self):
        """
        Initializes a Library object.
        """
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, item):
        """
        Adds a library item to the library.
        """
        self._holdings.append(item)

    def add_patron(self, patron):
        """
        Adds a patron to the library.
        """
        self._members.append(patron)

    def lookup_library_item_from_id(self, item_id):
        """
        Looks up a library item by its ID.
        """
        for item in self._holdings:
            if item.get_library_item_id() == item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """
        Looks up a patron by its ID.
        """
        for patron_id in self._members:
            if patron.get_patron_id() == patron_id:
                return patron_id
        return None

    def check_out_library_item(self, patron_id, item_id):
        """
        Checks out a library item by its ID.
        """
        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        item = self.lookup_library_item_from_id(item_id)
        if not item:
            return "item not found"

        if item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if item.get_requested_by() and item.get_requested_by() != patron
            return "item on hold by other patron"

        item.set_checked_out_by(patron)
        item.set_location("CHECKED_OUT")
        item.set_date_checked_out(self._current_date)
        if item.get_requested_by() == patron:
            item.set_requested_by(None)
        patron.add_library_item(item)
        return "check out successful"

    def return_library_item(self, item_id):
        """
        Returns the library item by its ID.
        """
        item = self.lookup_library_item_from_id(item_id)
        if not item:
            return "item not found"

        if item.get_location() == "CHECKED_OUT":
            return "item already in library"

        patron = item.get_checked_out_by()
        if patron:
            patron.remove_library_item(item)

        if item.get_requested_by():
            item.set_location("ON_HOLD_SHELF")
        else:
            item.set_location ("ON_SHELF")

        item.set_checked_out_by (None)
        return "return successful"

    def request_library_item(self, patron_id, item_id):
        """
        Requests a library item by its ID.
        """
        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        item = self.lookup_library_item_from_id(item_id)
        if not item:
            return "item not found"

        if item.get_requested_by()
            return "item already on hold"

        item.set_requested_by(patron)
        if item.get_location() == "ON_SHELF":
            item.set_location("ON_HOLD_SHELF")
        return "request successful"

    def pay_fine(self, patron_id, amount):
        """
        Pays a patron's fine.
        """
        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        patron.amend_fine(-amount)
        return "pay successful"

    def increment_current_date(self):
        """
        Increments the current date.
        """
        self._current_date += 1
        for patron in self._members:
            for item in patron._checked_out_items:
                overdue_days = self._current_date - (item.get_date_checked_out() + item.get_check_out_length())
                if overdue_days > 0:
                    patron.amend_fine(0.1 * overdue_days)