#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>


int main(){

  int pid = fork();

  // fork failed
  if(pid < 0){
    printf("fork failed");
    return 1;
  }
  // child process
  else if(pid == 0){
    execlp("./cpuemu.py",NULL);
    printf("cpu emulator error \n");
  }
  // the parent process
  else{
    pid = fork();
    if(pid < 0){
      printf("fork didnt work");
    }
    else if(pid == 0){
      sleep(1);
      execlp("./sched.py",NULL);
      printf("scheduler error \n");

      }else{
        wait(NULL);
        printf("this is the parent process ... \n");
        }
  }
  return 0;


}
