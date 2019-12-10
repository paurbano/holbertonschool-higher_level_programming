#include "lists.h"
/**
 * check_cycle - check a loop in a list.
 * @list: list
 * Description: check loop in a list
 * Return: 1 if there is a loop, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	ptr1 = list;
	ptr2 = list;

	if (list == NULL)
		return (0);

	while (ptr1->next != NULL && ptr1->next->next != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next->next;
		ptr2 = ptr2->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
