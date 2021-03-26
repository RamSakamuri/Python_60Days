class Node:

  def __init__(self, info, link=None):
    self.info = info
    self.link = link

first = Node(20)
print(first.info)