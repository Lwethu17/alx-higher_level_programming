#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - A singly linked list
 * @n: Pointer to an integer
 * @next: Pointer to the next node.
 * Descrption: Singly linked list node struct
 */
typedef struct listint_s
{
	int c;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
