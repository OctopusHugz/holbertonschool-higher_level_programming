#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of the list
 *
 * Return: 1 if linked list is a palindrome, or 0 if not
 **/

int is_palindrome(listint_t **head)
{
	listint_t *node;
	int array[1024], i = 0, half = 0, increment = 1, decrement = 0;

	if (*head == NULL)
		return (1);
	node = *head;
	while (node)
	{
		array[i] = node->n;
		node = node->next;
		i++;
	}
	half = i / 2 - 1;
	printf("half is: %d\n", half);
	while (i > half + 1)
	{
		if (array[half - decrement] == array[half + increment])
			printf("Repeat found at %d\n", array[half - decrement]);
		else
			return (0);
		increment++, decrement++, i--;
	}
	return (1);
}
