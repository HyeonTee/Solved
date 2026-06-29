class Solution {
    public void setZeroes(int[][] matrix) {
        int r = 0;
        boolean[] zeroCol = new boolean[matrix[0].length];

        while (r < matrix.length) {
            boolean isZeroRow = false;
            for (int c = 0; c < matrix[0].length; c++) {
                if (matrix[r][c] == 0) {
                    isZeroRow = true;
                    zeroCol[c] = true;
                }
            }

            if (isZeroRow) {
                Arrays.fill(matrix[r], 0);
            }

            r++;
        }

        for (int c = 0; c < zeroCol.length; c++) {
            if (zeroCol[c]) {
                for (int i = 0; i < matrix.length; i++) {
                    matrix[i][c] = 0;
                }
            }
        }
    }
}