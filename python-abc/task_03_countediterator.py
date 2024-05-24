class CountedIterator:
    """
    CountedIterator extends the built-in iterator to keep track
    of the number of items iterated over.
    """
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        Raise StopIteration when there are no more items.
        """
        try:
            item = self.iterator.__next__()
        except StopIteration:
            raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over.
        """
        return self.count

