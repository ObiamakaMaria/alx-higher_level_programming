#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * using the  Floyd's Cycle Detection(Tortoise and Hare) Algorithm
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL)
		return (0);

	tortoise = list; /* Tortoise represent slow */
	hare = list;     /* Hare represent fast */

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}

	return (0);
}
