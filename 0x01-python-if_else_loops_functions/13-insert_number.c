#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* insert_node - Insert node in list
* @head: pointer the list
* @number: int
* ---------------------------------------------
* Return: return a pointer the new node or a null if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *aux = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	else if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	for (; aux;)
	{
		if ((aux->next == NULL || aux->next->n > number))
		{
			if (aux->next == NULL)
				new_node->next = NULL;
			else
				new_node->next = aux->next;
			aux->next = new_node;
			return (new_node);
		}

		aux = aux->next;
	}

	return (NULL);
}
