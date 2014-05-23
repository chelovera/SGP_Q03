
#include <stdio.h>

int main(){
	

	int n;
	char *entrada;
	scanf("%d",&n);
	scanf("%s",entrada);
	int i=0;
	for(i=0;i<n-2;i++){
		printf("%c",*(entrada+i));
		if(i%2==1)
			printf("-");
	}
		
	printf("%c",*(entrada+(n-2)));
	printf("%c\n",*(entrada+(n-1)));
	return 0;
}


