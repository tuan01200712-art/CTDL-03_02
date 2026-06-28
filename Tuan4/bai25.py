def bai25():
    print("Bài 25: Chứng minh tính đúng đắn của DIJKSTRA")
    print()

    print("Bất biến tham lam:")
    print("Khi một đỉnh được lấy ra khỏi hàng đợi, khoảng cách của nó đã là tối ưu nhất.")

    print("Điều kiện:")
    print("Tất cả trọng cả cảnh phải không âm (W >= 0)")
    print()

    print("Lý do:")
    print("-Nếu có cạnh âm, một đỉnh đã chốt vẫn có thể.")
    print("được cải thiện bởi một đường đi khác")

    print("Ví dụ cạnh âm:")
    print("0 -> 1 = 2")
    print("0 -> 2 = 5")
    print("2 -> 1 = -4")
    print()

    print("Dijkstra cho dist[1] = 2")
    print("Nhưng đường đi 0 -> 2 -> 1 = 1")
    print("=> Dijkstra sai khi có cạnh âm")
    print()

    print("Thuật toán thay thế: Bellman-Ford")

print(bai25())