#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int _strlist(listint_t *head);
int _get_n_inde_list(listint_t *head, int index);

/**
* is_palindrome - check is palindrome
* @head: the pinter
* -----------------------------------------------
* Return int
*/
int is_palindrome(listint_t **head)
{
    int len_list = _strlist(*head);
    int i, j = len_list - 1;

    if (head == NULL || len_list == 0)
        return (1);

    for (i = 0; i < (len_list / 2); i++, j--)
    {
        if (_get_n_inde_list(*head, i) != _get_n_inde_list(*head, j))
        {
            return (0);
        }
    }

    return (1);
}

int _get_n_inde_list(listint_t *head, int index)
{
    int i;

    if (head == NULL)
        return (-1);

    for (i = 0; head; i++)
    {
        if (i == index)
            return (head->n);

        head = head->next;
    }

    return (-1);
}

int _strlist(listint_t *head)
{
    int i;

    if (head == NULL)
        return (0);

    for (i = 0; head; i++)
    {
        head = head->next;
    }
    return (i);
}