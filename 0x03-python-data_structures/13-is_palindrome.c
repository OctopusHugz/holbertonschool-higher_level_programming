#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of the list
 *
 * Return: 1 if linked list is a palindrome, or 0 if not
 **/

int is_palindrome(listint_t **head)
{
	listint_t *node;

	if (*head == NULL)
		return (1);
	node = *head;
	while (node)
	{
		if (node->n == node->next->n)
			return (1);
		node = node->next;
	}
	return (0);
}
