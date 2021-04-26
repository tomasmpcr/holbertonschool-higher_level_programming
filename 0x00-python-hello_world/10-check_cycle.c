#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list;

	for (; 1 == 1;)
	{
		current = current->next;

		if (current == NULL)
			return (0);
		else if (current == list)
			return (1);
	}

	return (0);
}
