#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>

/**
 * struct listint_s - A list that is singly linked
 * @c: integer given
 * @nxt: pointer to the next node
 * Description: singly linked lists node struct
 */
typedef struct listint_s
{
	int c;
	struct listint_s *nxt;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
#endif /* LISTS_H */
