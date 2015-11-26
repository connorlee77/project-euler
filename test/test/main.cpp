//
//  main.cpp
//  test
//
//  Created by Connor Lee on 10/15/15.
//  Copyright (c) 2015 Connor Lee. All rights reserved.
//

#include <iostream>
#include "problems.h"


int main(int argc, const char * argv[]) {
    //int i = problem14();
    //printf("%d\n", i);

    std::vector<int> primes = primeFactorize(600851475143);
    for(int i = 0; i < primes.size(); i++) {
        std::cout << primes[i] << std::endl;
    }
    return 0;
}
