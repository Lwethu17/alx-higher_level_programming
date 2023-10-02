#include "lists.h"

/**
 * check_syle - t checkes if a singly linked list has a cycle
 * @list: Singly linked to check
 * Return: 1 if the list has a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *yin = list;
	listint_t *yang = list;

	if (!list)
		return (0);

	while (yin && yang && yang->nxt)
	{
		yin = yin->nxt;
		yang = yang->nxt->nxt;
		if (yin == yang)
			return (1);
	}
	return (0);
}
