class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int r = matrix.length;
        int c = matrix[0].length;
        boolean[][] visited = new boolean[r][c];
        List<Integer> result = new ArrayList<>();

        boolean isHorizontal = true;
        boolean isRight = true;
        boolean isDown = true;
        int x = 0;
        int y = 0;
        int cnt = 0;
        while (cnt < r * c) {
            result.add(matrix[x][y]);
            visited[x][y] = true;
            cnt++;
            if (isHorizontal) {
                if (isRight) {
                    if (y + 1 < c && !visited[x][y + 1]) {
                        y++;
                    } else {
                        if (isDown) {
                            x++;
                        } else {
                            x--;
                        }
                        isHorizontal = false;
                        isRight = !isRight;
                    }
                } else {
                    if (y - 1 >= 0 && !visited[x][y - 1]) {
                        y--;
                    } else {
                        if (isDown) {
                            x++;
                        } else {
                            x--;
                        }
                        isHorizontal = false;
                        isRight = !isRight;
                    }
                }
            } else {
                if (isDown) {
                    if (x + 1 < r && !visited[x + 1][y]) {
                        x++;
                    } else {
                        if (isRight) {
                            y++;
                        } else {
                            y--;
                        }
                        isHorizontal = true;
                        isDown = !isDown;
                    }
                } else {
                    if (x - 1 >= 0 && !visited[x - 1][y]) {
                        x--;
                    } else {
                        if (isRight) {
                            y++;
                        } else {
                            y--;
                        }
                        isHorizontal = true;
                        isDown = !isDown;
                    }
                }
            }
        }
        return result;
    }

}