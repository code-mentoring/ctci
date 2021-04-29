#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

struct Node {
    int value;
    struct Node *left;
    struct Node *right;
};

struct Node *make_node(int value) {
    struct Node *node;
    if ((node = malloc(sizeof *node)) == NULL) {
        fprintf(stderr, "failed to allocate space for a node, exiting");
        exit(1);
    }
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void free_node(struct Node *node) {
    if (node != NULL) {
        free_node(node->left);
        free_node(node->right);
        free(node);
    }
}

struct Node *parent_of_smallest_node(struct Node *tree) {
    if (tree->left->left == NULL) {
        return tree;
    }
    return parent_of_smallest_node(tree->left);
}

struct Node *tree_from_sorted(int *xs, const size_t start, const size_t end) {
    const size_t n = end-start;
    if (n == 1) {
        return make_node(xs[start]);
    }
    struct Node *left_tree = tree_from_sorted(xs, start, start+n/2);
    struct Node *right_tree = tree_from_sorted(xs, start+n/2, end);
    if (right_tree->left == NULL) {
        right_tree->left = left_tree;
        return right_tree;
    }
    struct Node *parent_of_root = parent_of_smallest_node(right_tree);
    struct Node *root = parent_of_root->left;
    parent_of_root->left = NULL;
    root->left = left_tree;
    root->right = right_tree;
    return root;
}

void display_edges(struct Node *tree) {
    if (tree->left != NULL) {
        printf("%d -> %d\n", tree->value, tree->left->value);
        display_edges(tree->left);
    }
    if (tree->right != NULL) {
        printf("%d -> %d\n", tree->value, tree->right->value);
        display_edges(tree->right);
    }
}

int main() {
    int xs[12] = {1,2,3,4,5,6,7,8,9,10,11,12};
    struct Node *tree = tree_from_sorted(xs, 0, 12);
    display_edges(tree);
    free_node(tree);
}
