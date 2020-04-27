#include "lists.h"

/**
 * check_cycle - checks for cycle
 * @list: linked list to search for cycle
 * Return: 0 if no cycle is found, 1 if cycle is found
 **/

int check_cycle(listint_t *list)
{
	listint_t *node = list;

	if (node == NULL)
		return (0);

	while (node)
	{
		if (node->next > node)
			return (1);
		node = node->next;
	}
	return (0);
}
