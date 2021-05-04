#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_list(listint_t **head);

/**
* is_palindrome - check is palindrome
* @head: the pinter
* -----------------------------------------------
* Return int
*/
int is_palindrome(listint_t **head)
{
	listint_t *rev_list = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	rev_list = reverse_list(head);

	for (; *head && rev_list;)
	{
		if ((*head)->n != rev_list->n)
			return (0);

		*head = (*head)->next;
		rev_list = rev_list->next;
	}

	reverse_list(&rev_list);

	return (1);
}

listint_t *reverse_list(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *current = *head;
	listint_t *prev = NULL;

	for (; current;)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}