//
//  problems.cpp
//  test
//
//  Created by Connor Lee on 10/15/15.
//  Copyright (c) 2015 Connor Lee. All rights reserved.
//

#include "problems.h"

int problemFive() {
    bool isDivisible = true;
    
    std::vector<int> divisors = {11, 13, 14, 16, 17, 18, 19};
    int x = 1;
    
    while(x > 0) {
        int i = 20;
        i *= x;
        
        for(int k = 0; k < divisors.size(); k++) {
            if(i % divisors[k] != 0) {
                isDivisible = false;
            }
        }
        
        if(isDivisible == true) {
            return i;
        }
        isDivisible = true;
        x++;
    }
    return 0;
}




int problemSix() {
    int sum = 0;
    for(int i = 1; i <= 100; i++) {
        for(int k = 1; k <= 100; k++) {
            if(k != i) {
                sum += k*i;
            }
        }
    }
    
    return sum;
}

int problemSeven(int n) {
    
    std::vector<int> sieve;
    
    for(int i = 2; i <= n; i++) {
        sieve.push_back(i);
    }
    
    int primeCount = 1;
    int currPrime = 2;
    int currPrimeIndex = 0;
    bool hasPrime = true;
    
    while(hasPrime) {
        
        for(int i = 2; i * currPrime <= n; i++) {
            sieve[i * currPrime - 2] = 0;
        }
        
        hasPrime = false;
        
        for(int i = currPrimeIndex + 1; i < sieve.size(); i++) {
            if(sieve[i] != 0) {
                primeCount++;
                currPrimeIndex = i;
                currPrime = sieve[i];
                hasPrime = true;
                break;
            }
        }
        
        if(primeCount == 10001) {
            return currPrime;
        }
    }
    
    return currPrime;
}

std::vector<int> primeFactorize(long n) {
    int i = 2;
    std::vector<int> primeFactors;
    while(i <= n){
        if(n % i == 0) {
            primeFactors.push_back(i);
            n /= i;
        } else {
            if(i == 2) {
                i = 1;
            }
            i += 2;
        }
    }
    
    return primeFactors;
}

int countDivisors(int n) {
    int i = 2;
    int prod = 1;
    int currCount = 0;
    while(i <= n){

        if(n % i == 0) {
            currCount++;
            n /= i;
        } else {
            if(currCount != 0) {
                prod *= currCount + 1;
                currCount = 0;
            }
            if(i == 2) {
                i = 1;
            }
            i += 2;
        }
    }
    
    if(currCount != 0) {
        prod *= currCount + 1;
    }

    
    return prod;
}



long problemTen(int n) {
    long sum = 0;
    
    std::vector<int> sieve;
    
    for(int i = 2; i <= n; i++) {
        sieve.push_back(i);
    }
    
    int currPrime = 2;
    int currPrimeIndex = 0;
    bool hasPrime = true;
    
    while(hasPrime) {
        
        if(currPrime >= 2000000) {
            return sum;
        }
        sum += currPrime;
        
        for(int i = 2; i * currPrime <= n; i++) {
            sieve[i * currPrime - 2] = 0;
        }
        
        hasPrime = false;
        
        for(int i = currPrimeIndex + 1; i < sieve.size(); i++) {
            if(sieve[i] != 0) {
                currPrimeIndex = i;
                currPrime = sieve[i];
                hasPrime = true;
                break;
            }
        }
    }

    return sum;
}



int problem12(int divisors) {
    
    int n = 1, triNum = 0, currDivisors = 0;

    while(currDivisors <= divisors) {
        triNum = n * (n + 1) / 2;
        
        currDivisors = countDivisors(triNum);
        
        n++;
    }
    
    return triNum;
}






