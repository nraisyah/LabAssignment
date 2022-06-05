#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <signal.h>

int main(void)
{

  void sigint_handler1(int sig1);
  void sigint_handler2 (int sig2);
  void sigint_handler3 (int sig3);
  char s[200];

  if (signal(SIGINT, sigint_handler1) == SIG_ERR){
     perror("signal");
     exit(1);
  }
 else if (signal(SIGTSTP, sigint_handler2) == SIG_ERR){
     perror("signal");
     exit(1);
  }
 else if (signal(SIGQUIT, sigint_handler3) == SIG_ERR){
     perror("signal");
     exit(1);
  }



  printf("Enter a string:\n");

  if (fgets(s, 200, stdin) == NULL)
      perror("gets");
  else
      printf("you entered: %s\n", s);

  return 0;
}

void sigint_handler1(int sig1)
{
  printf("This is a special signal handler for SIGINT. \n");
}

void sigint_handler2(int sig2)
{
  printf("This is a special signal handler for SIGTSTP. \n");
}

void sigint_handler3(int sig3)
{
  printf("This is a special signal handler for SIGQUIT. \n");
}



