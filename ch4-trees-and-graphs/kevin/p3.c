#include <stdlib.h>
#include <stdio.h>

#define NODE_LIST_INITIAL_CAPACITY 4

#define NODE_LIST_ADD_SUCCESS 0
#define NODE_LIST_ADD_ALLOC_FAIL -1

typedef struct node {
    int value;
    struct node *left;
    struct node *right;
} node_t;

typedef struct {
    node_t **nodes;
    size_t length;
    size_t capacity;
} node_list_t;

node_list_t *make_node_list() {
    node_list_t *list = NULL;
    if ((list = malloc(sizeof *list)) == NULL) {
        return NULL;
    }
    list->length = 0;
    list->capacity = NODE_LIST_INITIAL_CAPACITY;
    if ((list->nodes = malloc(NODE_LIST_INITIAL_CAPACITY * sizeof *(list->nodes))) == NULL) {
        free(list);
        return NULL;
    }
    return list;
}

void free_node_list(node_list_t *list) {
    if (list == NULL) {
        return;
    }
    free(list->nodes);
    free(list);
}

int node_list_add(node_list_t *list, node_t *node) {
    if (list->capacity <= list->length) {
        // Time to grow.
        list->capacity *= 2;
        list->nodes = realloc(list->nodes, list->capacity * sizeof(*(list->nodes)));
        if (list->nodes == NULL) {
            return NODE_LIST_ADD_ALLOC_FAIL;
        }
    }
    list->nodes[list->length++] = node;
    return NODE_LIST_ADD_SUCCESS;
}

node_t *node_list_get(node_list_t *list, size_t i) {
    if (i >= list->length) {
        return NULL;
    }
    return list->nodes[i];
}

size_t tree_max_depth(node_t *root) {
    if (root == NULL) {
        return 0;
    }
    // I sure hope your trees aren't going to be too deep.
    size_t left_depth = tree_max_depth(root->left);
    size_t right_depth = tree_max_depth(root->right);
    return 1 + (left_depth < right_depth ? right_depth : left_depth);
}

int main() {
    /*
       root
        |\
        | \
        x  y
        |
        z
    */
    node_t z = { .value = 3, .left = NULL, .right = NULL };
    node_t x = { .value = 5, .left = &z, .right = NULL };
    node_t y = { .value = -1, .left = NULL, .right = NULL };
    node_t root = { .value = 1, .left = &x, .right = &y };

    const size_t D = tree_max_depth(&root);
    node_list_t **lists = NULL;
    if ((lists = malloc(D * sizeof(*lists))) == NULL) {
        fprintf(stderr, "failed to allocate memory for list of lists\n");
        exit(1);
    }
    // first, set 'em all to NULL so that they
    // can be free'd later on, even if they haven't
    // been set.
    for (size_t i = 0; i < D; ++i) {
        lists[i] = NULL;
    }
    // then try to malloc.
    for (size_t i = 0; i < D; ++i) {
        if ((lists[i] = make_node_list()) == NULL) {
            fprintf(stderr, "failed to allocate node list\n");
            goto cleanup;
        }
    }

    // now fill up the lists.
    if (node_list_add(lists[0], &root) != NODE_LIST_ADD_SUCCESS) {
        fprintf(stderr, "failed to add node to list\n");
        goto cleanup;
    }
    for (size_t i = 1; i < D; ++i) {
        node_list_t *previous = lists[i-1];
        node_list_t *current = lists[i];
        // take all nodes at previous level and add their children.
        for (size_t j = 0; j < previous->length; ++j) {
            node_t *node = node_list_get(previous, j);
            if (node->left != NULL) {
                if (node_list_add(current, node->left) != NODE_LIST_ADD_SUCCESS) {
                    fprintf(stderr, "failed to add node to list\n");
                    goto cleanup;
                }
            }
            if (node->right != NULL) {
                if (node_list_add(current, node->right) != NODE_LIST_ADD_SUCCESS) {
                    fprintf(stderr, "failed to add node to list\n");
                    goto cleanup;
                }
            }
        }
    }

    // now print 'em out.
    for (size_t i = 0; i < D; ++i) {
        node_list_t *list = lists[i];
        printf("At depth %zu: ", i);
        for (size_t j = 0; j < list->length; ++j) {
            printf("%d ", node_list_get(list, j)->value);
        }
        printf("\n");
    }

cleanup:
    for (size_t i = 0; i < D; ++i) {
        free_node_list(lists[i]);
    }
    free(lists);
    return 0;
}
