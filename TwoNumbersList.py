
def two_sum(L,K):
    seen = set()
    for num in L :
        if K-num in seen:
            return (num,K-num)
        seen.add(num)

def main():
    L = list(map(int,input().split()))
    K = int(input())
    print(two_sum(L,K))



if __name__ == "__main__":
    main()