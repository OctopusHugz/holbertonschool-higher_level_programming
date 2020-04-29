#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include "lists.h"

/**
 * insert_node - inserts a new node with the number provided
 * @head: pointer to head of the linked list
 * @number: number to add to new node of the linked list
 *
 * Return: Address of new node, or NULL if it fails
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	temp->next = NULL;
	if (head == NULL)
	{
		*head = temp;
		return (*head);
	}
	node = *head;
	while (node)
	{
		if (node->next == NULL)
		{
			if (node->n < number)
			{
				free(temp);
				return (NULL);
			}
		}
		if (node->next->n > number)
		{
			temp->next = node->next;
			node->next = temp;
			return (temp);
		}
		node = node->next;
	}
	free(temp);
	return (NULL);
}
