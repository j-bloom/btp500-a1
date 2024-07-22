#    Main Author(s):
#    Main Reviewer(s):



class Stack:

    def __init__(self, cap=10):
        self.cap = cap
        self.count = 0
        # Fill an array size of capacity with None values
        self.stack = [None] * cap

    def capacity(self):
        return self.cap

    def push(self, data):

        # Check if stack capacity has been passed
        self.count += 1
        if self.cap < self.count:

            # Create a new stack double the size with None values
            self.cap *= 2
            newlist = [None]*self.cap

            # Then reverse copy the existing stack
            # into it since the stack is added to in reverse order.
            for i, v in enumerate(reversed(self.stack)):
                newlist[self.cap - 1 - i] = v

        # New array is set as stack and pushed value is added
            self.stack = newlist
        self.stack[self.cap - self.count] = data

    def pop(self):

        # Catch empty stack pop
        if self.count == 0:
            raise IndexError('pop() used on empty stack')

        # Store ref to top item from stack then set that index to None
        # and reduce the stack count. Top item index is simply
        # the stack capacity minus the current number of items in the stack
        item = self.stack[self.cap - self.count]
        self.stack[self.cap - self.count] = None
        self.count -= 1
        return item

    def get_top(self):
        # Top item index is stack capacity minus the current number of items
        if self.count == 0:
            return None
        return self.stack[self.cap - self.count]

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def __len__(self):
        return self.count


class Queue:

    def __init__(self, cap=10):
        self.front = 0
        self.back = 0
        self.count = 0
        self.cap = cap
        self.queue = [None]*cap


    def capacity(self):
        return self.cap

    def enqueue(self, data):

        # Move the index to the item at back forward by 1 or set index
        # to 0 if that index is out of bounds
        def moveBack(self):
            self.back += 1
            if self.back >= self.cap/2:
                self.back = 0

        # This branch runs if bounds of deque exceeded by this push operation
        if self.count >= self.cap:

            # Create a new queue double the size of the old filled with None values
            newqueue = [None] * self.cap*2
            newqueue[self.cap] = data
            self.cap *= 2

            # Copy all items from old queue into new starting from the old queues
            # back then moving forward and looping around until queue front reached
            index = 0
            newqueue[index] = self.queue[self.back]
            index += 1
            moveBack(self)
            while self.back != self.front:
                newqueue[index] = self.queue[self.back]
                index += 1
                moveBack(self)
            newqueue[index] = self.queue[self.back]

            # Set newqueue as deque and set back to 0 and front to one past new item
            self.queue = newqueue
            self.back = 0
            self.front = index + 1

        # This branch runs if deque capacity not passed this push
        else:

            # If item exists at current front index move front forward by 1 wrapping
            # around if needed and assign item to that index
            if self.queue[self.front] is not None:
                self.front += 1
                if self.front >= self.cap:
                    self.front = 0
            self.queue[self.front] = data

        # If no items in deque set front to index 0
        if self.count == 0:
            self.front = 0


        # In all cases increase count by one
        self.count += 1

    def dequeue(self):
        # Check for calling pop on empty deque
        if self.count == 0:
            raise IndexError('dequeue() used on empty queue')

        # Copy item at queue back then set the value of that index to 0
        item = self.queue[self.back]
        self.queue[self.back] = None

        # move back forward by 1 index wrapping around to index 0
        # if out of bounds
        self.back += 1
        if self.back >= self.cap:
            self.back = 0

        # In any case reduce count by 1 and return item
        self.count -= 1
        return item

    def get_front(self):
        if self.count == 0:
            return None
        return self.queue[self.back]

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def __len__(self):
        return self.count


class Deque:

    def __init__(self, cap=10):
        self.cap = cap
        self.count = 0
        self.front = 0
        self.back = 0
        self.deque = [None]*cap

    def capacity(self):
        return self.cap

    def push_front(self, data):


        # Move the index to the item at back forward by 1 or set index
        # to 0 if that index is out of bounds
        def moveBack(self):
            self.back += 1
            if self.back >= self.cap/2:
                self.back = 0

        # This branch runs if bounds of deque exceeded by this push operation
        if self.count >= self.cap:

            # Create a new deque double the size of the old filled with None values
            newdeque = [None] * self.cap*2
            newdeque[self.cap] = data
            self.cap *= 2

            # Copy all items from old queue into new starting from the old queues
            # back then moving forward and looping around until queue front reached
            index = 0
            newdeque[index] = self.deque[self.back]
            index += 1
            moveBack(self)
            while self.back != self.front:
                newdeque[index] = self.deque[self.back]
                index += 1
                moveBack(self)
            newdeque[index] = self.deque[self.back]

            # Set newdeque as deque and set back to 0 and front to one past new item
            self.deque = newdeque
            self.back = 0
            self.front = index + 1

        # This branch runs if deque capacity not passed this push
        else:

            # If item exists at current front index move front forward by 1 wrapping
            # around if needed and assign item to that index
            if self.deque[self.front] is not None:
                self.front += 1
                if self.front >= self.cap:
                    self.front = 0
            self.deque[self.front] = data

        # If no items in deque set front to index 0
        if self.count == 0:
            self.front = 0

        # In all cases increase count by one
        self.count += 1

    def push_back(self, data):

        # Move the index to the item at back forward by 1 or set index
        # to 0 if that index is out of bounds
        def moveBack(self):
            self.back += 1
            if self.back >= self.cap/2:
                self.back = 0

        # This branch runs if bounds of deque exceeded by this push operation
        if self.count >= self.cap:

            # Create a new deque double the capacity of the old filled with None
            newdeque = [None] * self.cap*2

            # Item being pushed to back is added to index 0 of new deque
            newdeque[0] = data
            self.cap *= 2

            # Copy all items from old deque into new starting at old deques
            # back then moving forward and wrapping around until front equals back
            index = 1
            newdeque[index] = self.deque[self.back]
            index += 1
            moveBack(self)
            while self.back != self.front:
                newdeque[index] = self.deque[self.back]
                index += 1
                moveBack(self)
            newdeque[index] = self.deque[self.back]

            # Set new deque as deque and back to index 0 and front to index of last
            # value not None
            self.deque = newdeque
            self.back = 0
            self.front = index

        # This branch runs if deque capacity not passed this push
        else:

            # If item exists at current back index set move back back by 1
            # wrapping around if needed to end of array then add item to that index
            if self.deque[self.back] is not None:
                self.back -= 1
                if self.back < 0:
                    self.back = self.cap - 1
            self.deque[self.back] = data

        # If deque empty set back to index 0
        if self.count == 0:
            self.back = 0

        # In all cases increate count by one
        self.count += 1

    def pop_front(self):

        # Check for calling pop on empty deque
        if self.count == 0:
            raise IndexError('pop_front() used on empty deque')

        # Copy item at deque front then set the value of that index to 0
        item = self.deque[self.front]
        self.deque[self.front] = None

        # move front back by 1 index wrapping around to index at front of array
        # if out of bounds
        self.front -= 1
        if self.front < 0:
            self.front = self.cap - 1

        # In any case reduce count by 1 and return item
        self.count -= 1
        return item

    def pop_back(self):

        # Check for calling pop on empty deque
        if self.count == 0:
            raise IndexError('pop_back() used on empty deque')

        # Copy item at deque back then set the value of that index to 0
        item = self.deque[self.back]
        self.deque[self.back] = None

        # move back forward by 1 index wrapping around to index 0
        # if out of bounds
        self.back += 1
        if self.back >= self.cap:
            self.back = 0

        # In any case reduce count by 1 and return item
        self.count -= 1
        return item

    def get_front(self):
        return self.deque[self.front]

    def get_back(self):
        return self.deque[self.back]

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def __len__(self):
        return self.count

    def __getitem__(self, k):

        # Check if index we are getting is outside array
        if k > self.count - 1:
            raise IndexError('Index out of range')

        # If k is greater than front
        # Subtract the difference from the deque capacity then return the
        # value at that index
        if k > self.front:
            idx = (self.front - k) + self.cap
            return self.deque[idx]

        # If k is less than front return the value at the index of
        # front minus k
        return self.deque[self.front - k]
