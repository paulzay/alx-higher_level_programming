#include "lists.h"

/**
 * insert_node - insert singly linked list
 * @number: integer
 * @head: points to the head
 *
 * Description: singly linked list node structure
 * Return: pointer to node or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t  *newNode;

	newNode = malloc(sizeof(listint_t));


    if (newNode == NULL)
        return (NULL);

    if (*head == NULL)
    {
    	newNode->n = number;
    	newNode->next = NULL;
        *head = newNode;
    }

    return (newNode);
/*
	if (*head != NULL)
	{
		while (currentNode->next != NULL)
		{
			if (currentNode->n < number){
				continue;
			}
			currentNode = currentNode->next;

		}
		return (currentNode);
	}
	return (NULL);
*/
}