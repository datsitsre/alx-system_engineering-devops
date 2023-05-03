#include "stdlib.h"
#include "stdio.h"
#include "unistd.h"

/**
 * infinite_while - Functions that loops
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create some zombines process
 * Return: 0
 */
int main(void)
{
	pid_t process_id;
	int child_process = 0;

	while (child_process < 5)
	{
		process_id = fork();
		if (!process_id)
			break;
		printf("Zombie process created, PID: %i\n", (int)process_id);
		child_process++;
	}
	if (process_id != 0)
	{
		infinite_while();
	}
	return (0);
}
