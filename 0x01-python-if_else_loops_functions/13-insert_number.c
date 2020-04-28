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

	if (head == NULL)
		return (NULL);
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	node = *head;
	while (node)
	{
		if (node->next == NULL)
		{
			if (node->n > number)
			{
				temp->n = number;
				temp->next = node;
				*head = temp;
				return (*head);
			}
			else
			{
				node->next = temp;
				temp->n = number;
				temp->next = NULL;
				return (temp);
			}
		}
		else if (node->next->n > number)
		{
			temp->next = node->next;
			node->next = temp;
			temp->n = number;
			return (temp);
		}
		node = node->next;
	}
	free(temp);
	return (NULL);
}
