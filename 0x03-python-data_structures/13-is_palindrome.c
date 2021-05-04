#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int _strlist(listint_t **head);

/**
* is_palindrome - check is palindrome
* @head: the pinter
* -----------------------------------------------
* Return: int
*/
int is_palindrome(listint_t **head)
{
	listint_t *salto = *head;
	long int sum_n = 0, i, len_list, mid, rest = 0;

	if (head == NULL || *head == NULL)
		return (1);

	len_list = _strlist(head);

	mid = len_list / 2;
	if (len_list % 2 == 0)
		rest = 1;

	for (i = 0; salto; i++)
	{
		if (mid > i)
			sum_n += salto->n;
		else if (rest > 0)
		{
			rest--;
			continue;
		}
		else if (mid < i)
			sum_n -= salto->n;
		salto = salto->next;
	}

	if (sum_n == 0)
		return (1);

	return (0);
}

/**
* _strlist - len in a list
* @head: the pointer
* -----------------------------------------------
* Return: int
*/
int _strlist(listint_t **head)
{
	listint_t *salto = *head;
	int i;

	if (salto == NULL)
		return (0);

	for (i = 0; salto; i++)
	{
		salto = salto->next;
	}
	return (i);
}
