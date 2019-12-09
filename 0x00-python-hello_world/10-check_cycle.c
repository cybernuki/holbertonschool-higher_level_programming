#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: is the linked list
 * return: 0 if it does not have cycle in it. 1 in otherwise
 */
int check_cycle(listint_t *list)
{
	listint_ *faster = list;
	listint_ *slower = list;

	while (f && f->next)
	{
		slower = slower->next;
		faster = faster->next->next;

		if(slower == faster)
			return (1);
	}
	return (0);
}
