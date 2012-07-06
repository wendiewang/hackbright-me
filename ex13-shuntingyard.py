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
operation_dictionary = {"*":3, "/":3, "+":2, "-":2}

#if token is ")", 
    #Until token at top of stack is "(" pop operators off the stack combining w/last 2 elements
    #to create binary tree node and putting on stack

    while len(token_list) > 0:
        token = consume(token_list)
        output_queue = []
        operator_stack = []
        if is_num(token):
            output_queue.append(token)
        elif token in "+-*/":
            if len(operator_stack) == 0:
            root = BinaryTreeNode(token)
            root.left = output_queue.pop(-2)
            root.right = output_queue.pop(-1)
            output_queue.append(root)
            elif operation_dictionary(token) > operation_dictionary(operator_stack[-1]):
                output_queue.append(token)
            elif operation_dictionary(token) <= operation_dictionary(operator_stack[-1]):    
                output_queue.append(operator_stack[-1])
                operator_stack.append(token)


        elif token == "(":
            operator_stack.push(token)
        #>>>>>>>>elif token == ")":
        left = BinaryTreedNode(output_queue[0])
        right = BinaryTreedNode(output_queue[1])

    """Takes in a token list and produces a parse tree according to the rules in the README"""
    # IMPLEMENT SHUNTING YARD ALGORITHM HERE
    root = BinaryTreeNode("+")
    left = BinaryTreeNode(3)
    right = BinaryTreeNode(2)
    root.left = left
    root.right = right
    return root

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
    sample_string = "(3 + (2 + 5))"
    tokens = tokenize(sample_string)
    tree = build_parse_tree(tokens)
    print evaluate_tree(tree)

if __name__ == "__main__":
    main()
