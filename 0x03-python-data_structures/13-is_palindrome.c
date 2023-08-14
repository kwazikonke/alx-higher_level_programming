#include "lists.h"
int recursive_check(listint_t **head, listint_t *next)
{  
	if (next == NULL){
		return (1);
	}
if (recursive_check(head, next->next) && (*head)->n == next->n)
	{
		(*head) = (*head)->next;
		return (1);
	}
	return (0);
}
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (recursive_check(head, *head));
}
