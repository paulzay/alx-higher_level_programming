#include "lists.h"

/**
 * check_cycle - function to check for cycle
 * @list: the list
 * Return: int
*/
int check_cycle(listint_t *list)
{
	listint_t first = list;
	listint_t second = list;

	if (list == NULL)
	{
		return (0)
	}
	while (first.next != NULL && first != NULL)
	{
		first = first.next.next;
		second = second.next
		if (first == second)
		{
			return (1);
		}
	}
	return (0)
}