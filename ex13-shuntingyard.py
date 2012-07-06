#!/usr/bin/env python

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tokenize(string):
    return string.replace("(", " ( ").replace(")", " ) ").split()

def consume(token_list):
    return token_list.pop(0)

def build_parse_tree(token_list):
	queue = []
	stack = []

	oper_dict = {"*":3, "/":3, "+":2, "-":2}

	while len(token_list) > 0:
		token = consume(token_list)
		if is_num(token):
			queue.append(int(token))
		elif token in ['*', '/', '-', '+']:
			o1 = token
			while len(stack) > 0 and stack[-1] in ['*', '/', '-', '+']: 
				o2 = stack[-1]
				if oper_dict[o1] <= oper_dict[o2]:
					o2 = stack.pop()
					right = queue.pop() # take last 2 elements from queue
					left = queue.pop() 
					root = BinaryTreeNode(o2) # build binary tree
					if is_num(left):
						left = BinaryTreeNode(left)
					if is_num(right):
						right = BinaryTreeNode(right)
					root.left = left # set left and right children
					root.right = right 
					queue.append(root)
			stack.append(o1)
		elif token == "(":
			stack.append(token)
		elif token == ")":
			while stack[-1] != "(":
				n = stack.pop()
				right = queue.pop()
				left = queue.pop()
				root = BinaryTreeNode(n)
				if is_num(left):
					left = BinaryTreeNode(left)
				if is_num(right):
					right = BinaryTreeNode(right)
				root.left = left
				root.right = right 
				queue.append(root)
			stack.pop()

	while len(stack) > 0:
		n = stack.pop()
		right = queue.pop()
		left = queue.pop()
		root = BinaryTreeNode(n)
		if is_num(left):
			left = BinaryTreeNode(left)
		if is_num(right):
			right = BinaryTreeNode(right)
		root.left = left
		root.right = right
		queue.append(root)

	return queue[-1]

def is_num(string):
    try:
        int(string)
        return True
    except:
        return False

def evaluate_tree(node):
    if node is None:
        return
    if type(node.value) == int:
        return node.value
    elif node.value == "+":
        return evaluate_tree(node.left) + evaluate_tree(node.right)
    elif node.value == "*":
        return evaluate_tree(node.left) * evaluate_tree(node.right)
    elif node.value == "/":
        return evaluate_tree(node.left) / evaluate_tree(node.right)
    elif node.value == "-":
        return evaluate_tree(node.left) - evaluate_tree(node.right)

def main():
    sample_string = "(((3 + 2) * (4 - 1) / 3 + 7) * (1 + (-5 + 6)))"
    #sample_string = "(3 + (2 + 5))"
    tokens = tokenize(sample_string)
    tree = build_parse_tree(tokens)
    print evaluate_tree(tree)

if __name__ == "__main__":
    main()
