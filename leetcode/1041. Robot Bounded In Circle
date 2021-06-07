func isRobotBounded(instructions string) bool {
    x, y := 0, 0
    directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
    ptr := 0
    for _, char := range instructions {
        if char == 'G' {
            x += directions[ptr][0]
            y += directions[ptr][1]
        } else if char == 'L' {
            if ptr == 0 {
                ptr = 3
            } else {
                ptr -= 1
            }
        } else {
            if ptr == 3 {
                ptr = 0
            } else {
                ptr += 1
            }
        }
    }
    return (x == 0 && y == 0) || ptr != 0
}
