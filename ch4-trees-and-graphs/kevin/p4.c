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

bool is_balanced_with_count(struct Node *tree, size_t *count) {
    if (tree == NULL) {
        *count = 0;
        return true;
    }
    size_t left_count;
    size_t right_count;
    bool result = is_balanced_with_count(tree->left, &left_count)
               && is_balanced_with_count(tree->right, &right_count)
               && left_count == right_count;
    *count = left_count + right_count + 1;
    return result;
}

bool is_balanced(struct Node *tree) {
    size_t dummy_count;
    return is_balanced_with_count(tree, &dummy_count);
}

int main() {
    struct Node *root = make_node(3);
    struct Node *left = make_node(2);
    struct Node *right = make_node(4);
    struct Node *right_right = make_node(5);
    root->left = left;
    root->right = right;
    right->right = right_right;
    display_edges(root);

    printf(is_balanced(root) ? "balanced" : "NOT balanced");
    printf("\n");
    free_node(root);
}
