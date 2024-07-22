#    Main Author(s):
#    Main Reviewer(s):




class SortedList:

	class Node:
		# Function initializes a new node
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.front = next
			self.back = prev

		def get_data(self):
			return self.data
		
		# Function returns a reference to the next node in the Sortedlist
		def get_next(self):
			if self.next == self.back:
				return None
			
			return self.next

		# Function returns a reference to the previous node in the Sortedlist
		def get_previous(self):
			if self.prev == self.front:
				return None
			
			return self.prev

	# Function initializes a Linked List
	def __init__(self):
		self.front = self.Node(None)
		self.back = self.Node(None)
		self.front.next = self.back
		self.back.prev = self.front

	# Function returns a reference to the first data node. Returns None if the
	# list is empty
	def get_front(self):
		if self.front.next is not self.back:
			return self.front.next
		else:
			return None

	# Function returns a reference to the last data node. Returns None if the
	# list is empty
	def get_back(self):
		if self.back.prev is not self.front:
			return self.back.prev
		else:
			return None

	# Function returns True if the Sorted List is empty
	def is_empty(self):
		if self.front is self.back.prev:
			return True
		else:
			return False
		
	# Function returns the number of nodes that store values
	def __len__(self):
		list_length = 0
		current_node = self.front.next

		# If list is empty return 0 elements
		if current_node is self.back:
			return list_length
		else:
			# If list is not empty loop through the list, adding 1
            		# to the counter for each node between sentinels
			while current_node is not self.back:
				list_length += 1
				current_node = current_node.next
			return list_length

	# Function inserts a new node in the correct position keeping list sorted
    	# Function returns a reference to the new node that got added
	def insert(self,data):
		nn = self.Node(data)

		# If list is empty, add new node between sentinels
		if self.front is self.back.prev:
			nn.next = self.back
			nn.prev = self.front
			self.front.next = nn
			self.back.prev = nn
			return nn
		
		current_node = self.front.next

		# If the first node data is greater then argument data if
        	# if so push new node in first position
		if current_node.data > nn.data:
			nn.next = current_node
			nn.prev = current_node.prev
			current_node.prev.next = nn
			current_node.prev = nn
			return nn
		
		# If first node data is smaller then argument data, loop until
        	# current node data is smaller or end of list reached and 
        	# prepend current node or sentinel
		if current_node.data < nn.data:
			while current_node is not self.back:
				current_node = current_node.next

				if current_node is self.back:
					nn.next = current_node
					nn.prev = current_node.prev
					current_node.prev.next = nn
					current_node.prev = nn
					return nn
				
				if current_node.data > nn.data:
					nn.next = current_node
					nn.prev = current_node.prev
					current_node.prev.next = nn
					current_node.prev = nn
					return nn

	# Function removes the node that is stored in the position passed as
	# an argument
	def erase(self,node):
		current_node = self.front.next

		if node is None:
			raise ValueError('Cannot erase node referred to by None')

		elif current_node is node:
			current_node.next.prev = current_node.prev
			current_node.prev.next = current_node.next

		else:
			# Loop through the list until desired node is found
            		# Change pointers to before removing desired node
			while current_node is not node:
				current_node = current_node.next

			if current_node is node:
				current_node.next.prev = current_node.prev
				current_node.prev.next = current_node.next

	# Function returns a reference to the node that is stored in the position
	# passed as an argument
	def search(self, data):
		current_node = self.front.next
                
		if current_node is self.back:
			return None
		
		while current_node is not self.back:
			if current_node.data != data:
				current_node = current_node.next
						
			if current_node.data == data:
				return current_node
