#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//basically i encrypt/decrypt messages based on a shift down a certain number of positions. quick win as ive been watching spurs finals game and its already 10 pm lol
int main(int argc, char *argv[]) {

    if (argc < 4){
        printf("Write message to be encrypted/decrypted as a string.");
        return 1;
    }

    int shift = atoi(argv[2]);
    size_t length = strlen(argv[3]);

    if(!((strcmp(argv[1], "encrypt") == 0)||(strcmp(argv[1], "decrypt") == 0))){
        printf("Only valid instructions are encrypt and decrypt.");
        return 1;
    }

    char ret[] = argv[3];

    if((strcmp(argv[1], "encrypt") == 0)){
        int i = 0;
        while(ret[i]){
            if(ret[i]>='A'&&ret[i]<='Z'){
                ret[i] = ((ret[i] - 'A' + shift) % 26) + 'A';
            }else if(ret[i]>='a'&&ret[i]<='z'){
                ret[i] = ((ret[i] - 'a' + shift) % 26) + 'a';
            }
            
            i++;
        }

        printf("%s\n",ret);
    }else{
        
    }


    return 0;
}