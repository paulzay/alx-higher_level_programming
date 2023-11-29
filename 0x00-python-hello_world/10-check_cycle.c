#include "lists.h"

/**
 * check_cycle - function to check for cycle
 * @list: the list
 * Return: int
*/
int check_cycle(listint_t *list)
{
	listint_t *first = list;

	while (first->next != NULL && first != NULL)
	{
		if (first->next == list)
		{
			return (1);
		}
		first = first->next;
	}
	return (0);
}
