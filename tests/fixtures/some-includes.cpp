#include<stdio.h>
#	include <cstdlib>

int main(int argc, char* argv[])
{
  #include <something>
  return 0;
  #include not even the right syntax, but it'll still get removed
}
