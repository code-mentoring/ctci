#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define ADD_EDGE_ALLOC_FAIL -1
#define ADD_EDGE_INVALID_VERTEX -2

#define PATH_BETWEEN_ALLOC_FAIL -1
#define PATH_BETWEEN_SUCCESS 0

#define VERTEX_LIST_INITIAL_CAPACITY 4

/* PART 1: Vertices and lists of them. */

typedef struct {
    int id;
    char *label;
} vertex_t;

typedef struct {
    size_t capacity;
    size_t n;
    vertex_t **vs;
} vertex_list_t;

bool vertices_equal(vertex_t *u, vertex_t *v) {
    if (u == NULL || v == NULL) {
        return u == v;
    }
    return u->id == v->id;
}

vertex_list_t *make_vertex_list() {
    vertex_list_t *list;
    if ((list = malloc(sizeof *list)) == NULL) {
        return NULL;
    }
    list->capacity = VERTEX_LIST_INITIAL_CAPACITY;
    list->n = 0;
    if ((list->vs = malloc(VERTEX_LIST_INITIAL_CAPACITY * sizeof *(list->vs))) == NULL) {
        free(list);
        return NULL;
    }
    return list;
}

bool vertex_list_add(vertex_list_t *list, vertex_t *vertex) {
    if (list->n == list->capacity) {
        // Need to add more space.
        list->capacity *= 2;
        if ((list->vs = realloc(list->vs, list->capacity * sizeof *(list->vs))) == NULL) {
            return false;
        }
            
    }
    list->vs[list->n++] = vertex;
    return true;
}

bool vertex_list_is_empty(vertex_list_t *list) {
    return list->n == 0;
}

vertex_t *vertex_list_pop(vertex_list_t *list) {
    if (vertex_list_is_empty(list)) {
        return NULL;
    }
    return list->vs[--(list->n)];
}

bool vertex_list_contains(vertex_list_t *list, vertex_t *v) {
    for (size_t i = 0; i < list->n; ++i) {
        if (vertices_equal(v, list->vs[i])) {
            return true;
        }
    }
    return false;
}

vertex_t *vertex_list_get(vertex_list_t *list, size_t i) {
    if (i >= list->n) {
        return NULL;
    }
    return list->vs[i];
}

void free_vertex_list(vertex_list_t *list) {
    // Don't free the vertices, that should be the
    // responsibility of whoever created them.
    free(list->vs);
    free(list);
}


/* PART 2: Graphs and their edges. */

typedef struct edge {
    vertex_t *from;
    vertex_t *to;
    struct edge *next;
} edge_t;

typedef struct {
    vertex_list_t *vertices;
    size_t next_id;
    edge_t *edges_head;
} graph_t;

graph_t *make_graph() {
    graph_t *g = NULL;
    if ((g = malloc(sizeof *g)) == NULL) {
        return NULL;
    }
    if ((g->vertices = make_vertex_list()) == NULL) {
        free(g);
        return NULL;
    }
    g->next_id = 0;
    g->edges_head = NULL;
    return g;
}

void free_vertex(vertex_t *v) {
    free(v);
}

vertex_t *graph_add_vertex(graph_t *g, char *label) {
    vertex_t *vertex = malloc(sizeof *vertex);
    if (vertex == NULL) {
        return NULL;
    }
    vertex->id = g->next_id++;
    vertex->label = label;
    if (!vertex_list_add(g->vertices, vertex)) {
        free_vertex(vertex);
        return NULL;
    }
    return vertex;
}

void free_graph(graph_t *g) {
    vertex_list_t *list = g->vertices;
    for (size_t i = 0; i < list->n; ++i) {
        free_vertex(vertex_list_get(list, i));
    }
    free_vertex_list(list);

    edge_t *current = g->edges_head;
    while (current != NULL) {
        edge_t *to_be_freed = current;
        current = current->next;
        free(to_be_freed);
    }

    free(g);
}

bool graph_contains(graph_t *g, vertex_t *v) {
    return vertex_list_contains(g->vertices, v);
}

bool graph_add_edge(graph_t *g, vertex_t *from, vertex_t *to, int *err_code) {
    if (!graph_contains(g, from) || !graph_contains(g, to)) {
        *err_code = ADD_EDGE_INVALID_VERTEX;
        return false;
    }
    edge_t *e;
    if ((e = malloc(sizeof *e)) == NULL) {
        *err_code = ADD_EDGE_ALLOC_FAIL;
        return false;
    }
    e->from = from;
    e->to = to;
    e->next = g->edges_head;
    g->edges_head = e;
    return true;
}

void dump_graph(graph_t *g) {
    printf("strict digraph G {\n");

    // first write the list of vertices.
    for (size_t i = 0; i < g->vertices->n; ++i) {
        vertex_t *v = vertex_list_get(g->vertices, i);
        printf("  %d [shape=circle,label=\"%s\"]\n", v->id, v->label);
    }

    // then the edges.
    edge_t *e = g->edges_head;
    while (e != NULL) {
        vertex_t *from = e->from;
        vertex_t *to = e->to;
        printf("  %d -> %d\n", from->id, to->id);
        e = e->next;
    }

    // kthxbye.
    printf("}\n");
}

/* PART 3: The actual algorithm. */

int path_between(graph_t *g, vertex_t *from, vertex_t *to, bool *result) {
    vertex_list_t *seen = NULL;
    vertex_list_t *stack = NULL;
    int flag = PATH_BETWEEN_SUCCESS;
    *result = false;

    if (!graph_contains(g, from) || !graph_contains(g, to)) {
        goto end;
    }

    if ((seen = make_vertex_list()) == NULL
            || (stack = make_vertex_list()) == NULL
            || !vertex_list_add(stack, from)) {
        flag = PATH_BETWEEN_ALLOC_FAIL;
        goto end;
    }

    while (!vertex_list_is_empty(stack)) {
        vertex_t *v = vertex_list_pop(stack);
        if (!vertex_list_contains(seen, v)) {
            if (vertices_equal(to, v)) {
                *result = true;
                break;
            }
            if (!vertex_list_add(seen, v)) {
                flag = PATH_BETWEEN_ALLOC_FAIL;
                goto end;
            }
            edge_t *e = g->edges_head;
            while (e != NULL) {
                if (vertices_equal(e->from, v)) {
                    if (!vertex_list_add(stack, e->to)) {
                        flag = PATH_BETWEEN_ALLOC_FAIL;
                        goto end;
                    }
                }
                e = e->next;
            }
        }
    }
    

end: // goto considered beneficial
    free_vertex_list(seen);
    free_vertex_list(stack);
    return flag;
}


/* PART 4: Test it out. */

void test_algo(graph_t *g, vertex_t *u, vertex_t *v) {
    printf("%s -> %s: ", u->label, v->label);
    bool result;
    if (path_between(g, u, v, &result) != PATH_BETWEEN_SUCCESS) {
        printf("error in calculating result");
    } else {
        printf("%s", result ? "yes" : "no");
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    graph_t *g = NULL;
    vertex_t *A = NULL, *B = NULL, *C = NULL, *D = NULL;

    // Create the graph & vertices.
    if ((g = make_graph()) == NULL
            || (A = graph_add_vertex(g, "A")) == NULL
            || (B = graph_add_vertex(g, "B")) == NULL
            || (C = graph_add_vertex(g, "C")) == NULL
            || (D = graph_add_vertex(g, "D")) == NULL) {
        fprintf(stderr, "failed to allocate memory for graph\n");
        goto cleanup;
    }

    // Create edges.
    int err_code;
    if (!(graph_add_edge(g, A, B, &err_code)
            && graph_add_edge(g, B, C, &err_code)
            && graph_add_edge(g, C, A, &err_code)
            && graph_add_edge(g, B, D, &err_code))) {
        switch(err_code) {
            case ADD_EDGE_ALLOC_FAIL:
                fprintf(stderr, "failed to allocate edge\n");
                break;
            case ADD_EDGE_INVALID_VERTEX:
                fprintf(stderr, "added edge for vertex that's not in the graph\n");
                break;
        }
        fprintf(stderr, "well, exiting now\n");
        goto cleanup;
    }

    // Aaaaand either test the algo, or dump the graph.
    if (argc < 2 || strcmp(argv[1], "test") == 0) {
        test_algo(g, A, B);
        test_algo(g, B, A);
        test_algo(g, C, B);
        test_algo(g, C, D);
        test_algo(g, D, A);
        test_algo(g, D, C);
    } else if (strcmp(argv[1], "dump") == 0) {
        dump_graph(g);
    } else {
        printf("unknown command\n");
    }

cleanup:
    // Don't need to free the vertices, the graph
    // itself is responsible for those.
    free_graph(g);
}
