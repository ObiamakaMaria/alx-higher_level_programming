#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - This function reverses a linked list
 * @head: This is a pointer to the head of the list
 * Return: This is a pointer to the new head of the
 * reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return prev;
}

/**
 * is_palindrome - This function checks if a singly linked list
 * is a palindrome
 * @head: This is a pointer to the head of the list
 * Description: snail represent slow while hare represents fast.
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *snail = *head;
	listint_t *hare = *head;
	listint_t *first_half = *head;
	listint_t *second_half = NULL;
	while (hare != NULL && hare->next != NULL)
	{
		snail = snail->next;
		hare = hare->next->next;
	}

	if (hare != NULL)
	{
		snail = snail->next;
		/* Move slow pointer one step for odd-length lists */
	}

	/* Reverse the second half of the list */
	second_half = reverse_list(snail);

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{

			reverse_list(snail);
			return 0;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	reverse_list(snail);

	return 1;/* Palindrome */
}
