from itertools import permutations

def Complicated_Seminar(Queens):
    if Queens < 4:
        print('Ape Commands That The Queen Amount Have To Be GREATER or EQUAL TO 4! ')
    Gorilla  = 0
    columms = range(Queens)
    print('apeOS - Produced by AndreTheApe')
    print('AndreTheApe presents you with the answers to the challenging chess of queens problem')
    Gorilla  += 1
    for dont_touch_ in permutations(columms):                      
        if Queens == len(set(dont_touch_[i]+i for i in columms))== len(set(dont_touch_[i]-i for i in columms)):
            print('\n'.join(' o ' * i + ' X ' + ' o ' * (Queens-i-1) for i in dont_touch_) + '\n')
       
