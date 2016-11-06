
def krakenCount(m, n):
	if m==0 or n==0:
		return 0
	if m==1 or n==1:
		return 1

	matrix = [[0 for j in xrange(n)] for i in xrange(m)]
	j=0
	while j<n:
		matrix[m-1][j]=1
		j+=1
	i=0
	while i<m-1: #m-1 was already covered in previous loop
		matrix[i][n-1]=1
		i+=1

	i=m-2
	while i>=0:
		j=n-2
		while j>=0:
			matrix[i][j]=sum([matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]])
			j-=1
		i-=1

	return matrix[0][0]


def main():
	print krakenCount(4, 4)

if __name__=="__main__":
	main()


    # static int krakenCount(int m, int n) {
    #     long[][] matrix = new long[m][n];
    #     for(int j=0; j<n; j++) matrix[m-1][j]=1;
    #     for(int i=0; i<m-1; i++) matrix[i][n-1]=1;
        
    #     for(int i=m-2; i>=0; i--){
    #         for(int j=n-2; j>=0; j--){
    #             matrix[i][j]=matrix[i+1][j]+matrix[i][j+1]+matrix[i+1][j+1];
    #         } 
    #     }
    #     return (int)matrix[0][0];
        
    # }