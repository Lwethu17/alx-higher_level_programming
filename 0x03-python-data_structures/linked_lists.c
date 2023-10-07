#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 *  print_listint - prints all elements of a listint_t list
 *  @h: A pointer to the head of a linked list
 *  Return: the number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *present;
	unsigned int c;  /* number of nodes */

	present = h;
	c = 0;

	while (present != NULL)
	{
		printf("%i\n", present->c);
		present = present->next;
		c++;
	}
	return (c);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: A pointer to the first node of listint_t list.
 * @n: Pointer to the integer to be added in new node
 * Return: Pointer to address of new element or NULL if fails.
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *present;

	present = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (present->next != NULL)
			present = present->next;
		present->next = new;
	}
	return (new);
}

/**
 * free_listint - Frees a singly linked listint_t list
 * @head: A pointer to the list that has to be freed.
 * Return: void.
 */
void free_listint(listint_t *head)
{
	listint_t *present;

	while (head != NULL)
	{
		present = head;
		head = head->next;
		free(present);
	}
}
