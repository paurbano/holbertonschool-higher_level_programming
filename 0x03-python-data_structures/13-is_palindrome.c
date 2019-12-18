#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - tell if list is palindrome or not
 * @head: pointer to list to be freed
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	int array[4096], cont0 = 0, cont1 = 0;
	listint_t *temp = *head;

	if ((*head)->next == NULL || head == NULL)
		return (1);

	while (temp != NULL)
	{
		array[cont1] = temp->n;
		temp = temp->next;
		cont1++;
	}
	cont1--;
	for ( ; cont0 < (cont1 / 2); cont0++, cont1--)
	{
		if (array[cont0] != array[cont1])
			return (0);
	}
	return (1);
}
