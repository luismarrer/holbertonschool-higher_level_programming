class VerboseList(list):
    """
    VerboseList is a subclass of the built-in list that provides
    custom notifications for list modifications.
    """
    def append(self, item):
        """
        Add an item to the end of the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a notification.
        """
        length_before = len(self)
        super().extend(iterable)
        length_after = len(self)
        print(f"Extended the list with [{length_after - length_before}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of the item from the list and
        print a notification.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Remove and return the item at the given index and print a
        notification. If no index is specified, remove and return
        the last item in the list.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

