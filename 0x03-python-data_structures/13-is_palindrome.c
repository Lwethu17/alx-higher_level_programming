/*
 * File: 13-is_palindrome.c
 * Author: Ref (Mbah Nkemdinma
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: Pointer to the start node of the singly list to reverse.
 * Return: Pointer tothe head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if linked list is a palindrome.
 * @head: Pointer to the head of a singly linked list
 * Return: If the singly linked list is not palindrome - 0.
 * and 1 if the singly linked list is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *riv, *med;
	size_t size = 0, c;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;

		if ((size % 2) == 0 && temp->n != temp->next->n)
			return (0);

		temp = temp->next->next;
		riv = reverse_listint(&temp);
		med = riv;

		temp = *head;
		while (riv)
		{
			if (temp->n != riv->n)
				return (0);
			temp = temp->next;
			riv = riv->next;
		}
		reverse_listint(&med);
		return (1);
	}
}
