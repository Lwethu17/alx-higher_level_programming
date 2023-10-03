#include "lists.h"

/**
 * insert_node - Puts a num into a singly linked list
 * @head: Pointer to the head of the singly linked list
 * @number: The number to be inserted in a linked list
 * Return: NULL (if the code/function fails
 * otherwise - a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
