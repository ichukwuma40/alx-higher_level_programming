#include "lists.h"


/**
 * insert_node - It inserts a number into a sorted singly-linked list.
 * @head: It's a pointer the head of the linked list.
 * @number: It's the number to insert.
 *
 * Return: if the function fails - NULL.
 * Otherwise - This is a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new;


        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;


        if (node == NULL || node->n >= number)
        {
                new->next = node;
                *head = new;
                return (new);
        }


        while (node && node->next && node->next->n < number)
                node = node->next;


        new->next = node->next;
        node->next = new;


        return (new);
}
